#!/usr/bin/env python

from __future__ import print_function

import argparse

import rospy
import mavros
import sys, struct, time, os, select
import numpy as np
from mavros.utils import *
from mavros import command
from geometry_msgs.msg import PoseStamped

def arm(state):
    try:
        ret = command.arming(value=state)
    except rospy.ServiceException as ex:
        fault(ex)

    if not ret.success:
        fault("Request failed. Check mavros logs")

    return ret

def do_long(state):
    if state:
      start = 1
    else:
      start = -1

    try:
        ret = command.long(command=30002, confirmation=1,
                      param1=start,
                      param2=0,
                      param3=0,
                      param4=0,
                      param5=0,
                      param6=0)
    except rospy.ServiceException as ex:
        fault(ex)

def safety_area(pose):
    vicon_data = PoseStamped()



def odrone_interface():
    rospy.init_node('odrone_interface', anonymous=False)
    rospy.Subscriber('/vicon_data', PoseStamped, safety_area)

    
    try:
        while not rospy.is_shutdown():
            key = raw_input("\nODRONE >> ")
            
            if key == 'a' :
                arm(True)

            elif key == 'd' :
                arm(False)

            elif key == 'w' :
                do_long(True)

            elif key == 's' :
                do_long(False)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    try:
        odrone_interface()
    except rospy.ROSInterruptException, KeyboardInterrupt:
        pass

