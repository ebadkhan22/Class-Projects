def get_first_element(lst):
    print(lst[0])

def main():
    lst = input("Enter a list of elements separated by spaces: ").split()
    get_first_element(lst)

if __name__ == '__main__':
    main()
