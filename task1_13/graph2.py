import numpy as np
import math
import pylab
from matplotlib import mlab

tmin = -10
tmax = 10

dt = 0.01
tlist = mlab.frange(tmin, tmax, dt)

pylab.ion()

for i in range(100):
	xlist = [math.sin(t + i) for t in tlist]
	ylist = [math.cos(2*t) for t in tlist]
	pylab.clf()
	pylab.plot(xlist, ylist)
	pylab.draw()
	
pylab.close()	
	

