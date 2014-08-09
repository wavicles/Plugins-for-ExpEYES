'''
Program to plot lissajous figures by setting SQR1and SQR2 with some phase difference
connect sqr1 to  A1 and and sqr2 to A2.
'''

from pylab import *
import expeyes.eyesj
p = expeyes.eyesj.open()


#p.set_sqr1(8000)
#p.set_sqr2(4000)
p.set_sqrs(8000,13) #econd parameter is phase difference in percentage


t1,v1,t2,v2 = p.capture2(1, 2, 400, 16)
figure(1)
plot(t1,v1)
figure(2)
plot(t1,v1, t2,v2)
figure(3)
plot(v1,v2)
show()
