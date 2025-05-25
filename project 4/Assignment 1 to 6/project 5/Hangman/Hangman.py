import random


word_list = [
    'python', 'hangman', 'developer', 'keyboard', 'function', 'algorithm', 'data',
    'machine', 'science', 'artificial', 'intelligence', 'programming', 'compiler',
    'debugging', 'variable', 'class', 'object', 'method', 'inheritance', 'recursion',
    'syntax', 'exception', 'constructor', 'parameter', 'iterator', 'framework', 'database',
    'network', 'server', 'cloud', 'encryption', 'security', 'application', 'deployment',
    'simulation', 'interface', 'performance', 'optimization', 'parallel', 'multithreading',
    'scripting', 'documentation', 'frontend', 'backend', 'repository', 'version', 'testing',
    'debug', 'refactor', 'refactoring', 'visualization', 'developer', 'program', 'project',
    'solution', 'matrix', 'functionality', 'expression', 'analysis', 'dependency', 'library'
]
secret_word = random.choice(word_list)
guessed_letters = []
lives = 6

print("🔠 Welcome to Hangman!")
print("_ " * len(secret_word))

while lives > 0:
    guess = input("📥 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")

    # Show current progress
    word_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_display += letter + " "
        else:
            word_display += "_ "
    print(word_display.strip())

    # Check for win
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You guessed the word! You win!")
        break
else:
    print(f"💀 You ran out of lives. The word was '{secret_word}'. Better luck next time!")
