def main():
    # Planet gravity constants as percentages of Earth's gravity
    planet_gravity = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }

    # Milestone #1: Prompt user for their weight on Earth
    weight_earth = float(input("Enter a weight on Earth: "))

    # Milestone #2: Prompt user for a planet
    planet = input("Enter a planet: ")

    # Check if the entered planet is valid
    if planet in planet_gravity:
        # Calculate the equivalent weight on the selected planet
        weight_planet = weight_earth * (planet_gravity[planet] / 100)
        # Print the result rounded to 2 decimal places
        print(f"The equivalent weight on {planet}: {round(weight_planet, 2)}")
    else:
        print("Invalid planet entered. Please enter a valid planet from the list.")

if __name__ == '__main__':
    main()
