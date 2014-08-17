'''
In addition to OD1, SQR1 and SQR2 also can be configured as digital outputs.
'''

import expeyes.eyesj
p = expeyes.eyesj.open()

#connect OD1 to IN1
p.set_state(10, 1)     # set OD1 to HIGH
print p.get_state(3)   # level on IN1

#connect SQR1 to IN2
p.set_sqr1(0)          # set SQR1 to HIGH
print p.get_state(4)   # level on IN2

p.set_sqr1(-1)         # set SQR1 to LOW
print p.get_state(4)   # level on IN2

p.set_state(8, 1)     # set SQR1 to HIGH
print p.get_state(4)   # level on IN2
