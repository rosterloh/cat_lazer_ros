#!/usr/bin/env python3
from rclpy.node import Node
from rclpy.qos import QoSProfile

from lazerbot_msgs.msg import Lazer, PanAndTilt

from lazerbot_node.lazer_control import LazerControl
from lazerbot_node.pan_and_tilt_move import PanAndTiltMove

class LazerbotPositionControl(Node):

    def __init__(self):
        super().__init__('lazerbot_position_control')

        self._pan_and_tilt_move_object = PanAndTiltMove()

        qos = QoSProfile(depth=10)

        self.lazer = LazerControl()

        self.lazer_sub = self.create_subscription(
            Lazer,
            'lazer',
            self.lazer_callback,
            qos)

        self.pan_and_tilt_sub = self.create_subscription(
            PanAndTilt,
            'pan_and_tilt',
            self.pan_and_tilt_callback,
            qos)

        self.get_logger().info("Lazerbot position control node has been initialised.")

    def lazer_callback(self, msg):
        if msg.on:
            self.lazer.on()
        else:
            self.lazer.off()
        
    def pan_and_tilt_callback(self, msg):
        self.get_logger().debug("Received PandAndTilt New msg: " + str(msg))
        self._pan_and_tilt_move_object.move_to_pitch_yaw(yaw=msg.pan, pitch=msg.tilt)