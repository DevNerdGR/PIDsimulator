import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

"""-----Change the values here to modify simulation parameters-----"""
#Change this to true to output a .gif file of the animation
renderAnim = False

#General
sampleSize = 1000
totalTime = 20
timeScale = 1

#SP control
initialSP = 2
disturbedSP = 7
disturbTime = 1.5

#PV control
initialPos = 7

#PID control
kp = 0.085
ki = 0.0001
kd = 0.018
"""----------------------------------------------------------------"""

t = np.linspace(0, totalTime, sampleSize)

pv = np.linspace(0, 0, sampleSize + 1)
pv[0] = initialPos

"""---Uncomment any of the following lines to set the type of SP---"""
#Note: To change the properties of the SP (e.g. start value, etc.), change the values of the variables above!!
#Horiszontal straight line
#sp = np.linspace(initialSP, initialSP, sampleSize) 

#Linear line
#sp = np.linspace(initialSP, disturbedSP, sampleSize)

#Step disturbance
#sp = np.add(np.multiply(np.heaviside(np.subtract(np.linspace(0, totalTime, sampleSize), disturbTime), 1), disturbedSP - initialSP), initialSP)

#Sine wave disturbance
sp = np.add(np.sin(t), initialSP) 

#Very noisy SP
#sp = np.add(np.random.rand(sampleSize), initialSP) 
"""---------------------------------------------------------------"""


def proportionalControl(et):
    return kp * et

etSum = 0
def integralControl(et):
    global etSum
    etSum += et
    return ki * etSum

def derivativeControl(de, dt):
    return (kd * (de / dt) if dt != 0 else 0)

fig, axis = plt.subplots()

spGraph, = plt.plot([], [], color='b', label="Set Point")
pvGraph, = plt.plot([], [], color='r', label="Process Variable")

plt.legend()

def updateFrame(frame):
    spGraph.set_data(t[:frame], sp[:frame])

    et = sp[frame] - pv[frame]
    if frame != 0:
        de = et - (sp[frame - 1] - pv[frame - 1])
        dt = totalTime / sampleSize
    else:
        de, dt = 0, 0
    pv[frame + 1] = pv[frame] + proportionalControl(et) + integralControl(et) + derivativeControl(de, dt)
    pvGraph.set_data(t[:frame], pv[:frame])
    

anim = FuncAnimation(fig, updateFrame, sampleSize, interval=(((totalTime * 1000) / sampleSize) / timeScale))


plt.xlabel("Time")
plt.xticks(np.linspace(0, totalTime, totalTime + 1))
axis.set_xlim([0, totalTime])

axis.set_ylim([0, 10])

plt.grid()
plt.title(f"PID Simulator:\nKp = {kp}, Ki = {ki}, Kd = {kd}")
anim.save("PIDsimulator.gif") if renderAnim else None
plt.show()

