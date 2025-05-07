# Checks if a guessed number SLAYER satisfies the puzzle condition.

def main():
    print("Guess a six-digit number SLAYER so that the following equation is true,")
    print("where each letter stands for the digit in the position shown:\n")
    print("SLAYER + SLAYER + SLAYER = LAYERS\n")

    slayer = int(input("Enter your guess for SLAYER: "))

    if slayer < 100000 or slayer > 999999:
        print("Your guess is incorrect:")

        print("SLAYER must be a 6-digit number.")
    else:
        sum_value = slayer * 3


        S = (slayer // 100000) % 10
        L = (slayer // 10000) % 10
        A = (slayer // 1000) % 10
        Y = (slayer // 100) % 10
        E = (slayer // 10) % 10
        R = slayer % 10

        layers = 100000*L + 10000*A + 1000*Y + 100*E + 10*R + S

        if sum_value == layers:
            print("Your guess is correct:\n")
            print(f"SLAYER + SLAYER + SLAYER = {sum_value}")
            print(f"LAYERS = {layers}")
        else:
            print("Your guess is incorrect:")
            print(f"SLAYER + SLAYER + SLAYER = {sum_value}")
            print(f"LAYERS = {layers}")

    print("Thanks for playing.")

main()