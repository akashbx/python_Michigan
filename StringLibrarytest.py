import StringLibrary as lib

def test(func_name, input_vals, expected):
    result = func_name(*input_vals)
    print(f"Testing {func_name.__name__}{input_vals} → Expected: {expected}, Actual: {result}")

test(lib.is_alpha, ("ABCxyz",), True)
test(lib.is_alpha, ("123abc",), False)
test(lib.is_digit, ("123456",), True)
test(lib.is_digit, ("abc123",), False)

test(lib.to_lower, ("HeLLo WoRLd!",), "hello world!")
test(lib.to_upper, ("HeLLo WoRLd!",), "HELLO WORLD!")

test(lib.find_chr, ("hello", "l"), 2)
test(lib.find_chr, ("hello", "z"), -1)
test(lib.find_chr, ("hello", "ll"), -1)

test(lib.find_str, ("banana", "na"), 2)
test(lib.find_str, ("banana", "xyz"), -1)

test(lib.replace_chr, ("hello", "l", "x"), "hexxo")
test(lib.replace_chr, ("hello", "ll", "x"), "")

test(lib.replace_str, ("hi hi", "hi", "yo"), "yo yo")
test(lib.replace_str, ("abc", "", "_"), "_a_b_c_")
