'''
connect sin ti A1 and a 1 microfarad capacitor from A1 to A2. Connect 1K resistor from A2 to GND. Capture voltage before and after the capacitor.
'''


import expeyes.eyesj
p = expeyes.eyesj.open()

from pylab import *
t1,v1,t2,v2 = p.capture2(1, 2, 300, 100)
figure(1)
plot(t1,v1)

plot(t1, v1, t2, v2)
plot(v1, v2)
show()

