######################################################
## part1.py
## Tanvir Heer and Marco Carmona
## CMPEv264
## 
## This file is used to calibrate our camera. We use
## a checkerboard to calibrate. This program detects
## the corners of the checkerboard from each 
## checkerboard image that is sent into this program.
## By scanning more images and detecting more corners
## we improve the output K matrix 'mtx' and radial 
## output paramater 'dist' in this case.
######################################################

import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*5,3), np.float32)
objp[:,:2] = np.mgrid[0:5,0:5].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.png')

for fname in images:
    img = cv2.imread(fname)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (5,5),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (5,5), corners2,ret) #was img =

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

# save and print out K matrix and distortion parameters
np.save('mtx',mtx)
np.save('dist',dist)
np.savetxt('mtx.out',mtx)
np.savetxt('dist.out',dist)
