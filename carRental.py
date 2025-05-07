# Car Rental Billing Program

import math

def main():
    while True:
        code = input("Enter classification code (Q to quit): ").strip().upper()
        if code == 'Q':
            print("Bye!")
            break

        days = int(input("Enter number of days: "))
        odo_start = int(input("Enter starting odometer reading: "))
        odo_end = int(input("Enter ending odometer reading: "))

        if odo_end >= odo_start:
            miles_driven = (odo_end - odo_start) / 10
        else:
            miles_driven = ((1000000 + odo_end) - odo_start) / 10

        amount = 0.0

        if code == 'B':
            amount = 40 * days + 0.25 * miles_driven

        elif code == 'D':
            base = 60 * days
            avg_daily_miles = miles_driven / days
            if avg_daily_miles > 100:
                extra_miles = miles_driven - (100 * days)
                mileage_charge = 0.25 * extra_miles
            else:
                mileage_charge = 0
            amount = base + mileage_charge

        elif code == 'W':
            weeks = math.ceil(days / 7)
            avg_weekly_miles = miles_driven / weeks
            base = 190 * weeks
            if avg_weekly_miles <= 900:
                mileage_charge = 0
            elif avg_weekly_miles <= 1500:
                mileage_charge = 100 * weeks
            else:
                extra_miles = miles_driven - (1500 * weeks)
                mileage_charge = 200 * weeks + 0.25 * extra_miles
            amount = base + mileage_charge

        else:
            print("Invalid classification code.")
            amount = 0.0

        print("\nCustomer summary:")
        print(f"Classification code: {code}")
        print(f"Rental days:         {days}")
        print(f"Odometer start:      {odo_start}")
        print(f"Odometer end:        {odo_end}")
        print(f"Miles driven:        {miles_driven:.1f}")
        print(f"Amount billed:      ${amount:.2f}\n")

if __name__ == "__main__":
    main()