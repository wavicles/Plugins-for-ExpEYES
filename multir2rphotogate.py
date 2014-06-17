'''
multi_r2rtime(input, nskip) returns the microseconds elapsed between two rising edges. 
nskip is the number of edges to be skipped in between.
LED from SQR1 to GND
Photo-transistor collector to SEN, emitter to GND
'''

import expeyes.eyesj
p = expeyes.eyesj.open()

p.set_sqr1(0)               # set HIGH on  SQR1, for LED

for k in range(10):
	print p.multi_r2rtime(0,1)    # skip alternate light interruptions
