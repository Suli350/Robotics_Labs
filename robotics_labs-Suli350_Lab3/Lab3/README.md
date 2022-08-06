# TECHIN 517 Robotics Lab3


## Intro

In this lab, I drove the robot using teleop inforot of the can on the table, and then makes the robot drive towards the can using the code.

## Explanation

The following sections explain how the robot is able to navigate towards the can on a table.

## Procedure

    1. Drive the robot in front of the can
    2. Acquire image
    3. Determine the contours of the can
    4. Find the center of the can
    5. Move the robot forwards

## Image Processing

Image processing occurs in the file findCentroid.py. The technique is outlined as follows:

    1. Convert the image to HSV colorspace. This makes the thresholding step easier.
    2. Threshold the image to extract only the red areas. For this scene, this should be the can on the table.
    3. Find the contours of the thresholded image, which represent the outline of the red can on the table.
    4. Find the centroid of the red can using the contours.
    5. Convert the centroid coordinates from pixel coordinates to a more useful coordinate space with the origin in the center of the image. 


## Control Loop Approach

The control loop inputs the coordinates of centroid of the red can on the table. It outputs the velocity commands that move the robot. The technique is outlined as follows:

    1. The robot processes a camera frame to extract the centroid coordinates.
    2. The robot's horizontal orientation is determined by using the horizontal position of the centroid and some trigonometry.
    3. The robot's angular velocity is set proportional to the horizontal orientation to steer it towards the center of can on the table.
    4. The robot's forward velocity is set to a constant positive value.
    5. The robot moves forward.

## How To Run

Make sure the required Python packages are installed, then follow the launch instructions. Vizualization Options contains various ways of viewing the robot's operation other than just looking at the Gazebo window.
Required Python Packages

    numpy
    cv2
    imutils
    rospy
    fetch_api

## Launch Instructions

Run each command in a seperate terminal tab.

    Launch Gazebo: roslaunch $HOME/catkin_ws/src/robotics_labs/Lab3/project_env.launch
    Run python script: python $HOME/catkin_ws/src/robotics_labs/Lab3/move.py

## Vizualization Options

    Camera Image Viewer: rosrun rqt_image_view rqt_image_view /head_camera/rgb/image_raw
    Launch RViz: rosrun rviz rviz -d $HOME/catkin_ws/src/robotics_labs/Lab3/fetch.rviz



