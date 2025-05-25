def get_list(lst):
    print(lst)

def main():
    lst = input("Enter a list of elements separated by spaces: ").split()
    get_list(lst)

if __name__ == '__main__':
    main()
