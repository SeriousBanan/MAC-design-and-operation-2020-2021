#!/usr/bin/env python3

from random import randint
import rospy
from geometry_msgs.msg import Point


def talker():
    pub = rospy.Publisher('/lab2_master', Point, queue_size=10)
    rospy.init_node('lab2_master_node', anonymous=True)
    rate = rospy.Rate(10)

    point = Point(
        x=randint(-10, 10),
        y=randint(-10, -10),
        z=0)

    while not rospy.is_shutdown():
        pub.publish(point)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
