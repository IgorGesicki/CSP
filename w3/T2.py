from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
# from scipy.optimize import fmin

a = 1
b = 1
c= 0.2
nu = 0.213
f = 0.382

def S(t,y):
    x, v = y
    dxdt= v
    dvdt = b*x-a*x**3-c*v+f*np.cos(2*np.pi*nu*t)
    return [dxdt, dvdt]

def V(y):
    x, v = y
    return b*x-a*x**3-c*v

# minimum = fmin(V,[0,0])

sol = solve_ivp(S, [0, 1000], [1.4, 0.15], t_eval=np.linspace(200,800,3000), method='RK45', rtol=1e-8, atol=1e-11)
sol2 = solve_ivp(S, [0, 1000], [1.4000000000001, 0.150000000001], t_eval=np.linspace(200,800,3000), method='RK45', rtol=1e-8, atol=1e-11)





plt.plot(sol.y[0], sol.y[1], 'b')
plt.plot(sol2.y[0], sol2.y[1], 'g')
plt.xlabel('x(t)')


plt.ylabel('v(t)')

plt.plot(np.sqrt(b/a),0,'ro')

plt.show()