import numpy as np
import matplotlib.pyplot as plt

P=10
N = 1000
Val = np.random.uniform(low=-1, high=1, size=(N,P))
G_data = np.random.normal(loc=15, scale=100, size=(N))
Mean=np.mean(G_data)
Stdev=np.std(G_data)


xsum = np.sum(Val, axis=(1))
xnew= Mean+Stdev*xsum*np.sqrt(3. / P)
# print(xsum)

plt.hist(xnew, bins=100, label=fr'$Nowe\ dane$')
plt.hist(G_data, bins=100, label=fr'$Dane\ z\ gaussa$')
plt.title(f'Central limit th.', fontsize=18)
plt.legend(loc='upper right', fontsize=12)
plt.savefig('flat_vs_gauss.png')