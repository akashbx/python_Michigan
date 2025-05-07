# Part B: Analyze measles vaccination data by year and income level

def open_file():
    while True:
        filename = input("Enter the name of the input file: ")
        try:
            return open(filename, "r")
        except FileNotFoundError:
            print("File not found. Try again.")

def process_file(file):
    year_input = input("Enter the year: ").strip()
    income_level_input = input("Enter income level (1=LI, 2=LMI, 3=UMI, 4=HI): ").strip()

    income_map = {
        "1": "WB_LI",
        "2": "WB_LMI",
        "3": "WB_UMI",
        "4": "WB_HI"
    }

    if income_level_input not in income_map:
        print("Invalid income level input.")
        return

    income_code = income_map[income_level_input]
    count = 0
    total_percent = 0
    min_country = ""
    max_country = ""
    min_percent = 101
    max_percent = -1

    for line in file:
        country = line[:50].strip()
        income = line[50:56].strip()
        percent_str = line[56:59].strip()
        year = line[-5:].strip()

        if year == year_input and income == income_code:
            try:
                percent = int(percent_str)
            except:
                continue

            count += 1
            total_percent += percent

            if percent < min_percent:
                min_percent = percent
                min_country = country

            if percent > max_percent:
                max_percent = percent
                max_country = country

    if count == 0:
        print("No records match the criteria.")
    else:
        avg = total_percent / count
        print(f"Number of matching records: {count}")
        print(f"Average percent vaccinated: {avg:.1f}")
        print(f"Lowest: {min_country} ({min_percent}%)")
        print(f"Highest: {max_country} ({max_percent}%)")

def main():
    file = open_file()
    process_file(file)
    file.close()

main()
