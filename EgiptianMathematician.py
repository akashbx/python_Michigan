# Egyptian Multiplication (Russian Peasant Algorithm)

def egyptian_multiplication(a, b):
    product = 0
    while b != 0:
        print(f"A = {a} and B = {b}")
        if b % 2 != 0:
            print(f"B was odd, we add A to make the product: {product + a}")
            product += a
        a *= 2
        b //= 2
    return product

def determine_sign(a, b):
    if a == 0 or b == 0:
        return "zero"
    elif (a > 0 and b > 0) or (a < 0 and b < 0):
        return "positive"
    else:
        return "negative"

def main():
    while True:
        user_input = input("\nPlease input the 2 numbers separated by a space: ")
        try:
            num1_str, num2_str = user_input.strip().split()
            num1 = int(num1_str)
            num2 = int(num2_str)
        except:
            print("Invalid input. Please enter two integers separated by a space.")
            break

        a, b = num1, num2

        abs_a = abs(a)
        abs_b = abs(b)

        print(f"A = {a} and B = {b}")
        result = egyptian_multiplication(abs_a, abs_b)

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            result = -result

        sign = determine_sign(a, b)
        print(f"Product is {sign}")
        print(f"The product of the two numbers is: {result}")

        again = input("Do you want to continue?(y/n): ")
        if again.lower() == 'y':
            print("=" * 50)
            continue
        elif again.lower() == 'n':
            print("Thanks for using the Egyptian Multiplication tool. Goodbye!")
            break
        else:
            print("Bad input, quitting.")
            break

if __name__ == "__main__":
    main()
