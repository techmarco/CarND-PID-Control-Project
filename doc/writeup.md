#**PID Controller**

#### Reflection

##### Describe the effect each of the P, I, D components had in your implementation.
The impact of the proportional **P** component was a steering correction inversely proportional to the measured cross track error.

The impact of the derivative **D** component was a steering correction opposing the rate of change of the measured cross track error.

The impact of the integral **I** component was a steering correction opposing the accumulated cross track error.

The effects of the various components on the total accumulated cross track error are shown in the figure presented below.
#![PID Controller Error][image1]{width=40%}

##### Describe how the final hyper parameters were chosen.
The final PID parameters selected empirically by observing the resulting driving behavior of the vehicle on the simulated track. The final PID parameters are tabulated below.

| P | I | D  |
| :-----: | :-----: | :-----: |
| 0.09 | 0.003 | 0.9 | 

The tuning procedure begun with the tuning of the **P**  parameter to generate steering oscillations in response to the cross track error as shown in blue in the graph above. This resulted in rapid oscillations that resulted in unsafe vehicle operation leading it off the simulated track.

To combat the oscillations of the **P** parameter, the **D** parameter was tuned to reduce the steering oscillations and improve linearity of the cross track error as shown in green in the graph above. This resulted in smoother driving behavior capable of navigating the simulated track.

Finally, to reduce the accumulated cross track error, the **I** parameter was tuned such that accumulated cross track error trends towards zero as shown in red in the graph above. With the tuned PID controller the car was able to safely navigate multiple laps around the simulated track.

[//]: # (Image References)

[image1]: /home/marco/github/CarND-PID-Control-Project/doc/pid_error_plot.png "PID Controller Error"
