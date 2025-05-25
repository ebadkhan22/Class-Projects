import time

def countdown_timer(seconds):
    while seconds > 0:
        print(seconds, end=" ", flush=True)
        time.sleep(1)
        seconds -= 1

    print("\nTime's up! ⏰")

def start_timer():
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("❌ Please enter a valid number.")

# Start the timer
start_timer()
