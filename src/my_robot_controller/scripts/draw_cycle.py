#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
if __name__ == '__main__':
    rospy.init_node("draw_cycle")

    rospy.loginfo("Node has been started")

    # topic name, type of message, queue size
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        # publish cmd vel
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        # publishing messages
        pub.publish(msg)
        rate.sleep()

