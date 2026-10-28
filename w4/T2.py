import numpy as np
from collections import deque
import matplotlib.pyplot as plt

N=100 #liczba testow




p=np.arange(0.4,0.7,0.01)
L = [20,50,100]



def neighbours(i):
    return [(i[0],i[1]+1),(i[0]+1,i[1]),(i[0]-1,i[1]), (i[0],i[1]-1)]

plt.figure(figsize=(8,5),dpi=150)

for len in L:
    vals = []
    for prob in p:
        T = 0
        for k in range(0,N):
            
            lattice = np.ones((len+2, len+2), dtype=int)*(-1)
            lattice[0, :] = 0 # top wall
            lattice[-1, :] =-2 # bottom wall
            lattice[:, 0] = 0 # left wall
            lattice[:, -1] = 0 # right wall
            lattice[1, 1:-1] = 1 # top row: liquid reservoir


            cluster = deque()
                
            for y in range(1, len+1):
                cluster.append((1, y))
            
            tossing = np.random.rand(len+2, len+2) < prob   


            while cluster:
                i = cluster.pop()
                nei = neighbours(i)
                if i[0] == len:
                    T += 1
                    break
                for j in nei:
                    if lattice[j] == -1:
                        if tossing[j] == True:
                            lattice[j] = 1
                            cluster.append(j)
                        if tossing[j] == False:
                            lattice[j] = 0
                    if lattice[j] == 0:
                        continue
                    if lattice[j] == -2:
                        T += 1
                        break
        vals.append(T/N)
    plt.plot(p,vals, lw = 2, label=f'{len}')   
  




# plt.imshow(lattice[1:-1, 1:-1], interpolation='nearest', cmap='magma')
plt.legend()
plt.savefig(f"Task_2.png", format='png')



# print(lattice)
# def check(p):
#     x, y = p
#     if lattice[x+1,y] == -1:


# def growth(x):
    