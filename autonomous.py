#!/usr/bin/env python

from roboclaw import RoboClaw
import rospy

#---------------------------------------------------- 

class Drive:
    def __init__(self,driver1,driver2):
        self.rightClaw = driver1
        self.leftClaw = driver2
         

    def drive_callback(self,inp):
        # A bit of help! These are arrays of data
        axes = inp.axes
        buttons = inp.buttons
        '''Trying to edit in github vs'''

        """TODO - INSERT YOUR CODE HERE
        
        Problem Statement: Insert Code here to make the rover move 
        forwards, Backwards, left, right according to input given
        """
        if (axes[1] >= 0.1):
            driver1.ForwardM1(axes[1]*100/0.9)
            driver1.ForwardM2(axes[1]*100/0.9)
            driver2.ForwardM1(axes[1]*100/0.9)
            driver2.ForwardM2(axes[1]*100/0.9)
        elif (axes[1] <= -0.1):
            driver1.BackwardM1(axes[1]*100/0.9)
            driver1.BackwardM2(axes[1]*100/0.9)
            driver2.BackwardM1(axes[1]*100/0.9)
            driver2.BackwardM2(axes[1]*100/0.9)
        elif (axes[0] <= -0.1):
            driver1.TurnRightMixed(axes[0]*100/0.9)
            driver2.TurnRightMixed(axes[0]*100/0.9)
        elif (axes[0] >= 0.1):
            driver1.TurnLeftMixed(axes[0]*100/0.9)
            driver2.TurnLeftMixed(axes[0]*100/0.9)
        

    def current_limiter(self):
        """BONUS: 

        Try to implement this function as well. It is a saftey feature. 
        How would you decide the current threshold? - Please elaborate
        """
        if (driver1.GETCURRENTS < 4A) && (driver2.GETCURRENTS < 4A):
            return False
        else:
            return True
                

#---------------------------------------------------                



