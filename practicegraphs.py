#import numpy functions and types
from pylab import *
x = arange(1,10,0.5)
xsquare = x**2
xcube = x**3
xsquareroot = x**0.5
#open figure 1
figure(1)
#basic plot
plot(x,xsquare)
#add a label to the x axis
xlabel('abscissa')
#add a label to the y axis
ylabel('ordinate')
#add a title
title('A practice plot.')
#save the figure to the current diretory as a png file
savefig('plot_1.png')
#open a second figure
figure(2)
#do two plots:
#one with red circles with no line joining them
#and another with green plus signs joined by a dashed curve
plot(x, xsquare, 'ro', x, xcube,'g+--')
#x and y labels, title
xlabel('abscissa')
ylabel('ordinate')
title('More practice.')
#add a legend
legend(('squared', 'cubed'))
#save the figure
savefig('plot_2.png')
figure(3)
#use the subplot function to generate multiple panels within the same plotting window
subplot(3,1,1)
#plot black stars with dotted lines
plot(x, xsquareroot,'k*:')
title('square roots')
subplot(3,1,2)
#plot red right-pointing triangles with dashed lines
plot(x, xsquare,'r>-')
title('squares')
subplot(3,1,3)
#plot magenta hexagons with a solid line
plot(x, xcube,'mh-')
title('cubes')
savefig('plot_3.png')
#show() should be the last line
show()
