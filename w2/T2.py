import numpy as np
import matplotlib.pyplot as plt

N = 100000
T = 100
x_func = np.linspace(-30,30,10000)
x = np.zeros(N)
def gaussian_vals(x,t):
    return 1/np.sqrt(2*np.pi*t)*np.exp(-x**2/(2*t))
    
    

fig, ((ax1), (ax2), (ax3)) = plt.subplots(1, 3, sharex=True, sharey=True)
fig.suptitle('Sharing x per column, y per row')

for ax in fig.get_axes():
    ax.label_outer()
    

for t in range(T+1):
    delta = np.random.normal(loc=0, scale=1, size=(N))
    x += delta
    if t == 1:
        ax1.hist(x, bins='auto', label=fr'$t=1$',density=True)
        ax1.plot(x_func ,gaussian_vals(x_func,t))
        ax1.legend(loc='upper right', fontsize=12)
    if t == 10:
        ax2.hist(x, bins='auto', label=fr'$t=10$',density=True)
        ax2.plot(x_func ,gaussian_vals(x_func,t))
        ax2.legend(loc='upper right', fontsize=12)
    if t == 100:
        ax3.hist(x, bins='auto', label=fr'$t=100$',density=True)
        ax3.plot(x_func, gaussian_vals(x_func,t))
        ax3.legend(loc='upper right', fontsize=12)

# plt.xlim(-T,T)
# plt.ylim(-T,T)


plt.show()


# for i in range(N):
#     plt.plot(T_vec, x[:,i] ,label=f"Cząstka {i}")


# plt.show()

# print(x)



