from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
# from scipy.optimize import fmin

a = 1
b = 1
c= 0.2
nu = 0.213
f = 0.2

def S(t,y):
    x, v = y
    dxdt= v
    dvdt = b*x-a*x**3-c*v+f*np.cos(2*np.pi*nu*t)
    return [dxdt, dvdt]

def V(y):
    x, v = y
    return b*x-a*x**3-c*v

# minimum = fmin(V,[0,0])

sol = solve_ivp(S, [0, 500], [0, 0], t_eval=np.linspace(0,500,5000))

fig, ((ax1), (ax2), (ax3)) = plt.subplots(1, 3)
fig.suptitle(f'Wykresy dla f={f}')

ax1.plot(sol.t, sol.y[0], )
ax2.plot(sol.t, sol.y[1])
ax3.plot(sol.y[0], sol.y[1])
ax1.set_xlabel('Time t')
ax2.set_xlabel('Time t')
ax3.set_xlabel('x(t)')

ax1.set_ylabel('x(t)')
ax2.set_ylabel('v(t)')
ax3.set_ylabel('v(t)')

ax3.plot(np.sqrt(b/a),0,'ro')

plt.show()