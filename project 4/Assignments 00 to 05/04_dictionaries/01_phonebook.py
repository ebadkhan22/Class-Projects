def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break  # Exit the loop if an empty string is entered for the name
        number = input("Number: ")
        phonebook[name] = number  # Store the name and number in the dictionary

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break  # Exit the loop if an empty string is entered for the name
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()  # Read phone numbers from user
    print_phonebook(phonebook)         # Print all phonebook entries
    lookup_numbers(phonebook)         # Allow the user to lookup numbers


# Python boilerplate.
if __name__ == '__main__':
    main()
