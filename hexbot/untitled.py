#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time

class Part():
	def __init__(self, pub):
		self.pub = pub

	def callback_left_laser(self,val):
		left = min(val.ranges[355:365])
		msg = Twist()
		state_description = 'going_left' #for personal info
		print("left",left)
		if(left>1):
			
			rospy.loginfo(state_description)
			msg.linear.y = 8
			self.pub.publish(msg)
		else:
			msg.linear.y=0
			self.pub.publish(msg)
			






def main():
	rospy.init_node('main2')
	velocity_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	a = Part(velocity_pub)
	sub_laser_left = rospy.Subscriber('/hexbot/laser_side/scan', LaserScan, a.callback_left_laser)
	rospy.spin()

if __name__ == '__main__':
	main()