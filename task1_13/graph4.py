import numpy as np
import matplotlib.pyplot as plt

def func(x,l):
	y = eval(l)
	return y
	
f = input()
x = np.arange(-10, 10, 0.01)
y = [func(_x, f) for _x in x]
plt.xkcd()
plt.plot(x, y)

plt.show()	
