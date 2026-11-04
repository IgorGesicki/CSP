import numpy as np
import matplotlib.pyplot as plt
import random

r= 1/2
k=1
Jx = J = 1
Jy = r*J
L = 5

n_therm = 1000
n_meas = 5000


def neighbours(i):
    return [(i[0] % L,(i[1]+1) % L),((i[0]+1) % L,i[1] % L),((i[0]-1) % L,i[1] % L), (i[0] % L,(i[1]-1) % L)]

def h(i, jx, jy, lat):
    nei = neighbours(i)
    return jx*(lat[nei[1]]+lat[nei[2]])+jy*(lat[nei[0]]+lat[nei[3]])

def sweepHB(lat, b, jx, jy):
    for k in range(L*L):
        i = ((np.random.randint(0,high=L)), (np.random.randint(0,high=L)))
        hi = h(i, jx, jy,lat)
        u = random.uniform(0, 1)
        if u < 1/(1+np.exp(-2*b*hi)):
            lat[i]= 1
        else:
            lat[i]= -1
    return None
            
def main(T):
    Beta = 1/T
    lattice = np.ones((L, L), dtype=np.int8)
    magnetization = []
    
    for k in range(n_therm):
        sweepHB(lattice, Beta, Jx, Jy)
    for k in range(n_meas):
        sweepHB(lattice, Beta, Jx, Jy)
        magnetization.append(np.mean(lattice))
    return np.mean(np.abs(magnetization))
        
for T in np.arange(1,6):

    print(f"For T={T}, <|m|> is: {main(T)}")