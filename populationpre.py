# Population Prediction Program


def main():
    CURRENT_POPULATION = 307357870
    SECONDS_PER_YEAR = 365 * 24 * 60 * 60

    BIRTH_RATE = 7
    DEATH_RATE = 13
    IMMIGRATION_RATE = 35

    years = int(input("Enter the number of years into the future: "))

    births_per_year = SECONDS_PER_YEAR // BIRTH_RATE
    deaths_per_year = SECONDS_PER_YEAR // DEATH_RATE
    immigrants_per_year = SECONDS_PER_YEAR // IMMIGRATION_RATE

    net_change_per_year = births_per_year - deaths_per_year + immigrants_per_year

    future_population = CURRENT_POPULATION + (net_change_per_year * years)

    print(f"Predicted population after {years} years: {future_population}")

if __name__ == "__main__":
    main()