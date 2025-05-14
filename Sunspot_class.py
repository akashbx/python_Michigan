def init_dictionary(file_string, sunspot_dict):
    try:
        with open(file_string, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue 
                try:
                    year = int(parts[0])
                    month = int(parts[1])
                    sunspots = float(parts[2])
                except ValueError:
                    continue  

                if 1749 <= year <= 2011 and 1 <= month <= 12:
                    if year not in sunspot_dict:
                        sunspot_dict[year] = [0] * 12
                    sunspot_dict[year][month - 1] = sunspots
    except FileNotFoundError:
        raise IOError(f"File '{file_string}' not found.")

def avg_sunspot(sunspot_dict, year_tuple=(1749, 2011), month_tuple=(1, 12)):
    start_year, end_year = year_tuple
    start_month, end_month = month_tuple

    if start_year < 1749 or end_year > 2011 or start_year > end_year:
        raise KeyError("Year range out of bounds (1749–2011)")

    if start_month < 1 or end_month > 12 or start_month > end_month:
        raise IndexError("Month range out of bounds (1–12)")

    total = 0.0
    count = 0

    for year in range(start_year, end_year + 1):
        if year not in sunspot_dict:
            continue
        for month in range(start_month - 1, end_month):
            value = sunspot_dict[year][month]
            if value != 0:
                total += value
                count += 1

    return total / count if count > 0 else 0.0
def main():
    sunspot_dict = {}
    init_dictionary("MONTHLY.txt", sunspot_dict)

    avg1 = avg_sunspot(sunspot_dict, (1850, 1851), (1, 6))
    print(f"Average (Jan-Jun 1850–1851): {avg1:.2f}")

    avg2 = avg_sunspot(sunspot_dict)
    print(f"Average (full dataset): {avg2:.2f}")

if __name__ == "__main__":
    main()