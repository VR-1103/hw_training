#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import String


joyInfo = rospy.Publisher('/joy1' , String)
def callback(data):
    rospy.loginfo(str(data))
    if(data.axes[0] < -0.1):
        joyInfo.publish('RIGHT')
    elif(data.axes[0] > 0.1):
        joyInfo.publish('LEFT')
    elif(data.axes[1] < -0.1):
        joyInfo.publish('BACKWARD')
    elif(data.axes[1] > 0.1):
        joyInfo.publish('FORWARD')


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/joy', Joy , callback)

    rospy.spin()
    
if __name__ == '__main__':
    listener()
