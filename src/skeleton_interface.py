#!/usr/bin/env python
################
# ROS IMPORTS: #
################
import roslib; roslib.load_manifest('trep_puppet_demo')
import rospy
import tf
from skeletonmsgs_nu.msg import Skeletons
from skeletonmsgs_nu.msg import Skeleton
from skeletonmsgs_nu.msg import SkeletonJoint


####################
# NON ROS IMPORTS: #
####################
import sys
import os
import math
import copy
from math import fmod, pi, copysign
import numpy as np


####################
# GLOBAL VARIABLES #
####################
SCALING = 1
# filter parameters:
FALPHA = 0.25
GAMMA = 0.05
A_LOW = 0.01
A_HIGH = 0.50
V_HIGH = 0.008
V_LOW = 0.001


class SingleController:
    """
    This class will be used for each individual input.  I need to provide
    methods for doing the following things:

    1) Storing the location of the "key" joint at a current time.... this will
    be used for providing the mapping between the person's joints and the puppet
    inputs.
    2) Update the filter
    3) Send out the frames associated with the controls
    4) Take in/ update the nominal location of the puppet's kinematic inputs so
    that I can (re)calibrate whenever I need to 
    """
    def __init__(self, joint, frame, pos):

        return


class SkeletonController:
    def __init__(self):

        # first with for the 
        
        
        







def main():
    rospy.init_node('skeleton_interface', log_level=rospy.INFO)

    rospy.set_param('legs', False)

    try:
        sim = SkeletonController()
    except rospy.ROSInterruptException: pass

    rospy.spin()


if __name__=='__main__':
    main()
