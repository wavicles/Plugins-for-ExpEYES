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
      dist1 = p.srfechotime(8,3) # used channel 8 i.e. SQR1 and 3 i.e. IN1
      dist2 = p.srfechotime(9,0)  #  used channel 9 i.e. SQR2 and 0 i.e. SEN
      et = time.time() - strt
      ta.append(et)
      da1.append(dist1)
      da2.append(dist2)
      s = '%d'%(dist1)
      ss = '%d'%(dist2)
      f.write(s + '\n')
      f.write(ss + '\n')
      print s
      print ss
      time.sleep(0.1)
plot(ta,da1)
plot(ts,da2)
show()
