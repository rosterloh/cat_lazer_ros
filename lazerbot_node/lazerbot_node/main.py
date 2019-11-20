#!/usr/bin/env python3
import rclpy

from lazerbot_node.lazerbot_position_control import LazerbotPositionControl


def main(args=None):
    rclpy.init(args=args)
    lazerbot_position_control = LazerbotPositionControl()
    rclpy.spin(lazerbot_position_control)

    lazerbot_position_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()