# Palindromic Integers using the 196-algorithm

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    return int(str(n)[::-1])

def check_196_algorithm(n, max_iterations=60):
    count = 0
    while count < max_iterations:
        rev = reverse_number(n)
        n += rev
        count += 1
        if is_palindrome(n):
            return True, n  # Non-Lychrel
    return False, n       # Lychrel

def main():
    print("196-algorithm: Palindromic Integer Generator")
    
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    natural_palindromes = 0
    non_lychrel = 0
    lychrel = 0
    lychrel_list = []

    for num in range(start, end + 1):
        if is_palindrome(num):
            natural_palindromes += 1
        else:
            success, result = check_196_algorithm(num)
            if success:
                non_lychrel += 1
            else:
                lychrel += 1
                lychrel_list.append(num)

    print(f"Natural palindromes: {natural_palindromes}")
    print(f"Non-Lychrel numbers: {non_lychrel}")
    print(f"Lychrel numbers: {lychrel}")
    if lychrel > 0:
        print("Lychrel number(s):", ", ".join(str(x) for x in lychrel_list))

if __name__ == "__main__":
    main()
