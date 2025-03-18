import numpy as np 
import matplotlib.pyplot as plt
from control import TransferFunction, feedback, step_response

m = 1.0 
c = 5.0
k = 2 

num = [1]
den = [m, c, k]
plant = TransferFunction(num, den)

kp = 10
ki = 1
kd = 1

pid = TransferFunction([kd, kp, ki],[1,0])

system = feedback(pid*plant, 1)

t = np.linspace(1,10,1000)

t,y = step_response(system, t)
plt.figure(figsize=(10,6))
plt.plot(t,y,label="Mass Position")
plt.title('Mass spring damper PID controller')
plt.xlabel('Time [s]')
plt.ylabel('Displacement [m]')
plt.legend()
plt.grid(True)
plt.show()
