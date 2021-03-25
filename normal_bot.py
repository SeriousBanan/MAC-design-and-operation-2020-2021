#!/usr/bin/env python3

#Скрипт мониторинга

#Использование:
#python3 <path>/normal_bot.py <ID робота>

import rospy
import sys
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

rospy.init_node(f"laser_checker_{str(sys.argv[1])}")
pub = rospy.Publisher(f"/lidar_check_{str(sys.argv[1])}", String, queue_size=10)

def laser_callback(data):
    min_range = 30
    for _range in data.ranges[300:420]:
        if _range < min_range:
            min_range = _range

    if min_range < 5:
        pub.publish("1")
    else:
        pub.publish("0")


rospy.Subscriber(f"/bot_{str(sys.argv[1])}/laser/scan", LaserScan, laser_callback)

while not rospy.is_shutdown():
    pass