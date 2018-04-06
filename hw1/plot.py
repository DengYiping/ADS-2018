import numpy as np
import matplotlib.pyplot as plt

# Best case
tupleBest = [(1000,19), (2000,24), (3000,60), (4000,81), (5000,126), (6000,198), (7000,204), (8000,256), (9000,328), (10000,404), (11000,493), (12000,577), (13000,688), (14000,785), (15000,930), (16000,1094), (17000,1236), (18000,1395), (19000,1554), (20000,1717)]
# Average case
tupleAvg = [(1000,4), (2000,16), (3000,39), (4000,66), (5000,107), (6000,154), (7000,206), (8000,273), (9000,345), (10000,430), (11000,515), (12000,616), (13000,721), (14000,838), (15000,964), (16000,1089), (17000,1234), (18000,1383), (19000,1533), (20000,1711)]
# Worst case
tupleWorst = [(1000,6), (2000,18), (3000,37), (4000,71), (5000,108), (6000,156), (7000,214), (8000,276), (9000,355), (10000,428), (11000,534), (12000,670), (13000,782), (14000,905), (15000,1039), (16000,1195), (17000,1339), (18000,1496), (19000,1676), (20000,1845)]
def breaktuples(tup):
  xs = list()
  ys = list()
  for (x_, y_) in tup:
    xs.append(x_)
    ys.append(y_)
  return xs, ys

(xsBest, ysBest) = breaktuples(tupleBest)
(xsWorst, ysWorst) = breaktuples(tupleWorst)
(xsAvg, ysAvg) = breaktuples(tupleAvg)
plt.plot(xsBest, ysBest)
plt.plot(xsWorst, ysWorst)
plt.plot(xsAvg, ysAvg)

plt.show()