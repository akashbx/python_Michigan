roman_to_int = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def roman_to_integer(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman.upper()):
        value = roman_to_int[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total

def integer_to_roman(num):
    int_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'),
        (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = ''
    for value, numeral in int_to_roman:
        while num >= value:
            roman += numeral
            num -= value
    return roman

def main():
    r1 = input("Enter first Roman numeral: ")
    r2 = input("Enter second Roman numeral: ")
    i1 = roman_to_integer(r1)
    i2 = roman_to_integer(r2)
    total = i1 + i2
    roman_result = integer_to_roman(total)
    print(f"The sum of {r1} and {r2} is {roman_result} ({total})")

if __name__ == "__main__":
    main()
