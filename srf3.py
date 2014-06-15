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
	dist = p.srfechotime(8,3)
	et = time.time() - strt
	ta.append(et)
	da.append(dist)
	s = '%5.3f\t %5.3f'%(et,dist)
	#s = '%d\t %d'%(et,dist)
	f.write(s + '\n')
	print s
	time.sleep(0.1)


import numpy as np
import matplotlib.pyplot as plt
with open('srf.dat', 'r') as f2:
	lines = f2.readlines()
	data = [line.split()for line in lines] 
	data2 = np.asfarray(data)
	x1 = data2[:,0]
	y1 = data2[:,1]
	plt.plot(x1, y1)
plt.show()


# ss = '%5.3f\t %5.3f'%(vd,i)
 
# print ss
 # f.write(ss+'\n')

'''
#clf()
#clear
M=fscanfMat('srf.dat');
t=M(:,1);
len=length(t);
x=M(:,2);
dt=diff(t);
dx=diff(x);
v=dx./dt;
dv=diff(v);
a=dv./dt(1:len-2);
subplot(311), title("position"),
plot(t,x,'b');
subplot(312), title("velocity"),
plot(t(1:len-1),v,'g');
subplot(313), title("acceleration"),
plot(t(1:len-2),a,'r');
import numpy as np
import matplotlib.pyplot as plt
with open('data.dat', 'r') as f2:
lines = f2.readlines()
data = [line.split()for line in lines] 
data2 = np.asfarray(data)
x1 = data2[:,0]
y1 = data2[:,1]
plt.plot(x1, y1)
plt.show()
'''

plot(ta,da)
show()
