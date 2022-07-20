import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.random.randint(1000, size=50)
y = np.random.randint(1000, size=50)

even_sum = (x + y)%2

x2 = np.linspace(0, 5, 50)
y3 = 3*x2 + 0.5
y4 = 5*np.sqrt(x2)

fig, axs = plt.subplots(2,2, figsize=(8, 8))
ax = axs[0, 0]
cax = ax.scatter(x, y, c=even_sum, s=50, alpha=0.7)
ax.axis([-10,1010,-10,1010])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('fake data!')
cbar = fig.colorbar(cax)

#fig, ax = plt.subplots()
ax = axs[0, 1]
ax.plot(x2, y3, 'k--*', label='linear')
ax.plot(x2, y4, 'g-^', label='sqrt')
ax.legend(loc='best')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('some functions')

#fig, ax = plt.subplots()
ax = axs[1, 0]
ax.plot(x2, y3, 'k--*', label='linear')
ax.plot(x2, y4, 'g-^', label='sqrt')
ax.legend(loc='best')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('some functions')

#fig, ax = plt.subplots()
ax = axs[1, 1]
barheights = [3,5,1]
barlabels = ['grapes', 'oranges', 'hockey pucks']
ax.bar(range(len(barheights)), barheights)
ax.set_xticks(range(len(barheights)))
ax.set_xticklabels(barlabels, rotation=45)

plt.tight_layout()
plt.show()