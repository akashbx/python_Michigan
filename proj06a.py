#Part A: Copy selected measles vaccination data by year

def main():
    try:
        infile = open("measles.txt", "r")
    except FileNotFoundError:
        print("Error: 'measles.txt' not found.")
        return

    outfile_name = input("Enter the name of the output file: ")
    try:
        outfile = open(outfile_name, "w")
    except:
        print("Error: cannot create output file.")
        infile.close()
        return

    year_filter = input("Enter a year filter (e.g., '1987', '19', or 'all'): ").strip()

    for line in infile:
        line_year = line[-5:].strip()
        if year_filter.lower() in ["", "all", "ALL"] or line_year.startswith(year_filter):
            outfile.write(line)

    infile.close()
    outfile.close()
    print("Filtered data written to", outfile_name)

main()
