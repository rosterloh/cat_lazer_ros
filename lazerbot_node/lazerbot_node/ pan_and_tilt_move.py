#!/usr/bin/env python3
import time
import math
from lazerbot_node.PCA9685 import PCA9685

class PanAndTiltMove(object):

    def __init__(self):
        self._pwm = PCA9685()

        self._PWM_FREQ = 50

        self._pwm.setPWMFreq(self._PWM_FREQ)

        self.PITCH_INIT_ANGLE = 0
        self.YAW_INIT_ANGLE = 0
        self.move_to_pitch_yaw(yaw=self.YAW_INIT_ANGLE,
                               pitch=self.PITCH_INIT_ANGLE)

    def __del__(self):
        self._pwm.exit_PCA9685()

    def move_to_pitch_yaw(self, yaw, pitch):
        self.move_yaw(yaw_angle=yaw)
        self.move_pitch(pitch_angle=pitch)

    def move_yaw(self, yaw_angle):
        self._pwm.setRotationAngle(0, yaw_angle)

    def move_pitch(self, pitch_angle):
        self._pwm.setRotationAngle(1, pitch_angle)

    def yaw_range_test(self):
        """
        It tests the range of yaw servo once
        :return:
        """
        for angle in range(10,170,1):
            print("Moving Yaw="+str(angle))
            self.move_yaw(yaw_angle=angle)
            time.sleep(0.1)

        for angle in range(170,10,-1):
            print("Moving Yaw="+str(angle))
            self.move_yaw(yaw_angle=angle)
            time.sleep(0.1)

    def pitch_range_test(self):
        """
        It tests the range of pitch servo once
        :return:
        """
        for angle in range(10,170,1):
            print("Moving Pitch="+str(angle))
            self.move_pitch(pitch_angle=angle)
            time.sleep(0.1)

        for angle in range(170,10,-1):
            print("Moving Pitch="+str(angle))
            self.move_pitch(pitch_angle=angle)
            time.sleep(0.1)

    def input_yaw_test(self):

        while True:
            input_x = raw_input("Type Angle to move to")
            angle = int(input_x)
            print("Moving Yaw=" + str(angle))
            self.move_yaw(yaw_angle=angle)

    def input_pitch_test(self):

        while True:
            input_x = raw_input("Type Angle to move to")
            angle = int(input_x)
            print("Moving Pitch=" + str(angle))
            self.move_pitch(pitch_angle=angle)

    def yaw_pitch_circle_test(self, repetitions=1):

        # These values are base on Hardware observations where they are stable.
        max_range = 100
        min_range = 30
        period = 0.1
        increments = 10

        for num in range(repetitions):
            for angle in range(0,359,increments):
                pitch_angle = int((((math.sin(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)
                yaw_angle = int((((math.cos(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)

                print("Moving Yaw="+str(yaw_angle))
                print("Moving Pitch=" + str(pitch_angle))

                self.move_pitch(pitch_angle)
                self.move_yaw(yaw_angle)
                time.sleep(period)

            for angle in range(0,359,-increments):
                pitch_angle = int((((math.sin(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)
                yaw_angle = int((((math.cos(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)

                print("Moving Yaw="+str(yaw_angle))
                print("Moving Pitch=" + str(pitch_angle))

                self.move_pitch(pitch_angle)
                self.move_yaw(yaw_angle)
                time.sleep(period)
