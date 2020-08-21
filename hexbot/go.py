#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

pub = None

def callback(msg):
	if msg.data=="stop":
		state_description = 'pkd'
		rospy.loginfo(state_description)
		v =Twist()
		v.linear.y=0
		pub.publish(v)
	if msg.data=="go":
		v = Twist()
		state_description = 'pkd' #for personal info
		rospy.loginfo(state_description)
		v.linear.y = -0.5
		pub.publish(v)


def main():
	global pub
	rospy.init_node('a',anonymous=True)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	sub = rospy.Subscriber('/stop',String, callback)
	

	rospy.spin()

if __name__ == '__main__':
	main()