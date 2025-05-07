# GDP and Unemployment Comparison

def get_average_gdp(filename, year):
    """Reads the GDP file and returns the average GDP for the specified year"""
    with open(filename, 'r') as file:
        gdp_data = file.readlines()
    
    index = year - 1948
    if index < 0 or index >= len(gdp_data):
        return None

    # Split the line into parts
    line_parts = gdp_data[index].split()
    
    # Skip any non-numeric (like '1960q2') and convert the rest to float
    gdp_values = []
    for part in line_parts:
        try:
            gdp_values.append(float(part))
        except ValueError:
            continue  # Skip parts that cannot be converted

    if not gdp_values:
        return None

    avg_gdp = sum(gdp_values) / len(gdp_values)
    return avg_gdp


def get_average_unemployment(filename, year):
    """Reads the unemployment file and returns the average unemployment for the specified year"""
    with open(filename, 'r') as file:
        uemp_data = file.readlines()
    
    index = year - 1948
    if index < 0 or index >= len(uemp_data):
        return None

    try:
        uemp_values = list(map(float, uemp_data[index].split(',')))
    except ValueError:
        return None

    avg_uemp = sum(uemp_values) / len(uemp_values)
    return avg_uemp


def main():
    gdp_file = input("GDP File Name: ")
    uemp_file = input("Unemployment File Name: ")

    while True:
        try:
            year = int(input("Year to examine: "))
            if 1948 <= year <= 2008:
                break
            else:
                print("Bad year, try again")
        except ValueError:
            print("Invalid input. Please enter a year between 1948 and 2008.")

    avg_gdp = get_average_gdp(gdp_file, year)
    avg_uemp = get_average_unemployment(uemp_file, year)

    if avg_gdp is not None and avg_uemp is not None:
        print(f"For {year}, average GDP: {avg_gdp:.3f} and average unemployment: {avg_uemp:.3f}")
    else:
        print("Data not available for the given year.")


if __name__ == "__main__":
    main()
