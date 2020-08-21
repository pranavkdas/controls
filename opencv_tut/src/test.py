#!/usr/bin/env python
from __future__ import print_function

import rospy
import cv2
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from geometry_msgs.msg import Twist

pub =None

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image, queue_size= 10)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/hexbot/camera1/image_raw",Image,self.callback)
    self.vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)
    
    #imfinal = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    #ret,thresh = cv2.threshold(imfinal,230,255,cv2.THRESH_BINARY)
    #image, contours, hierarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
    #cnt = contours[1]
    #ellipse = cv2.fitEllipse(cnt)
    #cv_image = cv2.drawContours(cv_image, contours, 1, (0,255,0), 3)
    #img = cv2.ellipse(cv_image,ellipse,(0,255,0),2)
    #M = cv2.moments(contours[1])
    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])
    #contour = contours[1]
    #l = tuple(contour[contour[:,:,0].argmin()][0])
    #r = tuple(contour[contour[:,:,0].argmax()][0])
    #t = tuple(contours[1][contours[1][:,:,1].argmin()][0])
    #b = tuple(contours[1][contours[1][:,:,1].argmax()][0])
    #cv_image = cv2.circle(cv_image, (t[0],t[1]), radius=5, color=(0, 0, 255), thickness=-1)
    #cv_image = cv2.circle(cv_image, (b[0],b[1]), radius=5, color=(0, 0, 255), thickness=-1)
    #cv_image = cv2.circle(cv_image, (cx,cy), radius=5, color=(0, 0, 255), thickness=-1)
    #cv_image = cv2.circle(cv_image, (cv_image.shape[1]//2,cv_image.shape[0]//2), radius=10, color=(255,0,0), thickness=-1)
    #cv2.imshow("Image window", img)
    #cv2.waitKey(3)
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(1)

    #a = cv_image.shape[1]//2
    #b = cx
    #if abs(a-b)<10:
    #  msg =Twist()
    #  msg.linear.y =0
    #  self.vel_pub.publish(msg)
    #else:
    #  msg = Twist()
    #  msg.linear.y = 0.5
    #  self.vel_pub.publish(msg)

    

def main(args):
  global pub
  rospy.init_node('image_converter', anonymous=True)
  image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)