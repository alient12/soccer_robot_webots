# soccer_robot_webots
Controlling a soccer robot using python in Webots simulation environment for digital control course project

<h1 align="center">Control Digital Lab</h1>

**Professor**: Dr.Ali Talebi
, **Teaching Asistant**: AmirAli Setayeshi

**Team members:**
* Ali Entezari
* Pouya Ibrahimi
* Sevil Xojasteh
* Ali Qolami

<h1 align="center">Exercise</h1>
## Goals
1. Controlling robot in 1 dimention using P and PI controllers
1. Controlling robot angle usign P and PI controller
1. Moving robot to the targeted coordination in 2 dimentions using P and PI controllers
1. Moving robot to the ball

## Robot physic
We use ***v*** and ***ω*** to design controllers but in reality we have to control robot with left and right motor. So we use these transforms:
```python
vr = (2*v + w*L)/(2*R)
vl = (2*v - w*L)/(2*R)
```
And there is a dead zone for real motors that we cannot get lower speed than a specific speed.

![deadzone](https://user-images.githubusercontent.com/73688480/176275301-b74b5ea7-67c3-420d-9e61-61b63bce8a50.jpg)

So we simulated it the soft way.
```python
if abs(vr) > offset:
    self.right_motor.setVelocity(vr)
else:
    self.right_motor.setVelocity(0)
if abs(vl) > offset:
    self.left_motor.setVelocity(vl)
else:
    self.left_motor.setVelocity(0)
```
for ease of use we wrote a function to do all these

```python
def set_v_w(v, w):
    L, R = 0.02, 0.085
    offset = 0.5
    vr = (2*v + w*L)/(2*R)
    vl = (2*v - w*L)/(2*R)

    if abs(vr) > offset:
        self.right_motor.setVelocity(vr)
    else:
        self.right_motor.setVelocity(0)
    if abs(vl) > offset:
        self.left_motor.setVelocity(vl)
    else:
        self.left_motor.setVelocity(0)
```
## Webots
The credit of soccer robot simulation is belongs to [Adman](https://github.com/Adman) from this [repo](https://github.com/RoboCupJuniorTC/rcj-soccersim)

The only difference is robot controllers.

To get the robot coordination there was a python dictionary variable named `ball_data` that has to keys named `strength` and `direction`. `strength` is the IR sensor output. it's reverse of distance. `direction` was an array with unknown normalized data between -1 and 1. with multiple test understood they probably are sine and cosine of the angle between robot and ball.

![direction](https://user-images.githubusercontent.com/73688480/176278617-12e9b9ad-635a-4804-9b9c-f599d2af70fa.PNG)

![angle](https://user-images.githubusercontent.com/73688480/176278635-87ebfc9b-1c23-4ea3-be1d-de0f2fcd465d.png)

<h1 align="center">Lab</h1>
<h1 align="center">Project</h1>
