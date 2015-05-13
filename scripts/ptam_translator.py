#!/usr/bin/env python

import rospy
import from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped

def callback(data):
	ptam_pos = PoseStamped()
	ptam_pos.header = data.header
	ptam_pos.pose = data.pose.pose

	pub_ptam.publish(ptam_pos)

def get_ptam_data():
	global pub_ptam
	rospy.init_node('ptam_translator', anonymous=False)
	rospy.Subscriber("/vslam/pose",PoseWithCovarianceStamped, callback)
	pub_ptam = rospy.Publisher('/mavros/vision_pose/pose', PoseStamped, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	get_ptam_data()