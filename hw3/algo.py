def mul(x, y):
    n = max(num of digit of x, num of digit of y)
    if n == 1:
        return x * y
    x_l, x_r = left half of x, right half of x
    y_l, y_r = left half of y, right half of y
    p_1 = mul(x_l, y_l)
    p_2 = mul(x_r, y_r)
    p_3 = mul(x_l + x_r, y_l + y_r)
    return p_1 * 2^n + (p_3 - p_1 - p_2) * 2^(n / 2) + p_2
