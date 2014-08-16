'''
expEYES program
This is the GUI for doing all sound experiments
Developed as a part og GSoC project " Pligins for ExpEYES"

License : GNU GPL version 3
'''
import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

from Tkinter import *
import expeyes.eyesj as eyes, expeyes.eyeplot as eyeplot, expeyes.eyemath as eyemath, time, math

TIMER = 10
WIDTH  = 800        # width of drawing canvas
HEIGHT = 400        # height 
delay = 50		    # Time interval between samples
NP = 500			# Number of samples
data = [] 		    # Of the form, [ [x1,y1], [x2,y2],....] where x and y are vectors
outmask = 1
looping = False


def update():
	global data, looping, NP, delay
	if looping == False:
		return
	data = []
	if NP <= 900:
		t,v = p.capture_hr(1,NP,delay)
	else:
		t,v = p.capture(1,NP,delay)
	g.delete_lines()
	g.line(t,v)
	data.append([t,v])
	fa = eyemath.fit_sine(t, v)
	if fa != None:
		#g.line(t,fa[0], 8)
		rms = p.rms(v)
		f0 = fa[1][1] * 1000
		s = _('Freq = %5.0f Hz')%(fa[1][1]*1000)
	else:
		s = _('No Signal')
	msgwin.config(text=s)			# CRO part over	
	root.after(TIMER, update)	

def start():
	global looping, NP, delay
	if looping == True:
		return
	p.disable_actions()
	ns = int(Nsam.get())
	if 100 <= ns <=1800:			# Number of samples
		NP = ns
		g.setWorld(0,-5, NP * delay * 0.001, 5,_('mS'),_('V'))
	if A0.get() == 1:
		f = float(Freq0.get())
		fr = p.set_sqr1(f)
		Freq0.delete(0,END)
		Freq0.insert(0,'%5.1f'%fr)
	else:
		p.set_sqr1(-1)
	if A1.get() == 1:
		f = float(Freq.get())
		fr = p.set_sqr2(f)
		Freq.delete(0,END)
		Freq.insert(0,'%5.1f'%fr)
	else:
		p.set_sqr2(-1)
	looping = True
	root.after(TIMER, update)

def stop():
	global looping
	looping = False
	p.set_sqr1(-1)
	p.set_sqr2(-1)
def msg(s, col='blue'):
	msgwin.config(text=s, fg=col)



def set_sqr2():
	state = int(Sqr2.get())
	if state == 0:
		p.set_sqr2(-1)
		msg(_('SQR2 set to LOW'))
	else:
		try:
			fr = float(Freq.get())
			res = p.set_sqr2(fr)
			if res == None:
				msg(_('Enter a value between .7 to 200000 Hz'))
			else:
				msg(_('SQR2 set to %5.1f Hertz') %res)
		except:
			msg(_('Enter valid frequency, in Hertz'),'red')

def set_sqrs():
	state = int(Both.get())
	if state == 0:
		p.set_sqr1(-1)
		p.set_sqr2(-1)
		msg(_('SQR1 and SQR2 set to LOW'))
	else:
		try:
			fr = float(Freq.get())
			shift = float(Phase.get())
			res = p.set_sqrs(fr,shift)
			if res == None:
				msg(_('Enter a value between .7 to 200000 Hz'))
			else:
				msg(_('SQR1 and SQR2 set to %5.1f Hertz, Shift is %5.2f %% of Period') %(res,shift))
		except:
			msg(_('Enter valid frequency in Hertz and phase shift in percentage'),'red')

def sqr1_slider(w):
	if p == None: return
	freq = SQR1slider.get()
	if freq == 0: 
		p.set_sqr1(-1)
		msg(_('SQR1 set to LOW'))
	else:
		fs = p.set_sqr1(freq)
		msg(_('SQR1 set to %5.1f') %fs)


def do_fft():
	global data, delay, NP
	if data == []: return
	fr,tr = eyemath.fft(data[0][1], delay * 0.001)
	p.save([ [fr,tr] ], 'FFT.dat')
	p.grace([ [fr,tr] ], _('freq'), _('power'))
	msgwin.config(text = _('Fourier transform Saved to FFT.dat.'))

def save():
	global data
	s = fn.get()
	if s == '':
		return
	p.save(data, s)
	msgwin.config(text = _('Data saved to file ')+s)

def xmgrace():		# Send the data to Xmgrace
	global data
	p.grace(data, _('milliSeconds'), _('Volts'))

