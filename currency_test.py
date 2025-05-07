# proj10-test.py
from currency import Currency

print("Creating two currency objects:")
c1 = Currency(100, 'USD')
c2 = Currency(50, 'EUR')
print("c1:", c1)
print("c2:", c2)

print("\nConverting c2 to USD:")
converted = c2.convert_to('USD')
print("converted:", converted)

print("\nAdding c1 + c2:")
sum_result = c1 + c2
print("sum:", sum_result)

print("\nSubtracting c1 - c2:")
sub_result = c1 - c2
print("difference:", sub_result)

print("\nCompare c1 > c2:")
print("c1 > c2:", c1 > c2)

print("\nAdding c1 + 25.5:")
print("result:", c1 + 25.5)

print("\nUsing reversed addition (25.5 + c1):")
print("result:", 25.5 + c1)
