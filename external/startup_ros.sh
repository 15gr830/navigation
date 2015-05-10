#!/bin/bash

source /opt/ros/indigo/setup.bash
source /home/odroid/ros/devel/setup.bash
export ROS_IP=$(hostname -I)
export ROS_MASTER_URI=http://$ROS_IP:11311

# Initialise ROS and nodes
roscore &
roslaunch navigation nav.launch &

exit 0