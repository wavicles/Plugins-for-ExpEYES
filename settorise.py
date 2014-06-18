'''
set2rtime(out, in) returns the time in  microseconds elapsed from setting the specified output
to a rising edge on input. 
Similar functions are: clr2rtime(out, in) , set2ftime(out, in) and clr2ftime(out, in)

Connect 1k resistor from OD1 to IN1, 1uF capacitor from IN1 to GND
'''

import expeyes.eyesj, time
p = expeyes.eyesj.open()

p.set_state(10,0)           # set OD1 to LOW
print p.set2rtime(10,3)     # Time from setting OD1 to detection of HIGH on IN1
time.sleep(1)
print p.clr2ftime(10,3)     # Time from clearing OD1 to detection of LOW on IN1

