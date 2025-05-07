# Simple calculator with input validation and loop
def main():
    print("Welcome to the Simple Calculator!\n")

    while True:
        
        expr = input("Enter expression (operand operator operand): ")

        
        tokens = expr.split()
        if len(tokens) != 3:
            print("Error: Please enter exactly 3 items separated by spaces.")
            continue

        operand1, operator, operand2 = tokens

        
        try:
            num1 = float(operand1)
            num2 = float(operand2)
        except ValueError:
            print("Error: Operands must be valid numbers.")
            continue

     
        result = None
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                result = num1 / num2
        else:
            print(f"Error: Unsupported operator '{operator}'. Use +, -, *, or /.")
            continue

        print(f"Result: {result:.2f}")

        again = input("Do you want to perform another calculation? (yes or no): ")
        if again.strip().lower() not in ['yes', 'y']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
