class Matrix:
    def __init__(self, n11, n12, n21, n22):
        self.n11 = n11
        self.n12 = n12
        self.n21 = n21
        self.n22 = n22
    def mul(self, other):
        n11 = self.n11 * other.n11 + self.n12 * other.n21
        n12 = self.n11 * other.n12 + self.n12 * other.n22
        n21 = self.n21 * other.n11 + self.n22 * other.n21
        n22 = self.n21 * other.n12 + self.n22 * other.n22
        return Matrix(n11, n12, n21, n22)
    def p(self):
        print("{} {}\n{} {}".format(self.n11,
            self.n12, self.n21, self.n22))
        return

base = Matrix(1, 1, 1, 0)
def fib_matrix(n):
    if n == 1:
        return base
    m_half = fib_matrix(n // 2)
    # half value
    res = m_half.mul(m_half)
    if n % 2 == 1:
        # deal with reminder
        res = res.mul(base)
    return res

def fib(n):
    if n == 0:
        return 0
    return fib_matrix(n).n21
