def fib(n):
    # We use the classical definition of Fibonacci number
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
