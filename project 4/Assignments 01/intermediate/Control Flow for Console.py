import random

# Constants
NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    # Play NUM_ROUNDS rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers for the player and the computer
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {your_number}")

        # Get user's guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Safeguard user input
        while guess not in ["higher", "lower"]:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Evaluate the guess
        if (guess == "higher" and your_number > computer_number) or (
                guess == "lower" and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")

    # Final message based on score
    print("Thanks for playing!")
    print("Here are your results:")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == '__main__':
    main()
