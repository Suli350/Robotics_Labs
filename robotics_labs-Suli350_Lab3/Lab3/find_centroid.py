#! /usr/bin/python

# inspired by https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

import cv2
import numpy as np
import math

import imutils

def extract_centroid(img, debug=False):
    # convert to HSV
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # For HSV, hue range is [0,179], saturation range is [0,255], and value range is [0,255]
    # source: https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html

    # blur image (doesn't seem to help)
    # img_blur = cv2.GaussianBlur(img_HSV, (5, 5), 0)

    # thresholding to only blue pixels
    #img_threshold = cv2.inRange(img_HSV, (90, 126, 100), (133, 255, 255))
    lower_red = np.array([175,0,0])
    upper_red = np.array([255,255,255])
    img_threshold = cv2.inRange(img_HSV, lower_red, upper_red)

    if debug:
        cv2.imshow("Thresh", img_threshold)

    # extract contours
    contours = cv2.findContours(img_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if debug:
        # draw contours
        img_contours = img.copy()
        cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)
        cv2.imshow("Contours", img_contours)

    

    # find the centroids of the contours
    centroids = []
    for contour in contours:
        M = cv2.moments(contour)
        cX = int((M["m10"] / M["m00"]) if M["m00"] != 0 else 0)
        cY = int((M["m01"] / M["m00"])if M["m00"] != 0 else 0)
        centroids.append((cX, cY))

    if debug:
        img_centroids = img.copy()
        for centroid in centroids:
            cv2.circle(img_centroids, centroid, 7, (255, 255, 255), -1)
        cv2.imshow("Centroids", img_centroids)

    if (len(centroids) > 0):
        if debug:
            print(centroids[0])
            print(img.shape)

        # convert centroid to new coordinate system
        # 0,0 in center of image
        # X = +1 on right side of screen
        # Y = +1 on top of screen
        height, width, _ = img.shape
        x1, y1 = centroids[0]
        x2 = (x1 / float(width)) * 2 - 1
        y2 = -(y1 / float(height)) * 2 + 1
        coords = (x2, y2)
    else:
        coords = (0,0)

    if debug:
        cv2.waitKey(1)
    return coords

if __name__ == "__main__":
    img = cv2.imread('frame_ROS_camera.jpeg')
    # Displaying the image 
    cv2.imshow("Image",img)

    coords = extract_centroid(img, debug=True)
    print(coords)

    #waits for user to press any key 
    cv2.waitKey(0) 

    #closing all open windows 
    cv2.destroyAllWindows()