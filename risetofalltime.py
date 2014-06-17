'''
r2ftime(in1, in2) returns the microseconds elapsed from a rising edge on input1 to a falling edge of input2, 
they could be the same
'''

import expeyes.eyesj
p = expeyes.eyesj.open()

p.set_sqr1(1000)        # set 1kHz squarewave
print p.r2ftime(6,6)    # 6 is the readback of SQR1. Rising edge to falling edge
print p.f2rtime(6,6)    # and falling edge to rising edge

p.set_sqr1_pwm(25)      # set 488 Hz at 25% duty cycle
print p.r2ftime(6,6)    # 6 is the readback of SQR1. Rising edge to falling edge
print p.f2rtime(6,6)    # and falling edge to rising edge
