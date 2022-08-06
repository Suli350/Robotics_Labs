# TECHIN 517 Robotics Lab4


## Intro

In this lab, I drove the robot using teleop inforot of the can then let the robot grasp the can.

## Explanation

The following sections explain how the robot is to grasp the can.

## Procedure

- Move the robot using teleop in front of the can
- Run the grasp node
    - The node first will detect the can
    - Take an image of the can
    - Threshold the can to find red color
    - Find centroid of the can
    - Get pose (x, y, z) of the can 
    - Set pose using go_to_pose() function
    - Open the gripper using Fetch API
    - Move the aram to reach the can
    - Set the gripper orientation to horizontal 
    - Move the gripper forward to the can
    - Close the gripper
    - And finally lift the can off.

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

    Launch Gazebo: roslaunch $HOME/catkin_ws/src/robotics_labs/Lab4/project_env.launch
    Run python script: python $HOME/catkin_ws/src/robotics_labs/Lab4/grasp.py

## Vizualization Options

    Camera Image Viewer: rosrun rqt_image_view rqt_image_view /head_camera/rgb/image_raw
    Launch RViz: rosrun rviz rviz -d $HOME/catkin_ws/src/robotics_labs/Lab4/fetch.rviz



