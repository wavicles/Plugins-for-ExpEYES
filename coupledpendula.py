
from pylab import *
import expeyes.eyesj, time
p = expeyes.eyesj.open()

DURATION = 15
ta = []
tb = []
va = []
vb = []
f = open('pend_wave.dat','w')

start = p.get_voltage_time(1)[0]
start2 = p.get_voltage_time(2)[0]

while 1:
    res = p.get_voltage_time(1)
    tm = res[0] - start			# elapsed time
    ta.append(tm)
    va.append(res[1])
    res2 = p.get_voltage_time(2)
    tm2 = res2[0] - start			# elapsed time
    tb.append(tm2)
    vb.append(res2[1])
    ss = '%6.3f %6.3f'%(tm,res[1])
    print ss
    f.write(ss+'\n')
    if tm > DURATION:
       break


figure(1)      
plot(ta,va)
figure(2)
plot(tb,vb)
figure(3)
plot(ta,va, tb,vb)
show()
