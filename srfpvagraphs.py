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
print "Calculating velocity and acceleration..."
va = []
aa = []
for i in range(0,len(da)-1):
    # Calculate Velocity
    v = (da[i+1]-da[i])/(ta[i+1]-ta[i])
    va.append(v)
    
    # Calculate Acceleration
    if i < len(da)-2:
        a = (da[i+2]-2*da[i+1]+da[i])/((ta[i+2]-ta[i+1])*(ta[i+1]-ta[i]))
        aa.append(a)

#Create Plots ----------------------------------------------------------------

subplot(3,1,1)
plot(ta,da,'r')   # Position plot
title('Position-Time Graph')
xlabel('Time')
ylabel('Position')

subplot(3,1,2)
plot(ta[1:],va)  	# Velocity Plot
title('Velocity-Time Graph')
xlabel('time')
ylabel('Velocity')

subplot(3,1,3)
plot(ta[2:],aa)		# Acceleration Plot
title('Acceleration-Time Graph')
xlabel('time')
ylabel('Acceleration')

show()


