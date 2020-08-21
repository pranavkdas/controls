#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String

pub = None
n=None

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
		command = "Not_yet"
		rospy.loginfo(command)
		n.publish(command)
	else:
		msg.linear.y=0
		pub.publish(msg)
		command = "Go_forward"
		#x=10
		#while(x>0):
		rospy.loginfo(command)
		n.publish(command)
		#x=x-1
		#rospy.signal_shutdown("quitting")
	


def main():
	global pub
	global n
	rospy.init_node('reading_laser')
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	sub = rospy.Subscriber('/hexbot/laser_side/scan', LaserScan, clbk_laser)
	n= rospy.Publisher('/forward_command',String,queue_size=10)
	

	rospy.spin()

if __name__ == '__main__':
	main()