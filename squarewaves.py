import expeyes.eyesj
p = expeyes.eyesj.open()

from pylab import *
p.set_sqr1(150)  # Generate 150 Hz  on SQR1
p.set_sqr1(500)  # Generate 500 Hz  on SQR2

res = p.capture2(6,7, 300, 100)  # returns two sets of data
plot(res[0], res[1])   # SQR1 readback
plot(res[2], res[3])   # SQR2 readback
show()
