# GDP and Personal Income Data Analysis

import csv
import pylab

REGIONS = ['far_west', 'great_lakes', 'mideast', 'new_england',
           'plains', 'rocky_mountain', 'southeast', 'southwest']

FIELDS = {
    "Pop": 2, "GDP": 3, "PI": 4, "Sub": 5, "CE": 6, "TPI": 7, "GDPp": 8, "PIp": 9
}

def open_file():
    while True:
        try:
            fname = input("Input a file: ")
            fp = open(fname, 'r', newline='')
            return fp
        except FileNotFoundError:
            print("File not found. Try again.")

def read_data(fp):
    region = input("Specify a region: ").lower()
    while region not in REGIONS:
        print("Invalid region. Try again.")
        region = input("Specify a region: ").lower()

    reader = csv.reader(fp)
    next(reader)  # skip header
    data = []

    for row in reader:
        if row[1].strip().lower() == region:
            try:
                pop = float(row[2])
                gdp = float(row[3])
                pi = float(row[4])
                gdp_per_capita = (gdp * 1000) / pop
                pi_per_capita = (pi * 1000) / pop
                row.extend([gdp_per_capita, pi_per_capita])
                data.append(row)
            except:
                continue
    return data

def display_data(data):
    max_gdp = max(data, key=lambda x: x[8])
    min_gdp = min(data, key=lambda x: x[8])
    max_pi = max(data, key=lambda x: x[9])
    min_pi = min(data, key=lambda x: x[9])

    print()
    print(f"{max_gdp[0]} has the highest GDP per capita at ${max_gdp[8]:,.2f}")
    print(f"{min_gdp[0]} has the lowest GDP per capita at ${min_gdp[8]:,.2f}")
    print(f"{max_pi[0]} has the highest personal income per capita at ${max_pi[9]:,.2f}")
    print(f"{min_pi[0]} has the lowest personal income per capita at ${min_pi[9]:,.2f}")
    print()

    print("Data by state:")
    header = f"{'State':<15}{'Pop(m)':>8}{'GDP(b)':>10}{'PI(b)':>10}{'Sub(m)':>10}{'CE(b)':>10}{'TPI(b)':>10}{'GDPpc':>12}{'PIpc':>12}"
    print(header)
    print("-" * len(header))

    for row in sorted(data, key=lambda x: x[0]):
        print(f"{row[0]:<15}{float(row[2]):>8.2f}{float(row[3]):>10.2f}{float(row[4]):>10.2f}"
              f"{float(row[5]):>10.2f}{float(row[6]):>10.2f}{float(row[7]):>10.2f}"
              f"{row[8]:>12.2f}{row[9]:>12.2f}")

def plot_regression(x, y):
    m, b = pylab.polyfit(x, y, 1)
    pylab.plot(x, [m*i + b for i in x], label=f"Y={m:.2f}X+{b:.2f}")
    pylab.legend()

def create_plot(data):
    print()
    x_label = input("Enter x-axis field (Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp): ")
    y_label = input("Enter y-axis field (Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp): ")

    if x_label not in FIELDS or y_label not in FIELDS:
        print("Invalid field(s).")
        return

    x_idx = FIELDS[x_label]
    y_idx = FIELDS[y_label]

    x_vals = [float(row[x_idx]) for row in data]
    y_vals = [float(row[y_idx]) for row in data]
    labels = [row[0] for row in data]

    pylab.figure()
    pylab.scatter(x_vals, y_vals)

    for i, label in enumerate(labels):
        pylab.text(x_vals[i], y_vals[i], label)

    plot_regression(x_vals, y_vals)

    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.title(f"{y_label} vs {x_label}")
    pylab.show()

def main():
    fp = open_file()
    data = read_data(fp)
    display_data(data)

    response = input("\nDo you want to create a plot? (yes/no): ").lower()
    if response == "yes":
        create_plot(data)


if __name__ == "__main__":
    main()