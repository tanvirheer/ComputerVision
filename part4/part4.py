########################################################
## part4.py
## Tanvir Heer and Marco Carmona
## CMPE 264
## 
## This file does matrix multiplication for the
## different homography matrices that we found in 
## Part3: Finding Pairwise Homography. We do matrix
## multiplication so that all images that will be
## warped, are warped with respect to the first images
## perspective. This file helps with finding the 
## homography matrices that relate all images to the
## first image.
######################################################## 

import numpy as np
import cv2

# Matrix multiplication function
def matrixmultiplication(mA, mB):
	#zeroed matrix with height of mA and width of mB
	result = [[0 for y in range(len(mB[0]))] for x in range(len(mA))]
	for i in range(len(mA)):
		for j in range(len(mA)):
			for k in range(len(mA[0])):
				result[i][j] += mA[i][k]*mB[k][j]

	return result

# Homography matrix that relates image 2 to 1.
# Image 1 is the image first taken that begins
# at the farthest left of the 5 images
M2_1 = np.array([[1.022670040378709455e+00, -6.239569603775755452e-03, 1.619010917802496124e+03],
	[9.456889465611018064e-03, 1.036933418303967791e+00, -1.213115268353137388e+01],
	[8.496327394716175174e-06, 5.060079081123920794e-06, 1.000000000000000000e+00]])

# Homography matrix that relates image 3 to 2
M3_2 = np.array([[8.944533661440057237e-01, -4.989865754904993650e-02, 2.610396103145649249e+03],
	[3.788402247054426138e-03, 9.130192092811689752e-01, 1.113473534477205504e+02],
	[-3.241824568088192860e-06, 4.756090211328065646e-07, 1.000000000000000000e+00]])

# Homography matrix that relates image 4 to 3
M4_3 = np.array([[1.081122901220788357e+00, -9.855727324620454366e-02, 2.132750492870511607e+03],
	[5.767900718167602581e-02, 9.956583083735753847e-01, -9.665588757247757457e+00],
	[2.257391833930297068e-05, -7.717371733171479132e-06, 1.000000000000000000e+00]])

# Homography matrix that relates image 5 to 4
M5_4 = np.array([[8.719047967892687989e-01, -5.429587727127378055e-02, 1.851688990855063366e+03],
	[-4.805989163216177473e-02, 9.151725742134958486e-01, 1.953519155698035092e+02],
	[-2.298243385503934220e-05, -2.070809573855232264e-06, 1.000000000000000000e+00]])

h3_1 = matrixmultiplication(M2_1,M3_2) # relating image 3 to image 1
h4_1 = matrixmultiplication(h3_1,M4_3) # rleating image 4 to image 1
h5_1 = matrixmultiplication(h4_1,M5_4) # relating image 5 to image 1

# Printing out matrices
print "H2_1"
print M2_1
print "H3_1"
print h3_1
print "H4_1"
print h4_1
print "H5_1"
print h5_1