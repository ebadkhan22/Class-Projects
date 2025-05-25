MAX_LENGTH = 3

def shorten(lst):
    # Remove elements from the end until the list length is MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove and get the last element
        print(last_elem)  # Print the removed element

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Shorten the list to MAX_LENGTH and print removed items

if __name__ == '__main__':
    main()
