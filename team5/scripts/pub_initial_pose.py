#!/usr/bin/env python

import rospy
import geometry_msgs
import time

time.sleep(1.)

pub = rospy.Publisher('/initialpose', geometry_msgs.msg.PoseWithCovarianceStamped, queue_size=10)
rospy.init_node('initial_pose_publisher', anonymous=True)

pose = geometry_msgs.msg.PoseWithCovarianceStamped()
pose.header.frame_id = "map_o3d"
pose.pose.pose.position.x=8.639346270433826
pose.pose.pose.position.y=-32.01220504629785
pose.pose.pose.position.z=0
pose.pose.pose.orientation.z=0.9008209
pose.pose.pose.orientation.w=0.4341909
pose.pose.covariance=[0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
rospy.loginfo("Publishing initial pose...")
rospy.loginfo(pose)
pub.publish(pose)
