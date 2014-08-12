'''
expEYES program
Developed as a part of GSoC Project "Plugins-for-ExpEYES"

'''
#import numpy functions and types
#Program to plot lissajous figures using pylab functions
from pylab import *

t = arange(0, 2*pi, pi/400)
x = cos(t)

#case 1
figure(1)
n=1
phi=0
subplot(1,2,1)
plot(cos(t),cos(n*t+phi),'r.')
title('n=1, phi=0')

#case 2
n=1
phi=pi/4
subplot(1,2,2)
plot(cos(t),cos(n*t+phi),'r.')
title('n=1, phi=pi/4')

figure(2)
#case 3
n=1
phi=pi/2
subplot(1,2,1)
plot(cos(t),cos(n*t+phi),'r.')
title('n=1, phi=pi/2')

#case 4
n=2
phi=pi/2
subplot(1,2,2)
plot(cos(t),cos(n*t+phi),'r.')
title('n=2, phi=pi/2')

#case 5
figure(3)
n=4
phi=pi/2
subplot(1,2,1)
plot(cos(t),cos(n*t+phi),'r.')
title('n=4, phi=pi/2')

#case 6
n=8
phi=-pi/3
subplot(1,2,2)
plot(cos(t),cos(n*t+phi),'r.')
title('n=5, phi=-pi/3')
savefig('plot_lissajous.png')

#show() should be the last line
show()
