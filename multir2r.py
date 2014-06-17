'''
Program for measuring time intervals using photogates
'''
import expeyes.eyesj
p = expeyes.eyesj.open()

p.set_sqr1(1000)              # set 1kHz on  SQR1
t = p.multi_r2rtime(6,9)    # 6 is the readback of SQR1. Time of 10 cycles
print t
t = t * 1.0e-6  # to seconds
print 'Frequency = ', (10.0/t)

'''
connect photogate led to SQR1 anf GND. Detector From SEn and GND
'''
