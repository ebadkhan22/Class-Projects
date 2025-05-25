import random

def guess_number():
    print("🎲 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < number:
                print("Too low. Try again.")
            elif guess > number:
                print("Too high. Try again.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} tries.")
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guess_number()
