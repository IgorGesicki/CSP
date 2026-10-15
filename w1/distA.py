import numpy as np
import matplotlib.pyplot as plt

N = 10000
Val = np.random.normal(loc=15, scale=100, size=(N))

Mean=np.mean(Val)
Stdev=np.std(Val)



plt.hist(Val, bins=100, label=fr'$Mean:{Mean}, \sigma:{Stdev}$')
plt.title(f'Numbers from normal dist. Mean={Mean}, sigma={Stdev}', fontsize=10)
plt.legend(loc='upper right', fontsize=10)
plt.savefig('gauss.png')