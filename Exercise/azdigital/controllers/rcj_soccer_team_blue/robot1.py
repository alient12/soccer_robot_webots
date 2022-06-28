# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
import math  # noqa: F401

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

import time
import math


I = 0
I_v = 0
I_w = 0

class MyRobot1(RCJSoccerRobot):

    def run(self):
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841

                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                else:
                    # If the robot does not see the ball, stop motors
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841

                # Get GPS coordinates of the robot
                robot_pos = self.get_gps_coordinates()  # noqa: F841

                # Get data from sonars
                sonar_values = self.get_sonar_values()  # noqa: F841

                # self.left_motor.setVelocity(10)
                # self.right_motor.setVelocity(10)
                def set_v_w(v, w):
                    L, R = 0.02, 0.085
                    offset = 0
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

                # ########################### location 1:P ###########################
                # e_x = robot_pos[1] - (-0.8)
                # print(e_x)
                # k_p = 2.69
                # v = k_p * e_x
                # w = 0
                # set_v_w(v, w)
                # ###############################################################
                ########################### angle 2:P ###########################
                # e_phi = -heading
                # print(e_phi, heading)
                # k_p = 10
                # w = -k_p * e_phi
                # v = 0
                # set_v_w(v, w)
                ###############################################################
                ########################### location 1:PI ###########################
                # t0 = time.time()
                # global I
                # T = 1.3e-6
                # e_x = (0.55) - robot_pos[1]
                # print(e_x)
                # k_p = 2.69
                # K_I = 3000
                # I = T * K_I * e_x + I
                # v = -k_p * e_x - I
                # w = 0
                # set_v_w(v, w)
                # t1 = time.time()
                # delta_t = t1 - t0 
                # if delta_t < T:
                #     time.sleep(T - delta_t)

                ################################################################
                ########################### coordination 3:P & PI ###########################
                # t0 = time.time()
                # global I, I_v, I_w
                # T = 1.3e-6
                
                # x_d = -0.50
                # y_d = 0

                # e_x = x_d - robot_pos[1]
                # e_y = y_d - robot_pos[0]
                # e_r = (e_x**2+e_y**2)**0.5

                # phi_d = math.atan2(e_y, e_x)
                # if phi_d < 0:
                #     phi_d =  -phi_d - math.pi
                # else:
                #     phi_d = -phi_d + math.pi
                # phi = heading
                # e_phi = phi_d - phi
                
                # # print("phi_d:", phi_d*180/math.pi, "phi:", phi*180/math.pi, "e_x:", e_x, "e_y:", e_y, "e_r:", e_r, "e_phi:", e_phi*180/math.pi)
                # # print("Location:", robot_pos[1], robot_pos[0])

                # k_p_v = 2
                # K_I_v = 5
                # k_p_w = 5
                # K_I_w = 10

                # if abs(e_r) < 0.2:
                #     # PI
                #     I_v = T * K_I_v * e_r + I_v
                #     v = k_p_v * e_r - I_v

                #     # P
                #     # v = -k_p_v * e_r

                #     # Nothing
                #     # v = 0
                # else:
                #     v = 0.5
                
                # if abs(e_phi) > math.pi * 69 / 180 and abs(e_r) > 0.5:
                #     v = 0.01
                #     k_p_w = 7.5
                
                # elif abs(e_phi) > math.pi * 69 / 180 and abs(e_r) < 0.2:
                #     v = 0.01
                #     k_p_w = 1
                #     K_I_w = 15
                
                # # PI
                # I_w = T * K_I_w * e_phi + I_w
                # w = -k_p_w * e_phi - I_w

                # # P
                # # w = -k_p_w * e_phi
                
                # set_v_w(v, w)
                # t1 = time.time()
                # delta_t = t1 - t0 
                # if delta_t < T:
                #     time.sleep(T - delta_t)

                ################################################################
                ########################### ball 4:P & PI ###########################
                t0 = time.time()
                global I, I_v, I_w
                T = 1.3e-6

                e_r = 1 / ball_data["strength"] * 55 / 35
                
                cos_phi = ball_data["direction"][0]
                sin_phi = ball_data["direction"][1]
                e_phi = math.atan2(sin_phi, cos_phi)

                k_p_v = 2
                K_I_v = 5
                k_p_w = 5
                K_I_w = 10

                if abs(e_r) < 0.01:
                    # PI
                    # I_v = T * K_I_v * e_r + I_v
                    # v = k_p_v * e_r - I_v

                    # P
                    # v = -k_p_v * e_r

                    # Nothing
                    v = 0
                else:
                    v = 0.5
                
                if abs(e_phi) > math.pi * 69 / 180 and abs(e_r) > 0.5:
                    v = 0.01
                    k_p_w = 7.5
                
                elif abs(e_phi) > math.pi * 69 / 180 and abs(e_r) < 0.01:
                    v = 0.01
                    k_p_w = 1
                    K_I_w = 15
                
                # PI
                I_w = T * K_I_w * e_phi + I_w
                w = -k_p_w * e_phi - I_w

                # P
                # w = -k_p_w * e_phi
                
                
                set_v_w(v, w)
                t1 = time.time()
                delta_t = t1 - t0 
                if delta_t < T:
                    time.sleep(T - delta_t)

                ################################################################
                
                

                '''# Compute the speed for motors
                direction = utils.get_direction(ball_data["direction"])

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = 7
                    right_speed = 7
                else:
                    left_speed = direction * 4
                    right_speed = direction * -4

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)

                # Send message to team robots
                self.send_data_to_team(self.player_id)'''
