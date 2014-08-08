from pylab import *
import expeyes.eyesj, time
p = expeyes.eyesj.open()

p.set_state(10,1)

f = open('srf.dat','w')

ta = []
da = []
strt = time.time()

et =0
while et < 20:
	dist = p.srfechotime(9,0)
	et = time.time() - strt
	ta.append(et)
	da.append(dist)
	s = '%d'%(dist)
	f.write(s + '\n')
	print s
	time.sleep(0.1)
	
figure(1)
#position-time plot
plot(ta,da)
#add a label to the x axis
xlabel('Time')
#add a label to the y axis
ylabel('Distance')
#add a title
title('Position - Time Graph')
#save the figure to the current diretory as a png file
savefig('plot_1.png')
#open a second figure
figure(2)

'''#use the subplot function to generate multiple panels within the same plotting window
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
plot(ta,da)
'''
show()
