def print_ones_digit(num: int):
    print("The ones digit is", num % 10)

def main():
    value = int(input("Enter a number: "))
    print_ones_digit(value)

if __name__ == '__main__':
    main()
