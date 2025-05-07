# Number Guessing Game (Mastermind-style)

import random

MAX_GUESSES = 10

def is_valid_number(number):
    return number.isdigit() and len(number) == 5 and len(set(number)) == 5

def get_feedback(secret, guess):
    correct_digits = sum(1 for d in guess if d in secret)
    correct_positions = sum(1 for i in range(5) if guess[i] == secret[i])
    return correct_digits, correct_positions

def get_secret_number():
    while True:
        option = input("Do you want the computer to generate the secret number? (yes/no): ").lower()
        if option == "yes":
            digits = random.sample('0123456789', 5)
            return ''.join(digits)
        elif option == "no":
            while True:
                number = input("Administrator, enter a 5-digit secret number (no repeats): ")
                if is_valid_number(number):
                    print("\\n" * 50)  
                    return number
                else:
                    print("Invalid number. Must be 5 digits, no repeats.")
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    print("Welcome to the Number Guessing Game!")
    print(f"You have {MAX_GUESSES} tries to guess the secret number.")
    print("Each guess must be a 5-digit number with no repeated digits.")
    print("Type 'quit' to end the game early.\\n")

    secret = get_secret_number()
    guess_count = 0

    while guess_count < MAX_GUESSES:
        guess = input(f"Guess #{guess_count + 1}: ").strip()
        if guess.lower() == "quit":
            print(f"You quit the game after {guess_count} guess(es). The secret number was {secret}.")
            return
        if not is_valid_number(guess):
            print("Invalid guess. Must be a 5-digit number with no repeated digits.")
            continue

        guess_count += 1
        correct_digits, correct_positions = get_feedback(secret, guess)

        print(f"Guess: {guess} | Correct Digits: {correct_digits} | Correct Positions: {correct_positions}")

        if guess == secret:
            print(f"Congratulations! You guessed the number in {guess_count} tries.")
            return

    print(f"Sorry, you ran out of guesses. The secret number was {secret}.")

if __name__ == "__main__":
    main()