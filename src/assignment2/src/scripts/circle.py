#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
def move():
	# Starts a new node
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	#Receiveing the user's input
	print("Let's move your robot")
	#speed = int(input("Input your speed:"))
	speed = 1
	aspeed = 40
	angular_speed = aspeed*2*(math.pi)/360
	angle = 25
	relative_angle = angle*2*(math.pi)/360
#	distance = int(input("Type your distance:"))
	distance = 8
#	isForward = int(input("Foward?: "))#True or False
	isForward = 1

	

	#Checking if the movement is forward or backwards
	if(isForward):
		vel_msg.linear.x = abs(speed)
	else:
		vel_msg.linear.x = -abs(speed)
	#Since we are moving just in x-axis
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = abs(speed)


	while not rospy.is_shutdown():

		#Setting the current time for distance calculus
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		current_angle = 0
		#Loop to move the turtle in an specified distance
		count = 0 
		
		while(current_distance < distance):	

			#Publish the velocity
			velocity_publisher.publish(vel_msg)
			#Takes actual time to velocity calculus
			t1=rospy.Time.now().to_sec()
			#Calculates distancePoseStamped
			current_distance= speed*(t1-t0)
					
				
		#After the loop, stops the robot
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		#Force the robot to stop
		velocity_publisher.publish(vel_msg)
		
		# If we press control + C, the node will stop.
		rospy.spin()


if __name__ == '__main__':
	try:
		#Testing our function
		move()
	except rospy.ROSInterruptException: pass
