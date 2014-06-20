import expeyes.eyesj
p = expeyes.eyesj.open()

from pylab import *
p.set_sqrs(150,25)  # Generate 150 Hz  on both with 90 degree phase shift (25% of T)

res = p.capture2(6,7, 300, 100)  # returns two sets of data
plot(res[0], res[1])   # SQR1 readback
plot(res[2], res[3])   # SQR2 readback
show()
