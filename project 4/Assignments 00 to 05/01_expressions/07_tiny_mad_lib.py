SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "


def main():
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    sentence = f"{SENTENCE_START}{adjective} {noun} {verb}!"
    print(sentence)


if __name__ == '__main__':
    main()
