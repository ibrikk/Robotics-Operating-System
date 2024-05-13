#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg: Pose):
    rospy.loginfo("(" + str(msg.x) + ", " + str(msg.y) + ")")

if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")
    msg = Pose()
    # topic name, type of message, callback
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Node has been started")

    # Keeps your script spinning until the node has been shut down.
    # Allows callbacks to be called as long as the node is alive
    rospy.spin()


