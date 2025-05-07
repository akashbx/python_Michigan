# proj10-app.py
from currency import Currency

def parse_input(entry):
    parts = entry.strip().split()
    if len(parts) != 2:
        raise ValueError("Invalid input format")
    amount = float(parts[0])
    code = parts[1].upper()
    if code not in Currency.VALID_CODES:
        raise ValueError("Invalid currency code")
    return Currency(amount, code)

def main():
    balance = Currency(1000.0, 'USD')
    print("Initial account balance:", balance)

    while True:
        user_input = input("Enter an expense (amount and currency, e.g. '10 EUR') or 'q' to quit: ")
        if user_input.lower() in ['q', 'quit']:
            print("Final balance:", balance)
            break

        try:
            expense = parse_input(user_input)
            converted_expense = expense.convert_to('USD')
            balance = balance - converted_expense
            print("Balance:", balance)
            if balance.amount < 0:
                print("Account overdrawn.")
                break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
