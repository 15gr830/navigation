#!/usr/bin/env python

from __future__ import print_function

import argparse

import rospy
import mavros
from mavros.utils import *
from mavros import command
from mavros.srv import SetMode


def arm(state):
    try:
        ret = command.arming(value=state)
    except rospy.ServiceException as ex:
        fault(ex)

    if not ret.success:
        fault("Request failed. Check mavros logs")

    return ret


def main():
	arm(True)
	

if __name__ == '__main__':
    main()
