#!/usr/bin/env python
import rospy, SocketServer, thread, threading, struct
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class Positions:
    def __init__(self, pub_got, pub_vicon, pub_ptam, rospy):
        self.pub_got = pub_got
        self.pub_vicon = pub_vicon
        self.pub_ptam = pub_ptam
        self.rospy = rospy
        
        self.HOST = "0.0.0.0"
        self.PORT = 3232

        try:
            thread.start_new_thread( self.get_data, () )
        except:
            print("Error: Unable to start thread")

        rospy.Subscriber("/vslam/pose",PoseWithCovarianceStamped, send_ptam, queue_size=10)

    def send_ptam(self, topic):
        ptam_pos = PoseStamped()
        ptam_pos.header = topic.header
        ptam_pos.pose = topic.pose.pose

        self.pub_ptam.publish(ptam_pos)


    def get_data(self) :
        server = SocketServer.UDPServer((self.HOST, self.PORT), MatlabUDPHandler(self.pub_got, self.pub_vicon, self.rospy))
        server.serve_forever()

class MatlabUDPHandler(SocketServer.BaseRequestHandler):
    def __init__(self, pub_got, pub_vicon, rospy):
        self.pub_got = pub_got
        self.pub_vicon = pub_vicon
        self.rospy = rospy

    def handle(self):
        data = self.request[0]
        socket = self.request[0]
        # print "%s wrote:" % self.client_address[0]
        numOfValues = len(data) / 8
        data = struct.unpack('>' + 'd' * numOfValues, data)

        now = rospy.get_rostime()
        got_pos = PoseStamped()
        vicon_pos = PoseStamped()
        #rospy.loginfo("Time %i", now.secs)
        got_pos.header.stamp.secs = now.secs
        got_pos.header.stamp.nsecs = now.nsecs
        got_pos.pose.position.x = data[0]
        got_pos.pose.position.y = data[1]
        got_pos.pose.position.z = data[2]

        vicon_pos.header.stamp.secs = now.secs
        vicon_pos.header.stamp.nsecs = now.nsecs
        vicon_pos.pose.position.x = data[3]
        vicon_pos.pose.position.y = data[4]
        vicon_pos.pose.position.z = data[5]
        vicon_pos.pose.orientation.x = data[6]
        vicon_pos.pose.orientation.y = data[7]
        vicon_pos.pose.orientation.z = data[8]
        vicon_pos.pose.orientation.w = data[9]

        self.pub_got.publish(got_pos)
        self.pub_vicon.publish(vicon_pos)


def init():
    pub_got = rospy.Publisher('/mavros/mocap/pose', PoseStamped, queue_size=10)
    pub_vicon = rospy.Publisher('/vicon_data', PoseStamped, queue_size=10)
    pub_ptam = rospy.Publisher('/mavros/vision_pose/pose', PoseStamped, queue_size=10)
    
    rospy.init_node('position_node', anonymous=False)

    Positions(pub_got,pub_vicon,pub_ptam,rospy)
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException:
        pass
