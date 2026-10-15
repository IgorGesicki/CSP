import numpy as np
import matplotlib.pyplot as plt

N = 1
T = 1000
T_vec = np.linspace(0,T,T)
x = np.zeros(N)
delta = np.random.normal(loc=0, scale=1, size=(T,N))
delta[0,:]=0

print(delta)
x = np.cumsum(delta, axis=(0))
print(x)
for i in range(N):
    plt.plot(T_vec, x[:,i] ,label=f"Cząstka {i}")

plt.xlabel(r'$T\ step$', fontsize=16)
plt.ylabel(r'$x\ possition$', fontsize=16)
plt.legend(loc='upper right', fontsize=12)
plt.show()

# print(x)



