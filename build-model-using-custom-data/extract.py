
#!/usr/bin/env python2 | Python 2
# install pip as package manager

import cv2 
import os 

# Read the video from specified path 
cam = cv2.VideoCapture("./video-raw-tomato/video-tomato-1.mp4") 

try: 
	
	# Create a folder 
	if not os.path.exists('extract-2'): 
		os.makedirs('extract-2') 

# Catch error 
except OSError: 
	print ('Error creating folder.') 
 
# Initial framecount
framecount = 0

while(True): 
	
	# Reads 
	ret,frame = cam.read() 

	if ret: 
		# Shows status 
		filename = './extract-2/frame' + str(framecount) + '.jpg'
		print ('Creating...' + filename) 
 
		cv2.imwrite(filename, frame) 

		# Counter | Adjust with filename
		framecount += 1 
	else: 
		break
 
cam.release() 
cv2.destroyAllWindows() 
