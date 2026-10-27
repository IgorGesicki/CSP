from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


a = 1
b = 1
c= 0.07
nu = 0.213
f = 0.3
n = 5000

def S(t,y):
    x, v = y
    dxdt= v
    dvdt = b*x-a*x**3-c*v+f*np.cos(2*np.pi*nu*t)
    return [dxdt, dvdt]

def V(y):
    x, v = y
    return b*x-a*x**3-c*v

# minimum = fmin(V,[0,0])

sol = solve_ivp(S, [200/nu, (200+n-1)/nu], [1.4, 0.15], t_eval=np.linspace(200/nu,(200+n-1)/nu,n), method='RK45', rtol=1e-8, atol=1e-11) # better to use np.arange(200, 200+n)/mu

plt.scatter(sol.y[0], sol.y[1], s=3, c='g', lw=0, marker='o')
plt.xlabel('x(t)')


plt.ylabel('v(t)')

plt.show()