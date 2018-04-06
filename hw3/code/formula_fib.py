import math

phi = (1.0 + math.sqrt(5.0)) / 2.0
one_minus_phi = 1.0 - phi
sqrt_5 = math.sqrt(5)
def fib(n):
    # use formula to calculate the number
    try:
        f_fib = (math.pow(phi, n) - math.pow(one_minus_phi, n)) / sqrt_5
    except OverflowError:
        f_fib = -1.0
    return int(round(f_fib))
