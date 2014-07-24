from pylab import *

import expeyes.eyesj, time
p = expeyes.eyesj.open()

p.set_state(10,1)

f = open('srf.dat','r+')

ta = []
da = []
strt = time.time()

et =0
while et < 15:
	dist = p.srfechotime(8,3)
	et = time.time() - strt
	ta.append(et)
	da.append(dist)
	s = '%5.3f\t %d'%(et,dist)
	#s = '%d\t %d'%(et,dist)
	f.write(s + '\n')
	print s
	time.sleep(0.1)
# Calculate Velocity and Acceleration -----------------------------------------