def quit():
	sys.exit()

p = eyes.open()
p.set_sqr1(0)

root = Tk()
#top = Frame(root)
#top.pack(side=TOP, anchor =W)
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  # Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT)	# make plot objects using draw.disp
g.setWorld(0,-5, NP * delay * 0.001, 5,_('mS'),_('V'))

if p == None:
	g.text(0, 0,_('EYES Hardware Not Found. Check Connections and restart the program'),1)
	root.mainloop()
	sys.exit()

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

l = Label(cf,text='NS =')
l.pack(side=LEFT, anchor=SW)
Nsam = Entry(cf,width = 4, bg = 'white')
Nsam.pack(side=LEFT, anchor = SW)
Nsam.insert(END,'400')

#========================= Right Side panel ===========================================
rf = Frame( width = 75, height = HEIGHT)
rf.pack(side=LEFT,  fill = BOTH, expand = 1)

#---------------------- Extra Features -----------------------------
cf = Frame(rf, border = 1, relief = SUNKEN)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

label(cf, text = _('Setting Squarewaves'), fg='blue').pack(side=TOP)
f = Frame(cf)
f.pack(side=TOP, anchor = W)
Freq = Entry(f, width = 6)
Freq.pack(side=LEFT, anchor = N)
Freq.insert(0,'1000')
Label(f,text = _('Hz. dphi=')).pack(side=LEFT, anchor = N)
Phase = Entry(f, width=4)
Phase.pack(side=LEFT, anchor=N)
Phase.insert(0,'0')
Label(f,text = '%').pack(side=LEFT, anchor = N)


f = Frame(cf)			# Setting square waves
f.pack(side=TOP)
Sqr1 = IntVar()
Checkbutton(f,text = 'SQR1', command = set_sqr1, variable = Sqr1).pack(side=LEFT, anchor=N)
Sqr2 = IntVar()
Checkbutton(f,text = 'SQR2', command = set_sqr2, variable = Sqr2).pack(side=LEFT, anchor=N)
Both = IntVar()
Checkbutton(f,text = _('BOTH'), command = set_sqrs, variable = Both).pack(side=LEFT, anchor=N)

SQR1slider = Scale(cf,command = sqr1_slider, orient=HORIZONTAL, length=180, showvalue=False, from_ = 0, to=5000, resolution=5)
SQR1slider.pack(side=TOP, anchor=W)
Canvas(cf, height = 5,  width = 100).pack(side=TOP)	# Spacer


A0 = IntVar()
cb1 = Checkbutton(cf,text =_('SQR1='), variable=A0, fg = 'blue')
cb1.pack(side=LEFT, anchor = SW)
A0.set(0)

Freq0 = Entry(cf,width = 10, bg = 'white')
Freq0.pack(side=LEFT, anchor = SW)
Freq0.insert(END,'1500')

A1 = IntVar()
cb1 = Checkbutton(cf,text =_('SQR2='), variable=A1, fg = 'blue')
cb1.pack(side=LEFT, anchor = SW)
A1.set(0)
Freq = Entry(cf,width = 10, bg = 'white')
Freq.pack(side=LEFT, anchor = SW)
Freq.insert(END,'1000')

Start = Button(cf,text =_('START'), command = start, fg = 'blue')
Start.pack(side=LEFT, anchor = SW)
Stop = Button(cf,text =_('STOP'), command = stop, fg = 'blue')
Stop.pack(side=LEFT, anchor = SW)

b = Button(cf,text =_('Xmgrace'), command=xmgrace)
b.pack(side=LEFT, anchor = SW)

b = Button(cf,text =_('FFT'), command=do_fft)
b.pack(side=LEFT, anchor = SW)

b = Button(cf,text =_('Save to'), command=save)
b.pack(side=LEFT, anchor = SW)
fn = Entry(cf,width = 10, bg = 'white')
fn.pack(side=LEFT, anchor = SW)
fn.insert(END,'sound.dat')
b = Button(cf,text =_('QUIT'), command=quit)
b.pack(side=RIGHT, anchor = SW)


mf = Frame(root)				# Message Frame below command frame.
mf.pack(side=TOP, anchor = SW)
msgwin = Label(mf,text = _('Messages'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = SW)

eyeplot.pop_image('pics/image-name.png', _('Study of sound and waves'))
root.title(_('EYES: Study of sound'))
root.mainloop()
