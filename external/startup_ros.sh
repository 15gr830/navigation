#!/bin/bash

### BEGIN INIT INFO
# Provides:          Startup ROS
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

source /opt/ros/indigo/setup.bash
source /home/odroid/ros/devel/setup.bash
export ROS_IP=$(hostname -I)
export ROS_MASTER_URI=http://$ROS_IP:11311
#export ROS_MASTER_URI=http://$ROS_IP:11311

# Initialise ROS and nodes
roscore &
roslauch navigation nav.launch &

exit 0