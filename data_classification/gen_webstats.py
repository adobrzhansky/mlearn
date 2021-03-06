import os
import scipy as sp
from scipy.stats import gamma
import matplotlib.pyplot as plt

from utils import DATA_DIR, CHART_DIR

sp.random.seed(3)  # to reproduce the data later on

x = sp.arange(1, 31*24)
y = sp.array(200*(sp.sin(2*sp.pi*x/(7*24))), dtype=int)
y += gamma.rvs(15, loc=0, scale=100, size=len(x))
y += 2 * sp.exp(x/100.0)
y = sp.ma.array(y, mask=[y<0])
print(sum(y), sum(y<0))

plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(5)], 
           ['week %i' %(w+1) for w in range(5)])
plt.autoscale(tight=True)
plt.grid()
plt.savefig(os.path.join(CHART_DIR, "1400_01_01.png"))

sp.savetxt(os.path.join(DATA_DIR, "web_traffic.tsv"), 
           list(zip(x, y)), delimiter="\t", fmt="%s")
