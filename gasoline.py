# Gasoline Conversion Program

def main():
    gallons_str = input("Please enter the number of gallons of gasoline: ")
    gallons = float(gallons_str)

    LITERS_PER_GALLON = 3.7854
    GALLONS_PER_BARREL = 19.5
    CO2_PER_GALLON = 20.0
    GAS_ENERGY = 115000.0
    ETHANOL_ENERGY = 75700.0
    PRICE_PER_GALLON = 4.00

    liters = gallons * LITERS_PER_GALLON
    barrels = gallons / GALLONS_PER_BARREL
    co2 = gallons * CO2_PER_GALLON
    ethanol_equiv = (gallons * GAS_ENERGY) / ETHANOL_ENERGY
    price = gallons * PRICE_PER_GALLON

    print(f"Liters: {liters:.2f}")
    print(f"Barrels of oil: {barrels:.2f}")
    print(f"Pounds of CO2: {co2:.2f}")
    print(f"Ethanol energy equivalent (gallons): {ethanol_equiv:.2f}")
    print(f"Price: ${price:.2f}")

if __name__ == "__main__":
    main()