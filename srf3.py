
import time, math, sys
if sys.version_info.major==3:
        from tkinter import *
else:
        from Tkinter import *

sys.path=[".."] + sys.path

import expeyes.eyesj as eyes
import expeyes.eyeplot as eyeplot
import expeyes.eyemath as eyemath


p = expeyes.eyesj.open()

p.set_state(10,1)

f = open('srf.dat','r+')   # errors were beacuse file in only in write mode so changed to 'r+'

ta = []
da = []
strt = time.time()

et =0
while et < 20:
	dist = p.srfechotime(8,3)
	et = time.time() - strt
	ta.append(et)
	da.append(dist)
	s = '%5.3f\t %d'%(et,dist)
	#s = '%d\t %d'%(et,dist)
	f.write(s + '\n')
	print s
	time.sleep(0.1)



import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('srf.dat')
x1 = data[:,0]
y1 = data[:,1]
plt.plot(x1, y1)
plt.show()

plot(ta,da)
show()
