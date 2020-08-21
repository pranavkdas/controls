#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time

pub = None
command=0
sub_side=None

def callback(msg):
	n = len(msg.ranges)
	#distribute total region (half a circle) into 3 parts
	front = min(msg.ranges[n//3:2*n//3])
	go_front(front)
	#rospy.loginfo(ranges)

def go_front(value):
	msg = Twist()
	state_description = "pranav" #for personal info
	if(value>1.5):
		rospy.loginfo(state_description)
		msg.linear.x = 50
		pub.publish(msg)
		print("yo")
	else:
		msg.linear.x=0
		pub.publish(msg)

def clbk_laser(msg):
	global left
	n = len(msg.ranges)
	#distribute total region (half a circle) into 3 parts
	left= min(msg.ranges[n//3:2*n//3])
	take_action(left)


def take_action(value):
	msg = Twist()
	state_description = '' #for personal info
	if(value>1):
		rospy.loginfo(state_description)
		msg.linear.y = 8
		pub.publish(msg)
	else:
		msg.linear.y=0
		pub.publish(msg)
		command=1
		sub_side.unregister()
		



def main():
	global pub
	global sub_side
	global command
	rospy.init_node('all_together')
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	sub_side = rospy.Subscriber('/hexbot/laser_side/scan', LaserScan, clbk_laser)
	if command==1:
		sub_front = rospy.Subscriber('/hexbot/laser/scan', LaserScan, callback)
	

	rospy.spin()

if __name__ == '__main__':
	main()