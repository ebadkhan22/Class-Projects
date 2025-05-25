def make_sentence(word: str, part_of_speech: int):
    templates = [
        f"I am excited to add this {word} to my vast collection of them!",
        f"It's so nice outside today it makes me want to {word}!",
        f"Looking out my window, the sky is big and {word}!"
    ]

    if 0 <= part_of_speech <= 2:
        print(templates[part_of_speech])
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")


def main():
    term = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    kind = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(term, kind)


if __name__ == '__main__':
    main()
