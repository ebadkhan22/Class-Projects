def add_three_copies(my_list, data):
    # Add the data to the list three times
    for i in range(3):
        my_list.append(data)


def main():
    # Get user input for the message to copy
    message = input("Enter a message to copy: ")

    # Initialize an empty list
    my_list = []

    # Print the list before adding any copies
    print("List before:", my_list)

    # Add three copies of the message to the list
    add_three_copies(my_list, message)

    # Print the list after the operation
    print("List after:", my_list)


if __name__ == "__main__":
    main()
