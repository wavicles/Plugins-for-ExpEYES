import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('srf.dat')  # uses data from srf.dat
x1 = data[:,0]
y1 = data[:,1]
plt.plot(x1, y1)
plt.show()
