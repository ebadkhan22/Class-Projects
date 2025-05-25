import random

def computer_guess():
    print("🧠 Think of a number between 1 and 100 and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one number left to guess

        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please respond with 'H', 'L', or 'C'.")

    print(f"🎉 Yay! I guessed your number {guess} in {attempts} tries.")

# Run the game
computer_guess()
