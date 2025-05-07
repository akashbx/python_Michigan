# Description: Generate a Latin Square of given order and top-left value

def main():
    print("Welcome to the Latin Square Generator!\n")

    order = int(input("Enter the order of the Latin square (n): "))
    top_left = int(input("Enter the top-left number (1 to n): "))

    if top_left < 1 or top_left > order:
        print("Invalid input: top-left number must be between 1 and the order of the square.")
        return

    print("\nGenerated Latin Square:\n")

    for row in range(order):
        for col in range(order):
            value = ((top_left - 1 + row + col) % order) + 1
            print(value, end=" ")
        print()

if __name__ == "__main__":
    main()
