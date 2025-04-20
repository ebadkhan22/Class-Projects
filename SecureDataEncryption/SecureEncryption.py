import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from dotenv import load_dotenv




load_dotenv()
MASTER_PASSWORD = os.getenv("MASTER_PASSWORD")


# Constants
DATA_FILE = 'stored_data.json'
KEY_FILE = 'secret.key'
LOCKOUT_DURATION = 60  # in seconds

# Load or create encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
    return key

# Load or initialize data storage
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

# Hashing with PBKDF2
def hash_passkey(passkey, salt=b'streamlit_salt'):
    return hashlib.pbkdf2_hmac('sha256', passkey.encode(), salt, 100000).hex()

# Encryption/Decryption functions
KEY = load_key()
cipher = Fernet(KEY)

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

# Session states
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'lockout_time' not in st.session_state:
    st.session_state.lockout_time = 0
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = True

# Load data
stored_data = load_data()

# Lockout check
if st.session_state.failed_attempts >= 3:
    if time.time() - st.session_state.lockout_time < LOCKOUT_DURATION:
        st.warning("⏳ Too many failed attempts. Please wait a minute before trying again.")
        st.stop()
    else:
        st.session_state.failed_attempts = 0

# Navigation
st.title("🛡️ Secure Data Encryption System")
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("This app allows you to **securely store and retrieve data** using encryption and passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    username = st.text_input("Enter Your Username:")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if username and user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            stored_data[username] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            save_data(stored_data)
            st.success("✅ Data stored securely!")
        else:
            st.error("⚠️ All fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    username = st.text_input("Enter Your Username:")
    passkey = st.text_input("Enter Your Passkey:", type="password")

    if st.button("Decrypt"):
        if username and passkey:
            user_entry = stored_data.get(username)
            if user_entry and user_entry["passkey"] == hash_passkey(passkey):
                decrypted_text = decrypt_data(user_entry["encrypted_text"])
                st.success(f"✅ Decrypted Data: {decrypted_text}")
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect username or passkey! Attempts remaining: {attempts_left}")

                if st.session_state.failed_attempts >= 3:
                    st.session_state.lockout_time = time.time()
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.session_state.is_logged_in = False
                    time.sleep(5)
                    st.rerun()

        else:
            st.error("⚠️ All fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Replace with secure mechanism in production
            st.session_state.failed_attempts = 0
            st.session_state.is_logged_in = True
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            time.sleep(5)
            st.rerun()
        else:
            st.error("❌ Incorrect master password!")