def get_last_element(lst):
    print(lst[len(lst)-1])

def main():
    lst = input("Enter a list of elements separated by spaces: ").split()
    get_last_element(lst)

if __name__ == '__main__':
    main()
