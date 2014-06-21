import expeyes.eyesj
p = expeyes.eyesj.open()

from pylab import *
t1,t2,v1,v2 = p.capture2(1, 2, 300, 100)
plot(t1, v1, t2, v2)
plot(v1, v2)
show()

