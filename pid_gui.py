from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from control import TransferFunction, feedback, step_response


text_font = ("Sans Serif", 10, "bold")
m = 10
c = 10
k = 20

def get_values():
    global label
    kp = slider1.get()
    ki = slider2.get()
    kd = slider3.get()
    label.config(text=f"Kp = {kp}, Ki = {ki}, Kd = {kd}")

def pid():
    kp = slider1.get()
    ki = slider2.get()
    kd = slider3.get()

    # Define the transfer function of the plant
    num = [1]
    den = [m, c, k]
    plant = TransferFunction(num, den)

    # Define the PID controller transfer function
    pid = TransferFunction([kd, kp, ki], [1, 0])

    # Closed-loop system with unity feedback
    system = feedback(pid * plant, 1)

    # Time vector for the simulation
    t = np.linspace(0, 10, 1000)

    # Step response
    t, y = step_response(system, t)

    # Plotting the step response
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label="Mass Position")
    plt.title("PID Controller Response")
    plt.xlabel("Time [s]")
    plt.ylabel("Displacement [m]")
    plt.legend()
    plt.grid(True)
    plt.show()

root = Tk()
root.title("Mass Spring Damper PID Controller")
root.geometry("400x200")

# Slider for Kp
slider1 = Scale(root, from_=0, to_=500, orient=HORIZONTAL)
slider1.pack(anchor=CENTER)

# Slider for Ki
slider2 = Scale(root, from_=0, to_=500, orient=HORIZONTAL)
slider2.pack(anchor=CENTER)

# Slider for Kd
slider3 = Scale(root, from_=0, to_=500, orient=HORIZONTAL)
slider3.pack(anchor=CENTER)

# Label to display PID values
label = Label(root, text="", font=text_font)
label.pack(anchor=CENTER)

#Get input PID values 
button = Button(root, text="Confirm Gain Values", width=40, font=text_font, command=get_values)
button.pack(anchor=CENTER)

#Run controller
button_plot = Button(root, text="Run PID Controller", width=40, font=text_font, command=pid)
button_plot.pack(anchor=CENTER)

mass = Entry(root, font=text_font)
root.mainloop()
