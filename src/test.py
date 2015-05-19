#!/usr/bin/env python
import rospy, SocketServer, thread, threading, struct
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class Alpha:
        """test"""
        def __init__(self, en,to):
                self.en = en
                self.to = to

                try:
                        thread.start_new_thread( self.dav, () )
                except:
                        print("Error: Unable to start thread")
        def dav(self):
                print("Hej")
                hej = Beta(1).hejsa()


class Beta(object):
        """test"""
        def __init__(self, arg2):
                self.arg2 = arg2
                common = Alpha()

        def hejsa(self):
                while True:
                        print("derudad")
                        rospy.sleep(3)


def init():
    pub_got = rospy.Publisher('/mavros/mocap/pose', PoseStamped, queue_size=1)
    pub_vicon = rospy.Publisher('/vicon_data', PoseStamped, queue_size=1)
    rospy.init_node('mat2ros', anonymous=False)

    # Create new threads
    # get_got = Thread1(1, "GOT\n")
    # get_got.daemon = True
    # get_got.start()
    Alpha(1,2)

    rospy.spin()

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException:
        pass
                
