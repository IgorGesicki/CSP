from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def f(t, y):
    x, v = y
    dxdt = v
    dvdt = -x
    return [dxdt, dvdt]


sol = solve_ivp(f, [0, 10], [1, 0], t_eval=np.linspace(0,10,500))
# plt.plot(sol.t, sol.y[0])
plt.plot(sol.y[0], sol.y[1])
plt.show()
