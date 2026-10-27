from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


a = 1
b = 1
c= 0.07
nu = 0.213

f_val= np.linspace(0.15,0.4,100)
F=[]
X=[]

n = 10
delay = 500




for f in f_val:
    print(f)
    def S(t,y):
        x, v = y
        dxdt= v
        dvdt = b*x-a*x**3-c*v+f*np.cos(2*np.pi*nu*t)
        return [dxdt, dvdt]
    
    sol = solve_ivp(S, [0, (delay+n-1)/nu], [1.4, 0.15], t_eval=(np.arange(delay,delay+n)/nu), method='DOP853', rtol=1e-8, atol=1e-11)
    F.extend([f]*len(sol.t))
    X.extend(sol.y[0])
    
plt.scatter(F, X, s=3, c='g', lw=0, marker='o')  
plt.xlabel('f')
plt.ylabel('x_n')

plt.show()