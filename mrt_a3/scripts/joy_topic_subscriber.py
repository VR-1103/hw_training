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

    #logic in if statements
    #abc.publsih(data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/joy', Joy , callback)

    rospy.spin()

##def talker():
    ##rospy.init_node('talker' , anonymous=True)
    

if __name__ == '__main__':
    ##talker()
    listener()

'''if (axes[1] >= 0.1):
            driver1.FORWARDM1(axes[1]*100/0.9)
            driver2.FORWARDM2(axes[1]*100/0.9)
        elif (axes[1] <= -0.1):
            driver1.BACKWARDM1(axes[1]*100/0.9)
            driver2.BACKWARDM2(axes[1]*100/0.9)
        elif (axes[0] <= -0.1):
            driver1.BACKWARDM1(axes[0]*100/0.9)
            driver2.FORWARDM2(axes[0]*100/0.9)
        elif (axes[0] >= 0.1):
            driver1.FORWARDM1(axes[0]*100/0.9)
            driver2.BACKWARDM2(axes[0]*100/0.9)'''