'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 1A of Pharma Bot (PB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ PB_2228 ]
# Author List:		[ Sandeep Kumar Rai ]
# Filename:			task_1a.py
# Functions:		detect_traffic_signals, detect_horizontal_roads_under_construction, detect_vertical_roads_under_construction,
#					detect_medicine_packages, detect_arena_parameters
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import cv2
import numpy as np
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

def detect_traffic_signals(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list of
	nodes in which traffic signals are present in the image

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`traffic_signals` : [ list ]
			list containing nodes in which traffic signals are present
	
	Example call:
	---
	traffic_signals = detect_traffic_signals(maze_image)
	"""    
	traffic_signals = []

	##############	ADD YOUR CODE HERE	##############
	x1 = 96
	y1 = 105
	# Defining the color blue
	red = [0,0,255]

	# Loop for iterating over each grid cross-section
	for i in range(1,8):
		x=96
		y=105
		for j in range(1,8):
			# Slicing of image to cross section points in grid
			img = maze_image[x1:y1, x:y]
			x= x+100
			y=y+100
			# Checking for if the color of traffic signal is red and if it is red then appending the name of traffic signal to the list traffic_signals
			Y, X = np.where(np.all(img==red,axis=2))
			if Y.size>0 and X.size>0:
				s = 64+j
				traffic_signals.append(str(chr(s)+str(i)))
		x1 = x1+100
		y1 = y1+100
	# Sorting the list traffic_signal lexicographically
	traffic_signals.sort()
	##################################################
	
	return traffic_signals
	

def detect_horizontal_roads_under_construction(maze_image):
	
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing horizontal links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`horizontal_roads_under_construction` : [ list ]
			list containing missing horizontal links
	
	Example call:
	---
	horizontal_roads_under_construction = detect_horizontal_roads_under_construction(maze_image)
	"""    
	horizontal_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	x1 = 96
	y1 = 105
	# Defining the color white
	white = [255,255,255]

	# Iterating over each block of horizontal road and if the road is not present i.e. that part of image is white then appending the name of that road to list
	for i in range(1,8):
		x=96
		y=205
		for j in range(1,7):
			# Slicing the image to view the road part only and iterating over the whole image through two for loop
			img = maze_image[x1:y1, x:y]
			x= x+100
			y=y+100
			# Checking if the color of image is white 
			Y, X = np.where(np.all(img==white,axis=2))
			if Y.size>0 and X.size>0:
				# Starting point of road under construction
				first = chr(64+j)+str(i)
				# End point of road under construction
				second = chr(65+j)+str(i)
				# If the color of road is white then appending the name of road
				horizontal_roads_under_construction.append(str(first+"-"+second))
		x1 = x1+100
		y1 = y1+100
	# Sorting the names of road under construction lexicographically
	horizontal_roads_under_construction.sort()
	##################################################
	
	return horizontal_roads_under_construction	

def detect_vertical_roads_under_construction(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing vertical links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`vertical_roads_under_construction` : [ list ]
			list containing missing vertical links
	
	Example call:
	---
	vertical_roads_under_construction = detect_vertical_roads_under_construction(maze_image)
	"""    
	vertical_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	x1 = 96
	y1 = 205
	
	# Defining the white color
	white = [255,255,255]

	# Iterating over the image to find the vertical road under construction
	for i in range(1,7):
		x=96
		y=105
		for j in range(1,8):
			# Slicing the image to view vertical road part only and iterating over whole image to traverse through whole verical road
			img = maze_image[x1:y1, x:y]
			x= x+100
			y=y+100
			# Checking if the color of road is white and hence under construction
			Y, X = np.where(np.all(img==white,axis=2))
			if Y.size>0 and X.size>0:
				# Starting point of road under construction
				first = chr(64+j)+str(i)
				# End point of road under construction
				second = chr(64+j)+str(i+1)
				# # If the color of road is white then appending the name of road
				vertical_roads_under_construction.append(str(first+"-"+second))
		x1 = x1+100
		y1 = y1+100
	# Sorting the names of road under construction lexicographically
	vertical_roads_under_construction.sort()
	##################################################
	
	return vertical_roads_under_construction


def detect_medicine_packages(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list of
	details of the medicine packages placed in different shops

	** Please note that the shop packages should be sorted in the ASCENDING order of shop numbers 
	   as well as in the alphabetical order of colors.
	   For example, the list should first have the packages of shop_1 listed. 
	   For the shop_1 packages, the packages should be sorted in the alphabetical order of color ie Green, Orange, Pink and Skyblue.

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`medicine_packages` : [ list ]
			nested list containing details of the medicine packages present.
			Each element of this list will contain 
			- Shop number as Shop_n
			- Color of the package as a string
			- Shape of the package as a string
			- Centroid co-ordinates of the package
	Example call:
	---
	medicine_packages = detect_medicine_packages(maze_image)
	"""    
	medicine_packages_present = []

	##############	ADD YOUR CODE HERE	##############
	# Inintial height co-ordinates of required cropped image
	x1 = 96
	y1 = 205

	# Defining the color in BGR format
	green = [0,255,0]
	orange = [0,127,255]
	pink = [180,0,255]
	skyblue = [255,255,0]

	# Iterating over each block/shops using slicing of numpy array of image
	for i in range(1,2):
		x=96
		y=205
    
		for j in range(1,7):
			list_of_packages = []
			# First shop slicing from image
			img = maze_image[x1:y1, x:y] 
			# Incrementing the coordinates of shops to next shop
			x= x+100
			y=y+100
		
			value = 0
			# convert the image to grayscale and checking for contour and approxPolyDP and accordingly detecting the shape based on length of approxPolyDP
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
			contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

			for contour in contours:
				approx= cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
				value = len(approx)
			if value==12:
				shape = "Circle"
			elif value == 5:
				shape = "Triangle"
			elif value == 8:
				shape = "Square"
        
        
        
			# Finding whether any green package present in the shop
			Y, X = np.where(np.all(img==green,axis=2))
			if Y.size>0 and X.size>0:
				list_of_packages.append(f"Shop_{j}")
				list_of_packages.append("Green")
				list_of_packages.append(shape)
				# Finding position
				u1=15;v1=55
				package_coordinate=[]
				pos1=0;pos2=0
				for i_inner in range(1,3):
					u2=15;v2=55
					for j_inner in range(1,3):
						img2 =  img[u1:v1,u2:v2]
						Y, X = np.where(np.all(img2==green,axis=2))
						if Y.size>0 and X.size>0:
							if j_inner==1 and i_inner ==1:
								pos1 = int(f"{j}"+'30')
								pos2 = 130
							elif j_inner==2 and i_inner ==1:
								pos1 = int(f"{j}"+'70')
								pos2 = 130
							elif j_inner==1 and i_inner ==2:
								pos1 = int(f"{j}"+'30')
								pos2 = 170   
							elif j_inner==2 and i_inner ==2:
								pos1 = int(f"{j}"+'70')
								pos2 = 170
					
	#                     cv2.imshow("image",img2)
	#                     cv2.waitKey(0)
	#                     cv2.destroyAllWindows()
						u2 =u2+40;v2=v2+40
					u1=u1+40;v1=v1+40
				if shape=="Triangle":
					pos2=pos2-1;
				package_coordinate.append(pos1);package_coordinate.append(pos2)
				list_of_packages.append(package_coordinate)
		
			if len(list_of_packages)>0:
				medicine_packages_present.append(list_of_packages)
			list_of_packages = []
			Y, X = np.where(np.all(img==orange,axis=2))
			if Y.size>0 and X.size>0:
				list_of_packages.append(f"Shop_{j}")
				list_of_packages.append("Orange")
				list_of_packages.append(shape)
			
			# Finding position
				u1=15;v1=55
				pos=[]
				pos1=0;pos2=0
				for i_inner in range(1,3):
					u2=15;v2=55
					for j_inner in range(1,3):
						img2 =  img[u1:v1,u2:v2]
						Y, X = np.where(np.all(img2==orange,axis=2))
						if Y.size>0 and X.size>0:
							if j_inner==1 and i_inner ==1:
								pos1 = int(f"{j}"+'30')
								pos2 = 130
							elif j_inner==2 and i_inner ==1:
								pos1 = int(f"{j}"+'70')
								pos2 = 130
							elif j_inner==1 and i_inner ==2:
								pos1 = int(f"{j}"+'30')
								pos2 = 170   
							elif j_inner==2 and i_inner ==2:
								pos1 = int(f"{j}"+'70')
								pos2 = 170
					
	#                     cv2.imshow("image",img2)
	#                     cv2.waitKey(0)
	#                     cv2.destroyAllWindows()
						u2 =u2+40;v2=v2+40
					u1=u1+40;v1=v1+40
				if shape=="Triangle":
					pos2=pos2-1;
				pos.append(pos1);pos.append(pos2)
				list_of_packages.append(pos)
			
			if len(list_of_packages)>0:
				medicine_packages_present.append(list_of_packages)
			list_of_packages = []
			Y, X = np.where(np.all(img==pink,axis=2))
			if Y.size>0 and X.size>0:
				list_of_packages.append(f"Shop_{j}")
				list_of_packages.append("Pink")
				list_of_packages.append(shape)
			
			# Finding position
				u1=15;v1=55
				pos=[]
				pos1=0;pos2=0
				for i_inner in range(1,3):
					u2=15;v2=55
					for j_inner in range(1,3):
						img2 =  img[u1:v1,u2:v2]
						Y, X = np.where(np.all(img2==pink,axis=2))
						if Y.size>0 and X.size>0:
							if j_inner==1 and i_inner ==1:
								pos1 = int(f"{j}"+'30')
								pos2 = 130
							elif j_inner==2 and i_inner ==1:
								pos1 = int(f"{j}"+'70')
								pos2 = 130
							elif j_inner==1 and i_inner ==2:
								pos1 = int(f"{j}"+'30')
								pos2 = 170   
							elif j_inner==2 and i_inner ==2:
								pos1 = int(f"{j}"+'70')
								pos2 = 170
					
	#                     cv2.imshow("image",img2)
	#                     cv2.waitKey(0)
	#                     cv2.destroyAllWindows()
						u2 =u2+40;v2=v2+40
					u1=u1+40;v1=v1+40
				if shape=="Triangle":
					pos2=pos2-1;
				pos.append(pos1);pos.append(pos2)
				list_of_packages.append(pos)
			
			
			if len(list_of_packages)>0:
				medicine_packages_present.append(list_of_packages)
			list_of_packages = []
			Y, X = np.where(np.all(img==skyblue,axis=2))
			if Y.size>0 and X.size>0:
				list_of_packages.append(f"Shop_{j}")
				list_of_packages.append("Skyblue")
				list_of_packages.append(shape)
            
			# Finding position
				u1=15;v1=55
				pos=[]
				pos1=0;pos2=0
				for i_inner in range(1,3):
					u2=15;v2=55
					for j_inner in range(1,3):
						img2 =  img[u1:v1,u2:v2]
						Y, X = np.where(np.all(img2==skyblue,axis=2))
						if Y.size>0 and X.size>0:
							if j_inner==1 and i_inner ==1:
								pos1 = int(f"{j}"+'30')
								pos2 = 130
							elif j_inner==2 and i_inner ==1:
								pos1 = int(f"{j}"+'70')
								pos2 = 130
							elif j_inner==1 and i_inner ==2:
								pos1 = int(f"{j}"+'30')
								pos2 = 170   
							elif j_inner==2 and i_inner ==2:
								pos1 = int(f"{j}"+'70')
								pos2 = 170
					
	#                     cv2.imshow("image",img2)
	#                     cv2.waitKey(0)
	#                     cv2.destroyAllWindows()
						u2 =u2+40;v2=v2+40
					u1=u1+40;v1=v1+40
				if shape=="Triangle":
					pos2=pos2-1;
				pos.append(pos1);pos.append(pos2)
				list_of_packages.append(pos)
			
			if len(list_of_packages)>0:
				medicine_packages_present.append(list_of_packages)
			list_of_packages = []
			# cv2.namedWindow('res',cv2.WINDOW_NORMAL)
			# cv2.imshow('res',img)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()
		x1 = x1+100
		y1 = y1+100


	##################################################

	return medicine_packages_present

def detect_arena_parameters(maze_image):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary
	containing the details of the different arena parameters in that image

	The arena parameters are of four categories:
	i) traffic_signals : list of nodes having a traffic signal
	ii) horizontal_roads_under_construction : list of missing horizontal links
	iii) vertical_roads_under_construction : list of missing vertical links
	iv) medicine_packages : list containing details of medicine packages

	These four categories constitute the four keys of the dictionary

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`arena_parameters` : { dictionary }
			dictionary containing details of the arena parameters
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)
	"""    
	arena_parameters = {}

	##############	ADD YOUR CODE HERE	##############
	arena_parameters["traffic_signals"] = detect_traffic_signals(maze_image)
	arena_parameters["horizontal_roads_under_construction"] = detect_horizontal_roads_under_construction(maze_image)
	arena_parameters["vertical_roads_under_construction"] = detect_vertical_roads_under_construction(maze_image)
	arena_parameters["medicine_packages_present"] = detect_medicine_packages(maze_image)
	##################################################
	
	return arena_parameters

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########	

if __name__ == "__main__":

    # path directory of images in test_images folder
	img_dir_path = "public_test_images/"

    # path to 'maze_0.png' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
	
	# read image using opencv
	maze_image = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor maze_' + str(file_num) + '.png')

	# detect and print the arena parameters from the image
	arena_parameters = detect_arena_parameters(maze_image)

	print("Arena Prameters: " , arena_parameters)

	# display the maze image
	cv2.imshow("image", maze_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 15):
			
			# path to maze image file
			img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
			
			# read image using opencv
			maze_image = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor maze_' + str(file_num) + '.png')
			
			# detect and print the arena parameters from the image
			arena_parameters = detect_arena_parameters(maze_image)

			print("Arena Parameter: ", arena_parameters)
				
			# display the test image
			cv2.imshow("image", maze_image)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()