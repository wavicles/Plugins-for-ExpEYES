'''
ExpEYES Program 
Developed as a part of GSoC Project "Plugins-for-ExpEYES"

Program to plot lissajous figures using sin and phase diff added using capacitor.
connect sin ti A1 and a 1 microfarad capacitor from A1 to A2. Connect 1K resistor from A2 to GND. Capture voltage before and after the capacitor.
'''

import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

import expeyes.eyesj
p = expeyes.eyesj.open()

from pylab import *
t1,v1,t2,v2 = p.capture2(1, 2, 300, 100)
figure(1)
plot(t1,v1)     # Plots a sine wave
figure(2)
plot(t1, v1, t2, v2) # Plots the original sine wave and a wave with 90 degree phase difference
figure(3)
plot(v1, v2) # Plots Lissajous Figure....in this case it is an ellipse
show()

