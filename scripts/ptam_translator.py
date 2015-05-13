#!/usr/bin/env python

import rospy
import from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped

def callback(data):
	pos = PoseStamped()

def get_ptam_data():
	rospy.init_node('ptam_translator', anonymous=False)
	rospy.Subscriber("/vslam/pose",PoseWithCovarianceStamped, callback)
	pub = rospy.Publisher('/mavros/vision')

	rospy.spin()

if __name__ == '__main__':
	get_ptam_data()