PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Why do programmers prefer dark mode? Because the light attracts bugs!"
SORRY = "Sorry I only tell jokes."


def main():
    user_input = input(PROMPT)  # Prompt the user for input

    if user_input == "Joke":
        print(JOKE)  # Print the joke if user enters "Joke"
    else:
        print(SORRY)  # Print the sorry message for anything else


if __name__ == '__main__':
    main()
