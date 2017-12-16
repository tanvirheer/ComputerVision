############################################################
## part7.py
## Tanvir Heer and Marco Carmona
## CMPE 264
##
## This program rotates the stitched image by 45 degrees.
############################################################


import numpy as np
import cv2
import math as m

# define euler angles for rotation
C = m.cos(m.pi/4)
S = m.sin(m.pi/4)

# define K matrix found in part 1 of project
K = np.array([[  3.503e+03,   0.00000000e+00,   1.52549042e+03],
 [  0.00000000e+00,   3.503e+03,   1.99340074e+03],
 [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]])

# define inv(K) 
M = np.array([[1, 0, -1.52549042e+03],
	[0, 1, -1.99340074e+03],
	[0, 0, 3.503e+03]])

# define rotational matrix such that
# when looking at the image from above
# it would be seen as a 45 degree rotation
rotMat = np.array([ [C, 0, S],

                        [0, 1, 0],

                        [-S, 0, C]])

L = np.matmul(rotMat,M)          
H = np.matmul(K,L) # "virtually" rotation homography matrix
img = cv2.imread('stiched_im.png')
sz = img.shape
h, w, _ = img.shape

# warp image by 45 degrees
im2_aligned = cv2.warpPerspective(img,H,(5*sz[1],5*sz[0]))
print im2_aligned.shape



# Show final results
cv2.imwrite('Rot_img.png',im2_aligned)
