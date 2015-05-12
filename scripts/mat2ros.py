#!/usr/bin/env python
import rospy, SocketServer, threading, struct
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped

class myThread1(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        rospy.loginfo("Starting " + self.name)
        get_got_data()
        rospy.loginfo("Exiting " + self.name)

class MatlabUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        socket = self.request[0]
        # print "%s wrote:" % self.client_address[0]
        numOfValues = len(data) / 8
        data = struct.unpack('>' + 'd' * numOfValues, data)

        now = rospy.get_rostime()
        got_pos = PoseWithCovarianceStamped()
        vicon_pos = PoseWithCovarianceStamped()
        #rospy.loginfo("Time %i", now.secs)
        got_pos.header.stamp.secs = now.secs
        got_pos.header.stamp.nsecs = now.nsecs
        got_pos.pose.pose.position.x = data[0]
        got_pos.pose.pose.position.y = data[1]
        got_pos.pose.pose.position.z = data[2]

        vicon_pos.header.stamp.secs = now.secs
        vicon_pos.header.stamp.nsecs = now.nsecs
        vicon_pos.pose.pose.position.x = data[3]
        vicon_pos.pose.pose.position.y = data[4]
        vicon_pos.pose.pose.position.z = data[5]

        pub_got.publish(got_pos)
        pub_vicon.publish(vicon_pos)


def talker():
    global pub_got
    #global pub_vicon
    pub_got = rospy.Publisher('/mavros/global_position/local', PoseWithCovarianceStamped, queue_size=10)
    #pub_vicon = rospy.Publisher('/vicon_data', PoseWithCovarianceStamped, queue_size=10)
    rospy.init_node('mat2ros', anonymous=False)

    #Start MatlabUDPHandler 
    get_got.start()

    while not rospy.is_shutdown():
        rospy.spin()
        

def get_got_data() :
    HOST, PORT = "0.0.0.0", 3232
    server = SocketServer.UDPServer((HOST, PORT), MatlabUDPHandler)
    server.serve_forever()

# Create new threads
get_got = myThread1(1, "GOT\n")
get_got.daemon = True

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
