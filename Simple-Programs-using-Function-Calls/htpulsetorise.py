'''
htpulse2rtime(out, in) returns the microseconds elapsed from sending a HIGH TRUE pulse on output to
to a rising edge on input. 
Similar functions are: ltpulse2rtime(out, in) , htpulse2ftime(out, in) and ltpulse2ftime(out, in)

Wire a monoshot using IC555. Connect pin2 of 555 to OD1 and pin3 to IN1
Power the IC from SQR2
'''
import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

import expeyes.eyesj
p = expeyes.eyesj.open()

p.set_sqr2(0)                   # set SQR1 to HIGH
p.set_pulsewidth(2)            # 2 usec pulse width
p.set_state(10,1)               # set OD1 to HIGH
print p.ltpulse2rtime(10,3)     # Time from setting OD1 to detection of HIGH on IN1
