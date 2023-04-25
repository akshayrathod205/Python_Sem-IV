from decimal import Decimal

def round_off(x):
    x_decimal = Decimal(str(x))
    remainder = x_decimal.remainder_near(Decimal('0.10'))
    if abs(remainder) == Decimal('0.05'):
        return x_decimal
    else:
        return x_decimal - remainder

print(round_off(4.78))