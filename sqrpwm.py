'''
The outputs SQR1 and SQR2 can be configured to generate Pulse Width Modulated waveform at various
frequencies. 
set_sqr1_pwm(duty_cycle_in_percent, number_to_set_frequency)
The second argument is 14 by default, generating 488 Hz. 
Reducing it by 1 doubles the frequency and increasing it by 1 halves the frequency.
set_sqr2_pwm() does the same for SQR2 output
'''
import expeyes.eyesj
p = expeyes.eyesj.open()

from pylab import *
p.set_sqr1_pwm(35)          # 35% duty cycle wave on SQR1. Default frequency 488 Hz
print p.get_frequency(6)
p.set_sqr1_pwm(25, 13)      # 25% duty cycle wave on SQR1. requency 488 Hz
print p.get_frequency(6)
p.set_sqr1_pwm(25, 15)      # 25% duty cycle wave on SQR1. Default frequency 488 Hz
print p.get_frequency(6)

t,v = p.capture(6, 300, 100)
plot(t,v)
show()
