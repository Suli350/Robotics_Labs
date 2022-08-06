#! /usr/bin/python
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
from matplotlib import pyplot as plt
from multiprocessing import Queue
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import fetch_api
import time
import math

# for extracting the center of the blue rectangle
from find_centroid import extract_centroid

# Instantiate CvBridge
bridge = CvBridge()

base = fetch_api.Base()

def image_callback(msg):
    print("Recieved an image")
    try:
        # Convert your ROS Image message to OpenCV2
        img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # find the centroid of the picture
        x, y = extract_centroid(img, debug=False)
        print((x,y))
        # find the angular offset using some trig and the camera's field of view
        hfov = 54 # deg
        hfov_rad = hfov * 2 * math.pi / 360.0
        factor = math.tan(hfov_rad/2)
        theta = math.atan(x*factor)
        print(theta)
        # set the forward speed to 0.5 m/s
        # set the angular velocity proportional to the angular offset
        # TODO: make this into a PID controller
        base.move(0.5, -theta)

        # TODO: stop the robot before it hits the blue wall at the end of the hallway


def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/head_camera/rgb/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)

    rospy.spin()

if __name__ == '__main__':
    main()