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
    if i < len(ir_y)-2:
        a = (ir_y[i+2]-2*ir_y[i+1]+ir_y[i])/((t[i+2]-t[i+1])*(t[i+1]-t[i]))
        ir_a.append(a)

#Create Plots ----------------------------------------------------------------

subplot(3,1,1)
plot(t,ir_y,'r')   #Acceleration Plot
title('IR LED Movement')
#xlabel('Time')
ylabel('Position')

subplot(3,1,2)
plot(t[1:],ir_v)
#title('Velocity of IR')
#xlabel('time')
ylabel('Velocity')

subplot(3,1,3)
plot(t[2:],ir_a)
#title('Acceleration of IR')
xlabel('time')
ylabel('Acceleration')

show()
plot(ta,da)
show()

