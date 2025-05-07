# Vending Machine Change Maker

def print_stock(n, d, q, o, f):
    print("Stock contains:")
    print(f"  {n} nickels")
    print(f"  {d} dimes")
    print(f"  {q} quarters")
    print(f"  {o} ones")
    print(f"  {f} fives\n")

def print_menu():
    print("Menu for deposits:")
    print("  'n' - deposit a nickel")
    print("  'd' - deposit a dime")
    print("  'q' - deposit a quarter")
    print("  'o' - deposit a one dollar bill")
    print("  'f' - deposit a five dollar bill")
    print("  'c' - cancel the purchase\n")

def get_change(change_due, stock):
    coins_dispensed = {'nickels': 0, 'dimes': 0, 'quarters': 0}
    remaining = change_due


    max_q = min(remaining // 25, stock['quarters'])
    coins_dispensed['quarters'] = max_q
    remaining -= max_q * 25

    max_d = min(remaining // 10, stock['dimes'])
    coins_dispensed['dimes'] = max_d
    remaining -= max_d * 10

    max_n = min(remaining // 5, stock['nickels'])
    coins_dispensed['nickels'] = max_n
    remaining -= max_n * 5

    return coins_dispensed, remaining

def main():
    print("Welcome to the vending machine change maker program")
    print("Change maker initialized.")

    stock = {
        'nickels': 25,
        'dimes': 25,
        'quarters': 25,
        'ones': 0,
        'fives': 0
    }

    print_stock(stock['nickels'], stock['dimes'], stock['quarters'], stock['ones'], stock['fives'])

    while True:
        user_input = input("Enter the purchase price (xx.xx) or `q` to quit: ")
        if user_input.lower() == 'q':
            total_cents = (
                stock['nickels'] * 5 +
                stock['dimes'] * 10 +
                stock['quarters'] * 25 +
                stock['ones'] * 100 +
                stock['fives'] * 500
            )
            print(f"\nTotal: {total_cents // 100} dollars and {total_cents % 100} cents")
            break

        try:
            price = round(float(user_input) * 100)
            if price < 0 or price % 5 != 0:
                print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
                continue
        except:
            print("Invalid input.\n")
            continue

        amount_due = price
        print()
        print_menu()

        while amount_due > 0:
            dollars = amount_due // 100
            cents = amount_due % 100
            print(f"Payment due: {dollars} dollars and {cents} cents")
            deposit = input("Indicate your deposit: ").lower()

            if deposit == 'n':
                stock['nickels'] += 1
                amount_due -= 5
            elif deposit == 'd':
                stock['dimes'] += 1
                amount_due -= 10
            elif deposit == 'q':
                stock['quarters'] += 1
                amount_due -= 25
            elif deposit == 'o':
                stock['ones'] += 1
                amount_due -= 100
            elif deposit == 'f':
                stock['fives'] += 1
                amount_due -= 500
            elif deposit == 'c':
                print("\nPlease take the change below.")
                refund = price - amount_due
                change_coins, leftover = get_change(refund, stock)

                for coin in ['quarters', 'dimes', 'nickels']:
                    if change_coins[coin] > 0:
                        print(f"  {change_coins[coin]} {coin}")

                stock['quarters'] -= change_coins['quarters']
                stock['dimes'] -= change_coins['dimes']
                stock['nickels'] -= change_coins['nickels']

                if leftover > 0:
                    print("Machine is out of change.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is: {leftover // 100} dollars and {leftover % 100} cents")

                print()
                print_stock(stock['nickels'], stock['dimes'], stock['quarters'], stock['ones'], stock['fives'])
                break
            else:
                print("Illegal selection.")
                continue

        if amount_due <= 0:
            print("\nPlease take the change below.")
            change = -amount_due
            if change == 0:
                print("  No change due.")
            else:
                change_coins, leftover = get_change(change, stock)
                for coin in ['quarters', 'dimes', 'nickels']:
                    if change_coins[coin] > 0:
                        print(f"  {change_coins[coin]} {coin}")

                stock['quarters'] -= change_coins['quarters']
                stock['dimes'] -= change_coins['dimes']
                stock['nickels'] -= change_coins['nickels']

                if leftover > 0:
                    print("Machine is out of change.")
                    print("See store manager for remaining refund.")
                    print(f"Amount due is: {leftover // 100} dollars and {leftover % 100} cents")

            print()
            print_stock(stock['nickels'], stock['dimes'], stock['quarters'], stock['ones'], stock['fives'])

main()