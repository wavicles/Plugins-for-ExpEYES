'''
pendulum waveform in real time using srf eco module
'''
import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

from Tkinter import *
import expeyes.eyesj as eyes, expeyes.eyeplot as eyeplot,  time, sys, math

WIDTH  = 600   # width of drawing canvas
HEIGHT = 400   # height    
vs = 0.034000

class Pend:
	tv = [ [], [], [] ]		# Lists for Readings
	TIMER = 10			# Time interval between reads
	MINY = 0		# Voltage range
	MAXY = 80
	running = False
	MAXTIME = 10

	def xmgrace(self):
		if self.running == True:
			return
		p.grace([self.tv])

	def start(self):
		self.running = True
		self.index = 0
		self.tv = [ [], [] ]
		try:
			self.MAXTIME = int(DURATION.get())
			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_('Time'),_('Volt'))
			Dur.config(state=DISABLED)
			self.msg(_('Starting the Measurements'))
			root.after(self.TIMER, self.update)
		except:
			self.msg(_('Failed to Start'))

	def stop(self):
		self.running = False
		Dur.config(state=NORMAL)
		self.msg(_('User Stopped the measurements'))

	def update(self):
		if self.running == False:
			return
		tt = p.srfechotime(9,0)
		dist = (tt-400) *vs/2
		if len(self.tv[0]) == 0:
			self.start_time = time.time()
			elapsed = 0
		else:
			elapsed = time.time() - self.start_time
		self.tv[0].append(elapsed)
		self.tv[1].append(dist)
		if len(self.tv[0]) >= 2:
			g.delete_lines()
			g.line(self.tv[0], self.tv[1])
		if elapsed > self.MAXTIME:
			self.running = False
			Dur.config(state=NORMAL)
			self.msg(_('Completed the Measurements'))
			return 
		root.after(self.TIMER, self.update)

	def save(self):
