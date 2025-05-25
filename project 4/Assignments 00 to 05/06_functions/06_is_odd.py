def is_odd(number: int):
    return number % 2 != 0

def main():
    for num in range(10, 20):
        kind = "odd" if is_odd(num) else "even"
        print(f"{num} {kind}")

if __name__ == '__main__':
    main()
