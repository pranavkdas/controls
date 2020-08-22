#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time

pub = None
command=0

def callback(msg):
	n = len(msg.ranges)
	#distribute total region (half a circle) into 3 parts
	front = min(msg.ranges[n//3:2*n//3])
	go_front(front)
	#rospy.loginfo(ranges)

def go_front(value):
	msg = Twist()
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	state_description = "pranav" #for personal info
	if(value>1.5):
		rospy.loginfo(state_description)
		msg.linear.x = 10
		pub.publish(msg)
		#print("yo")
	else:
		msg.linear.x=0
		pub.publish(msg)

def clbk(msg):
	rospy.loginfo(msg.data)
	#if(msg.data=="Go_forward"):
		
		



def main():
	global pub
	global command
	rospy.init_node('going_forward')
	
	#sub_command = rospy.Subscriber('/forward_command',String,clbk)
	sub = rospy.Subscriber('/hexbot/laser/scan', LaserScan, callback)
	#time.sleep(5)
	#if(command==1):
	
	rospy.spin()

if __name__ == '__main__':
	main()