def main():
    c = 299_792_458
    m = input("Enter kilos of mass: ")
    m = float(m)
    e = m * c * c
    print("e = m * C^2...")
    print(f"m = {m} kg")
    print(f"C = {c} m/s")
    print(f"{e} joules of energy!")

if __name__ == '__main__':
    main()
