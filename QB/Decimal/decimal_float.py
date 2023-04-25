import decimal

print("Decimal from float")
pi = decimal.Decimal(3.14159)
print(pi)
print(pi.as_tuple())

print("Decimal from string")
num_str = decimal.Decimal("-123.25")
print(num_str)
print(num_str.as_tuple())