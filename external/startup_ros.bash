#! /bin/bash

### BEGIN INIT INFO
# Provides:          ROS application instance
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts instance of ROS
# Description:       starts instance of ROS using start-stop-daemon
### END INIT INFO

# Paste to crontab
# @reboot until [ -d /home/odroid ]; do sleep 1; done; /usr/bin/startup_ros.sh

case "$1" in
        start )
                while true
                do
                        ping -c 1 192.168.1.149

                        if [[ $? == 0 ]];
                                then
                                echo ‘Network available.’
                                break;
                        else
                                echo ‘Network is not available, waiting..’
                                sleep 3 
                        fi
                done

                # Initialise ROS and nodes
                source /opt/ros/indigo/setup.bash
                source /home/odroid/ros/devel/setup.bash
                export ROS_IP=$(hostname -I)
                export ROS_MASTER_URI=http://$ROS_IP:11311

                roscore &
                until rostopic list ; do sleep 1; done
                roslaunch navigation nav_mav.launch &
                ;;

        stop )
                source /opt/ros/indigo/setup.bash
                rosnode kill -a
                killall roscore
                ;;
esac
exit 0
