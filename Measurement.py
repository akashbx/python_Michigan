# Measurement conversion project

def main():
    mph = float(input("Enter speed in miles per hour (mph): "))

    meters_per_sec = mph * 1609.34 / 3600

    meters_per_day = meters_per_sec * 86400
    barleycorns_per_day = meters_per_day * 117.647

    meters_per_fortnight = meters_per_sec * 14 * 24 * 3600
    furlongs_per_fortnight = meters_per_fortnight / 201.168

    mach = meters_per_sec / 344.4

    psl = (meters_per_sec / 299_792_458) * 100

    print("\nConversion Results:")
    print(f"Barleycorns per day:     {barleycorns_per_day:.2e}")
    print(f"Furlongs per fortnight:  {furlongs_per_fortnight:.2f}")
    print(f"Mach number:             {mach:.6f}")
    print(f"Percent of speed of light: {psl:.10f}%")

if __name__ == "__main__":
    main()
