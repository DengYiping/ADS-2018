from fib_timer import calculate
import numpy as np
import matplotlib.pyplot as plt

upper_bdd = 100
def plotList(lst):
    bdd = upper_bdd
    if(len(lst) < upper_bdd):
        bdd = len(lst)
    plt.plot(np.log(list(range(0, bdd))), np.log(lst[0:bdd]))

r_times, b_times, f_times, m_times = calculate()
plotList(r_times)
plotList(b_times)
plotList(f_times)
plotList(m_times)
plt.show()
