import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y1 = np.sin(x)
y2=np.sin(2*x)
y3=np.sin(x)*np.exp(-x**2/25)


plt.figure(figsize=(8,5),dpi=150)
plt.plot(x,y1, 'r--', lw = 2, label=r'$\sin(x)$')
plt.plot(x,y2, 'b--', lw = 2, label=r'$\sin(2x)$')
plt.plot(x,y3, 'g', lw = 2, label=r'$\sin(x) \exp(-\frac{x^2}{25})$')

plt.title('Test title', fontsize=18)
plt.xlabel(r'$x data$', fontsize=16)
plt.ylabel(r'$functions$', fontsize=16)
plt.grid(alpha=0.6)
plt.legend(loc='upper right', fontsize=12)
# plt.show()
plt.savefig('patterns.png')