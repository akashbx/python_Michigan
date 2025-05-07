# Time Travel and Relativity Project

import math

def main():
    SPEED_OF_LIGHT = 299_792_458 
    SHIP_MASS_KG = 70000 

    speed_percent_str = input("Enter the percentage of the speed of light: ")
    speed_percent = float(speed_percent_str)

    velocity = (speed_percent / 100) * SPEED_OF_LIGHT

    try:
        factor = 1 / math.sqrt(1 - (velocity ** 2) / (SPEED_OF_LIGHT ** 2))
    except ZeroDivisionError:
        print("ERROR: You cannot travel at or above the speed of light!")
        return

    increased_mass = SHIP_MASS_KG * factor
    print(f"\nOriginal ship mass: {SHIP_MASS_KG:,.2f} kg")
    print(f"Increased ship mass at {speed_percent}% c: {increased_mass:,.2f} kg")

    destinations = {
        "Alpha Centauri": 4.3,
        "Barnard’s Star": 6.0,
        "Betelgeuse": 309,
        "Andromeda Galaxy": 2_000_000
    }

    print("\nAstronauts' travel time to destinations:")
    for name, distance in destinations.items():
        reduced_time = distance / factor
        print(f"- {name}: {reduced_time:.4f} years")

if __name__ == "__main__":
    main()
