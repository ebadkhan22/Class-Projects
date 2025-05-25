import random

def play_round():
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    user_input = input("Type 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    while user_input not in choices:
        print("❌ Invalid input. Please try again.")
        user_input = input("Type 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    user = choices[user_input]
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"🧠 You chose {user}, Computer chose {computer}")

    if user == computer:
        print("🤝 It's a tie!")
        return "tie"
    elif is_win(user, computer):
        print("✅ You won this round!")
        return "user"
    else:
        print("❌ Computer won this round!")
        return "computer"

def is_win(player, opponent):
    return (
        (player == "rock" and opponent == "scissors") or
        (player == "scissors" and opponent == "paper") or
        (player == "paper" and opponent == "rock")
    )

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors — Best of 5!")
    print("Use: 'r' = rock, 'p' = paper, 's' = scissors")

    user_score = 0
    computer_score = 0
    round_number = 1

    while user_score < 3 and computer_score < 3:
        print(f"\n🔁 Round {round_number} — Score: You {user_score} | Computer {computer_score}")
        result = play_round()

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        # Tie does not count

        round_number += 1

    print("\n🏁 Final Result:")
    print(f"🔢 Final Score: You {user_score} - {computer_score} Computer")

    if user_score > computer_score:
        print("🏆 Congratulations! You won the best of 5!")
    else:
        print("🤖 The computer won the best of 5. Better luck next time!")

# Start the game
play_game()
