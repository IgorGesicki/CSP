import numpy as np
import matplotlib.pyplot as plt
import random

r= 1/2
k=1
Jx = J = 1
Jy = r*J
Tc = 1.64102

n_therm = 2000
n_meas = 5000


def neighbours(i,L):
    return [(i[0] % L,(i[1]+1) % L),((i[0]+1) % L,i[1] % L),((i[0]-1) % L,i[1] % L), (i[0] % L,(i[1]-1) % L)]

def h(i, jx, jy, lat):
    nei = neighbours(i, L)
    return jx*(lat[nei[1]]+lat[nei[2]])+jy*(lat[nei[0]]+lat[nei[3]])

def sweepHB(lat, b, jx, jy, L):
    for k in range(L*L):
        i = ((np.random.randint(0,high=L)), (np.random.randint(0,high=L)))
        hi = h(i, jx, jy,lat)
        u = random.uniform(0, 1)
        if u < 1/(1+np.exp(-2*b*hi)):
            lat[i]= 1
        else:
            lat[i]= -1
    return None
            
def chi(T,L):
    Beta = 1/T
    lattice = np.ones((L, L), dtype=np.int8)
    magnetization = []
    
    for k in range(n_therm):
        sweepHB(lattice, Beta, Jx, Jy, L)
    for k in range(n_meas):
        sweepHB(lattice, Beta, Jx, Jy, L)
        magnetization.append(np.mean(lattice))
    return Beta * L**2 * np.var(magnetization)


for L in [10, 20]:
    y_chi = []
    T = np.arange(1,3,0.1)
    for t in T:
        y_chi.append(chi(t,L))
        print(f'working{t},{L}')
    plt.plot(T, y_chi, label=f"L= {L}")
    



T = np.arange(1,3,0.1)   
plt.vlines(Tc,0,1,label='model')

plt.show()