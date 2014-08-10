'''
ExpEYES Program
Developed as a part of GSoC Project " Plugins for ExpEYES"
License : GNU GPL version 3

Program to plot oscillations of a spring loaded with mass and determine spring constant 
Use DC motor as sensor...............
'''

from pylab import *
import expeyes.eyesj, time
p = expeyes.eyesj.open()

p.set_state(10,1)

f = open('srf.dat','r+')

ta = []
da = []
strt = time.time()

et =0
while et < 30:
dist = p.srfechotime(8,3) # for using two srf modules use 8,3 or 9,0 channels
et = time.time() - strt
ta.append(et)
da.append(dist)
s = '%5.3f\t %d'%(et,dist)
#s = '%d\t %d'%(et,dist)
f.write(s + '\n')
print s
time.sleep(0.1)

print p.get_frequency(3) # to get frequency at pin 3 this is giving time out error
'''
to fit the sine wave for spring expt.
'''
import expeyes.eyemath as em
p = expeyes.eyesj.open()
t,v= p.capture(3,400,100)
vfit, par = em.fit_sine(t,v)
print par[1] # second parameter is frequency
print(t,v)
plot(t, vfit)
show()
plot(ta,da)
show()
