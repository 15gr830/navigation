#!/bin/bash


while true
do
	ping -c 1 google.com

	if [[ $? == 0 ]];
		then
		echo ‘Network available.’
		break;
	else
		echo ‘Network is not available, waiting..’
		sleep 5
	fi
	done

# Initialise ROS and nodes
source /opt/ros/indigo/setup.bash
#source /home/odroid/ros/devel/setup.bash
export ROS_IP=$(hostname -I)
export ROS_MASTER_URI=http://$ROS_IP:11311

#roscore
roslaunch navigation nav.launch