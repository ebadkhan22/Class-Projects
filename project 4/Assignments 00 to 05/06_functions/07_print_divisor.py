def print_divisors(num: int):
    print(f"Here are the divisors of {num}")
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            print(divisor)

def main():
    user_number = int(input("Enter a number: "))
    print_divisors(user_number)

if __name__ == '__main__':
    main()
