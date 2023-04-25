import decimal

print("Round to floor")
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_FLOOR
print(decimal.Decimal(20) / decimal.Decimal(17))

print("Round to ceiling")
decimal.getcontext().rounding = decimal.ROUND_CEILING
print(decimal.Decimal(20) / decimal.Decimal(17))

print("Round to half even")
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
print(decimal.Decimal(20) / decimal.Decimal(9))