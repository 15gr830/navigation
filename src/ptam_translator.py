#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
# from sensor_msgs.msg import Imu

def write_to_pixhawk(data):
	ptam_pos = PoseStamped()
	ptam_pos.header = data.header
	ptam_pos.pose = data.pose.pose

	pub_ptam.publish(ptam_pos)

# def tf_imu_data(data):
# 	imu_data = Imu()
# 	imu_data = data
# 	pub_imu.publish(imu_data)

def get_ptam_data():
	global pub_ptam 
	# global pub_imu
	rospy.init_node('ptam_translator', anonymous=False)
	rospy.Subscriber("/vslam/pose",PoseWithCovarianceStamped, write_to_pixhawk)
	# rospy.Subscriber("/mavros/imu/data", Imu, tf_imu_data)
	pub_ptam = rospy.Publisher('/mavros/vision_pose/pose', PoseStamped, queue_size=10)
	# pub_imu = rospy.Publisher('/vslam/imu', Imu, queue_size=10)

	rospy.spin()

if __name__ == '__main__':
	get_ptam_data()