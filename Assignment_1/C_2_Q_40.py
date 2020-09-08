from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as c

# ~ s = symbols('s')
# ~ t = symbols('t', positive = True)#, real = True)

# ~ TF = 8/(59*s**3 + 14*s**2 + 12*s)
# ~ n_data_points = 1000
# ~ x_min = 0
# ~ x_max = 100
# ~ Impulse = np.zeros(n_data_points);Impulse[0] = 1
# ~ Step = np.ones(n_data_points)
# ~ Ramp = np.linspace(x_min, x_max, n_data_points)
# ~ Transfer_function = lambdify(s, TF, "numpy")
# ~ o = inverse_laplace_transform(TF, s, t)
# ~ Response = lambdify(t, o, 'numpy')

# ~ data = np.linspace(x_min, x_max, n_data_points)
# ~ Output = Response(data)
# ~ #plt.plot(data, Transfer_function(data), label='Transfer Function')
# ~ plt.title('Impulse Response')
# ~ plt.plot(data, Output, label = 'Output')
# ~ #plt.plot(data, Impulse, label = 'Input')
# ~ plt.xlabel('Time')
# ~ plt.grid()
# ~ plt.legend()
# ~ plt.show()

# ~ sig = signal.lti([8], [59, 14, 12])
# ~ w, mag, phase = signal.bode(sig)

# ~ plt.semilogx(w, mag, label = 'Magnitude')
# ~ plt.grid()
# ~ plt.legend()
# ~ plt.show()


# ~ plt.semilogx(w, phase, label = 'Phase')
# ~ plt.grid()
# ~ plt.legend()
# ~ plt.show()

sys = c.TransferFunction([8], [59, 13, 12])
T, y_ir = c.impulse_response(sys)
T, y_sr = c.step_response(sys)
Impulse = np.zeros(T.shape);Impulse[0] = 1
Step = np.ones(T.shape)

plt.plot(T, y_ir, label = 'Impulse Response')
plt.plot(T, Impulse, label = 'Impulse')
plt.legend()
plt.grid()
plt.savefig('Impulse Response.jpg')

plt.plot(T, y_sr, label = 'Step Response')
plt.plot(T, Step, label = 'Step')
plt.legend()
plt.grid()
plt.savefig('Step Response.jpg')
