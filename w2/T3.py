import numpy as np
import matplotlib.pyplot as plt

N = 100
T = 100

T_vec = np.linspace(0,T,T)
x = np.zeros(N)
x_0 = np.zeros(N)
def gaussian_vals(x,t):
    return 1/np.sqrt(2*np.pi*t)*np.exp(-x**2/(2*t))
    
def MSD(N,x,x_0):
    return 1/N*np.sum((x-x_0)**2)

MSD_vec = []
    

for t in range(T):
    delta = np.random.normal(loc=0, scale=1, size=(N))
    x += delta
    MSD_vec.append(MSD(N,x,x_0))

plt.figure(figsize=(8,5),dpi=150)
plt.plot(T_vec,MSD_vec,label="Dane")
plt.plot(T_vec,T_vec,label="Model")
plt.xlabel(r'$Time\ t$', fontsize=16)
plt.ylabel(r'$MSD$', fontsize=16)
plt.legend(loc='upper right', fontsize=12)
plt.show()


plt.show()


# for i in range(N):
#     plt.plot(T_vec, x[:,i] ,label=f"Cząstka {i}")


# plt.show()

# print(x)



