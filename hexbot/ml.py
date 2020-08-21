#!/usr/bin/env python
import rospy
import cv2
import tensorflow as tf 
import numpy as np 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def callback(ros_image_message):
	bridge = CvBridge()
	img = bridge.imgmsg_to_cv2(ros_image_message, 
	desired_encoding='passthrough')

	h=48
	b=64
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img=cv2.resize(img,(b,h))
	img=img.reshape(h,b,1)
	PATH='/home/pranavkdas/model1a_9927.h5'

	cv2.imshow('frame',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def listener():
	rospy.init_node('ml',anonymous=True)
	rospy.Subscriber('/hexbot/camera1/image_raw',
		Image,callback)
	rospy.spin()

if __name__=='__main__':
	listener()






