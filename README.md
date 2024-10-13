# PID Simulator
## About
PID Simulator is a simple python script that is able to simulate the behaviour of PID controllers based on various parameters that the user can modify.
<br/><br/>
**Sample output with the setpoint being a simple sine wave:**
<br/>
![](https://github.com/DevNerdGR/PIDsimulator/blob/main/SineWavePID.gif)

## Features
- Animated behaviour of controller using Matplotlib
- Exporting of animation as a .gif file
- Tweakable Kp, Ki, Kd values
- Tweakable disturbance parameters

## User guide
### Installation
1. Clone this repository
2. Install the following dependencies (if not already installed): matplotlib, numpy
### Usage
1. Open main.py in your preferred code editor
2. Change the values of the variables accordingly
3. Run the script and observe the output!

## Theory
This program simulates the behaviour of a **Proportional, Integral, Derivative Controller**, an instrument that is used to control behaviours of systems in many applications. In many cases, not all three components of the controller need to be used.
<br/>
PID controllers are essentially a function that take in the set point (i.e. desired value) and process variable (i.e. the current value) as inputs and provide the correction required as an output. PID controllers have a wide range of uses, from various industrial systems (e.g. in chemical plants) to missile guidance systems.
<br/>

**Proportional**: The proportional component of the PID serves to provide a correction that is scaled based on how great the difference between the set point and process variable is. (Note: the difference between the set point and process variable is also known as the error term, e(t)).
<br/>

**Integral**: The integral component serves to 'keep track' of the history of the errors by summing up all the errors, hence providing correction for errors that have built up over time. This is done by taking the integral of the error term with respect to time.
<br/>

**Derivative**: The derivative component serves to provide corrections based on the rate of change of the error term, hence in some way 'predicting' how the set point will change in the future. This is done by taking the derivative of the error term with respect to time.
