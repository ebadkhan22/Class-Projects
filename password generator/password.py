import re
import random
import string
import streamlit as st


def check_password_strength(password):
    score = 0
    feedback = []


    common_passwords = {"password123", "12345678", "qwerty123", "admin", "letmein", "welcome"}
    if password in common_passwords:
        return 0, "❌ This password is too common and easily guessable. Choose a unique one."


    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.\n")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.\n")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).\n")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).\n")

    # Strength Rating
    if score == 4:
        return score, "✅ Strong Password!"
    elif score == 3:
        return score, "⚠️ Moderate Password - Consider adding more security features."
    else:
        return score, "\n".join(feedback) + "\n❌ Weak Password - Improve it using the suggestions above."


def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(12))


# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    score, message = check_password_strength(password)
    st.write(message)

    if score < 4:
        st.write("🔹 Suggested Strong Password: ", generate_strong_password())
