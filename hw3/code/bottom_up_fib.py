def fib(n):
    """Return the nth Fibonacci number
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    n_1 = 0
    n_2 = 1
    for i in range(1, n):
        # execute n - 1 times
        n_2 = n_1 + n_2
        n_1 = n_2 - n_1
    return n_2
