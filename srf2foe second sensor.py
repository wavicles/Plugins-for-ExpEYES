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
      s = '%d'%(dist)
      f.write(s + '\n')
      print s
      time.sleep(0.1)
plot(ta,da)
show()
