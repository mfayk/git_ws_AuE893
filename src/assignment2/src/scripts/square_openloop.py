#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
def move():
	
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	#Receiveing the user's input
	print("Let's move your robot")
	speed = 0.2
	#speed = rospy.get_param('~speed')

	distance = 2

	#Checking if the movement is forward or backwards

	

	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0


	while not rospy.is_shutdown():

		#Setting the current time for distance calculus
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		vel_msg.linear.x = abs(speed)
		
		while(current_distance < distance):	

			#Publish the velocity
			velocity_publisher.publish(vel_msg)
			#Takes actual time to velocity calculus
			t1=rospy.Time.now().to_sec()
			#Calculates distancePoseStamped
			current_distance= speed*(t1-t0)
		
		vel_msg.linear.x = 0
		
		
		#Force the robot to stop
		velocity_publisher.publish(vel_msg)
		
		# If we press control + C, the node will stop.
		#rospy.spin()
		break

def rotate():
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	angular_speed = 0.2
	relative_angle = math.pi/2
	angle = 90

	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	
	
	while not rospy.is_shutdown():

		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		vel_msg.angular.z = -abs(angular_speed)
		#turn 1
		while(current_angle < relative_angle):
				
			velocity_publisher.publish(vel_msg)
			
			t1 = rospy.Time.now().to_sec()
			
			current_angle = angular_speed*(t1-t0)
				
		vel_msg.angular.z = 0
		
		
		#Force the robot to stop
		velocity_publisher.publish(vel_msg)
		
		# If we press control + C, the node will stop.
#		rospy.spin()
		break	
	
	


if __name__ == '__main__':
	try:
		#Testing our function
		# Starts a new node
		rospy.init_node('robot_cleaner', anonymous=True)
		move()
		rotate()
		move()
		rotate()
		move()
		rotate()
		move()
		rotate()
	except rospy.ROSInterruptException: pass
