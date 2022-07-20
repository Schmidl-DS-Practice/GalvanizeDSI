import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')

#a = np.random.randint(1000, size=50) #generates array populated with ints from 0 to 999
#b = np.random.randint(1000, size=50)

#plt.figure() #use before every plot to define it. works the same as 'fig, ax'
#even_sum = (a+b) % 2
#c=even_sum -->inside ax.scatter

#x = np.linspace(0,5, 10)
#y1 = 3*x + 0.5
#y2 = 5*np.sqrt(x)

barheights = [3, 5, 1]
barlabels = ['grapes', 'oranges', 'hockey pucks'] 

fig, ax = plt.subplots(1, 1)
#ax.plot(x, y1, alpha=0.7, label='x and y1', color='green', marker='p', linestyle='--')
#ax.plot(x, y2, alpha=0.4, label='x and y2', color='purple', marker='h', linestyle='dashdot')
#ax.axis([-0.5, 6, -0.5, 16.5])
ax.bar(np.arange(len(barheights)), barheights)
x_pos = np.arange(len(barheights))
ax.set_xticks(x_pos)
ax.set_xticklabels(barlabels, rotation=15)
ax.set_title('bar plot')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.legend()
#ax.set_xscale('log') set log scale
#cbar = fig.colorbar(cax)

#ax.set_xlim() #change range of values. [xmin, xmax]
#ax.set_ylim() #change range of values [ymin, ymax]

plt.show() #call after every plot to print it