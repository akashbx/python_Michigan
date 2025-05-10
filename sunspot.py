# Sunspots Analysis - Project #6 - CSE 231

def read_daily_data(filename):
    monthly_data = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 4:
                continue 
            year, month, day, *rest = parts
            if not rest:
                continue 
            try:
                count = float(rest[0])
                key = (int(year), int(month))
                if key not in monthly_data:
                    monthly_data[key] = []
                monthly_data[key].append(count)
            except ValueError:
                continue
    return monthly_data

def compute_monthly_averages(monthly_data):
    monthly_averages = []
    for key in sorted(monthly_data):
        year, month = key
        average = sum(monthly_data[key]) / len(monthly_data[key])
        monthly_averages.append((year, month, average))
    return monthly_averages

def write_monthly(filename, monthly_averages):
    with open(filename, 'w') as f:
        for year, month, avg in monthly_averages:
            f.write(f"{year} {month:02d} {avg:.2f}\n")

def compute_smoothed(monthly_averages):
    smoothed = []
    for i in range(6, len(monthly_averages) - 6):
        smoothed_value = (
            monthly_averages[i - 6][2] +
            2 * monthly_averages[i - 5][2] +
            2 * monthly_averages[i - 4][2] +
            2 * monthly_averages[i - 3][2] +
            2 * monthly_averages[i - 2][2] +
            2 * monthly_averages[i - 1][2] +
            2 * monthly_averages[i][2] +
            2 * monthly_averages[i + 1][2] +
            2 * monthly_averages[i + 2][2] +
            2 * monthly_averages[i + 3][2] +
            2 * monthly_averages[i + 4][2] +
            2 * monthly_averages[i + 5][2] +
            monthly_averages[i + 6][2]
        ) / 24
        year, month = monthly_averages[i][0], monthly_averages[i][1]
        smoothed.append((year, month, smoothed_value))
    return smoothed

def write_smoothed(filename, smoothed_data):
    with open(filename, 'w') as f:
        for year, month, value in smoothed_data:
            f.write(f"{year} {month:02d} {value:.2f}\n")

def main():
    daily_file = "RADAILY.PLT"
    monthly_file = "MONTHLY"
    smoothed_file = "SMOOTHED"

    data = read_daily_data(daily_file)
    monthly_avg = compute_monthly_averages(data)
    write_monthly(monthly_file, monthly_avg)

    smoothed = compute_smoothed(monthly_avg)
    write_smoothed(smoothed_file, smoothed)

    print("MONTHLY and SMOOTHED files have been generated.")

if __name__ == "__main__":
    main()