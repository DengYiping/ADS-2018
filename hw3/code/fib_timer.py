from time import time
import matrix_fib
import formula_fib
import bottom_up_fib
import recursive_fib

def timer(f):
    # a functional wrapper
    # will return the result in microsec
    def wrapper(*arg, **kw):
        t1 = time()
        res = f(*arg, **kw)
        t2 = time()
        return int(round((t2 - t1) * 1000000000)), res
    return wrapper

def avgTimer(f):
    timer_f = timer(f)
    def wrapper(*arg, **kw):
        s = 0
        for _ in range(5):
            t, _ = timer_f(*arg, **kw)
            s += t
        return s // 5
    return wrapper

def feeder(f):
    f_wrapped = avgTimer(f)
    t1 = time()
    n = 0
    res = []
    while (time() - t1) < 5.0:
        n += 1
        t = f_wrapped(n)
        res.append(t)
    return res

def calculate():
    """Quick check of correctness of 4 approaches
    >>> recursive_fib.fib(20) == bottom_up_fib.fib(20)
    True
    >>> formula_fib.fib(20) == recursive_fib.fib(20)
    True
    >>> matrix_fib.fib(20) == formula_fib.fib(20)
    True
    """
    recursive_times = feeder(recursive_fib.fib)
    bottom_up_times = feeder(bottom_up_fib.fib)
    formula_times = feeder(formula_fib.fib)
    matrix_times = feeder(matrix_fib.fib)
    return recursive_times, bottom_up_times, formula_times, matrix_times

sampleNum = {0, 1, 10, 20, 50, 100, 200, 400, 800, 1600, 3200, 6400, 128000}

def createTable(lst):
    count = 0
    for t in lst:
        if count in sampleNum:
            print("n = {}, t = {}".format(count, t))
        count += 1
if __name__ == "__main__":
    r_times, b_times, f_times, m_times = calculate()
    print("recursive:")
    createTable(r_times)
    print("bottom up:")
    createTable(b_times)
    print("formula:")
    createTable(f_times)
    print("m_times:")
    createTable(m_times)
