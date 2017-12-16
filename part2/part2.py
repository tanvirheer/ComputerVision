#################################################
## part2.py
## Tanvir Heer and Marco Carmona
## CMPE 264
##
## This file is to undistort the images inputted.
## Since we have 5 images to undistort we have
## to run this file 5 different times. Each time
## using the K matrix and undistored paramters
## found in part1.py.
#################################################
import numpy as np
import cv2
import math as m
from numpy.linalg import inv

# load K matrix and distortion parameters
# from part1.py to now undistort images.
mtx = np.load('mtx.npy')
dist = np.load('dist.npy')



img = cv2.imread('stiched_im.png')
h, w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

R_matrix = np.array([[1, 0, 0], [0, m.cos(45), -m.sin(45)], [0,m.sin(45),m.cos(45)]])

#warp_matrix = ((newcameramtx)*(R_matrix)*(inv(newcameramtx)))

warp_matrix = np.matmul(newcameramtx,R_matrix)

warp_matrix_1 = np.matmul(warp_matrix,(inv(newcameramtx)))

# Find size of im1
sz = img.shape
h, w, _ = img.shape

# Warp image
im2_aligned = cv2.warpAffine (img, (warp_matrix_1), (sz[1],sz[0]))
im2_aligned[0:h, 0:w, :] = img


# Show final results
cv2.imwrite('Warped_Image.png',im2_aligned)





dst = cv2.undistort(img, mtx, dist, None, newcameramtx) # undistorting image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w] # putting new undistorted image in image format with x and y directions
cv2.imwrite('calibresult.png',dst)
