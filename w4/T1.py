import numpy as np
from collections import deque
import matplotlib.pyplot as plt

p=0.62
L = 50
lattice = np.ones((L+2, L+2), dtype=int)*(-1)
lattice[0, :] = 0 # top wall
lattice[-1, :] =-2 # bottom wall
lattice[:, 0] = 0 # left wall
lattice[:, -1] = 0 # right wall
lattice[1, 1:-1] = 1 # top row: liquid reservoir


   
tossing = np.random.rand(L+2, L+2) < p   

cluster = deque()


def neighbours(i):
    return [(i[0],i[1]+1),(i[0]+1,i[1]),(i[0]-1,i[1]), (i[0],i[1]-1)]


for y in range(1, L+1):
    cluster.append((1, y))



while cluster:
    i = cluster.pop()
    nei = neighbours(i)

    if i[0] == L:
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
            print("bottom hit")
            break
        
        
        
        

plt.imshow(lattice[1:-1, 1:-1], interpolation='nearest', cmap='magma')
plt.savefig(f"Tastk_1_{p}.png", format='png')
# print(lattice)
# def check(p):
#     x, y = p
#     if lattice[x+1,y] == -1:


# def growth(x):
    