import numpy as np
import matplotlib.pyplot as plt
import control as c


sys = c.TransferFunction([8], [59, 13, 12])
T, y_ir = c.impulse_response(sys)
T, y_sr = c.step_response(sys)
Impulse = np.zeros(T.shape);Impulse[0] = 1
Step = np.ones(T.shape)

plt.plot(T, y_ir, label = 'Impulse Response')
plt.plot(T, Impulse, label = 'Impulse')
plt.legend()
plt.grid()
plt.savefig('./figs/Impulse Response.jpg')
plt.close()
plt.plot(T, y_sr, label = 'Step Response')
plt.plot(T, Step, label = 'Step')
plt.legend()
plt.grid()
plt.savefig('./figs/Step Response.jpg')
