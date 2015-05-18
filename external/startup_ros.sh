#!/bin/bash

# Paste to crontab
# @reboot until [ -d /home/odroid ]; do sleep 1; done; /usr/bin/startup_ros.sh

while true
do
	ping -c 1 192.168.1.149

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
#source /opt/ros/indigo/setup.bash
#source /home/odroid/ros/devel/setup.bash
#export ROS_IP=$(hostname -I)
#export ROS_MASTER_URI=http://$ROS_IP:11311
source /home/odroid/.bashrc

roscore &
#roslaunch navigation nav.launch