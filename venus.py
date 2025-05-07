# Venus Crater Mining - Extract eligible craters

def get_crater_tuple(line_str):
    fields = line_str.strip().split(",")
    try:
        crater_id = int(fields[0])
        name = fields[1]
        lat = float(fields[2])
        lon = float(fields[3])
        diameter = float(fields[4])
        return (crater_id, name, lat, lon, diameter)
    except (IndexError, ValueError):
        return None

def read_craters(filename):
    crater_list = []
    while True:
        try:
            with open(filename, 'r') as fp:
                next(fp)  # Skip header
                for line in fp:
                    crater = get_crater_tuple(line)
                    if crater:
                        crater_list.append(crater)
                return crater_list
        except FileNotFoundError:
            print("File not found.")
            filename = input("Enter a filename: ")

def get_eligible_craters(crater_list):
    eligible = []
    for crater in crater_list:
        _, _, lat, lon, diameter = crater
        if -40 <= lat <= 50 and 40 <= lon <= 135 and diameter >= 60:
            eligible.append(crater)
    return eligible

def write_craters(eligible_list):
    with open("craters.txt", "w") as fp:
        fp.write(f"{'ID':>3} {'Name':<15} {'Latitude':>9} {'Longitude':>9} {'Diameter':>9}\n")
        for crater in eligible_list:
            crater_id, name, lat, lon, diameter = crater
            fp.write(f"{crater_id:>3} {name:<15} {lat:9.2f} {lon:9.2f} {diameter:9.2f}\n")

def main():
    filename = input("Enter a filename: ")
    crater_list = read_craters(filename)
    eligible_craters = get_eligible_craters(crater_list)
    write_craters(eligible_craters)
    print(f"{len(eligible_craters)} eligible craters written to 'craters.txt'.")

if __name__ == "__main__":
    main()
