# Number Theory Persistence Project

def get_digits(n):
    """Helper function to split an integer into its digits."""
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits

def additive_persistence_and_root(n):
    """Calculate additive persistence and root."""
    if n < 10:
        return 0, n

    count = 0
    while n >= 10:
        digits = get_digits(n)
        n = sum(digits)
        count += 1
    return count, n

def multiplicative_persistence_and_root(n):
    """Calculate multiplicative persistence and root."""
    if n < 10:
        return 0, n

    count = 0
    while n >= 10:
        digits = get_digits(n)
        product = 1
        for d in digits:
            product *= d
        n = product
        count += 1
    return count, n

def main():
    print("Welcome to the Number Theory Persistence Calculator!\n")

    while True:
        num = int(input("Enter a positive integer (negative to quit): "))

        if num < 0:
            print("Goodbye!")
            break

        if num < 10:
            add_persistence, add_root = 0, num
            mult_persistence, mult_root = 0, num
        else:
            add_persistence, add_root = additive_persistence_and_root(num)
            mult_persistence, mult_root = multiplicative_persistence_and_root(num)

        print(f"\nResults for {num}:")
        print(f"Additive persistence: {add_persistence}, Additive root: {add_root}")
        print(f"Multiplicative persistence: {mult_persistence}, Multiplicative root: {mult_root}\n")

if __name__ == "__main__":
    main()
