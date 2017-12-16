##########################################################
## part5.py
## Tanvir Heer and Marco Carmona
## CMPE 264
##
## We manually inserted the homography matrices
## that relate images 2 to 1, 3 to 1, etc. Once
## the matrices are implemented in the warpPerspective
## function it warps each image so that the 
## straight lines all relate to the the straight
## lines from the first image.
##########################################################
import numpy as np
import cv2

# Read the images to be aligned
im1 = cv2.imread("1.png");
im2 = cv2.imread("5.png");

# The following commented lines are actual matrices that are used
# to warp images with repect to the first image

# Homography matrix to warp image 2 to image 1
#H2_1:
#warp_matrix = np.array([[1.02267004e+00, -6.23956960e-03, 1.61901092e+03], [9.45688947e-03, 1.03693342e+00, -1.21311527e+01], [8.49632739e-06, 5.06007908e-06, 1.00000000e+00]])

# Homography matrix to warp image 3 to image 1
#H3_1:
#warp_matrix = np.array([[0.90945847270252023, -0.055956692838605084, 4287.8900464488497], [0.012426394576524842, 0.94626247388253149, 128.01486655502373], [4.3769136849384232e-06, 4.6716030915871986e-06, 1.022742206336136]])

# Homography matrix to warp image 4 to image 1
#H4_1:
#warp_matrix = np.array([[1.0768033358163214, -0.17843873477349514, 6228.0789067316064], [0.070903736926937744, 0.93994144414495473, 145.37108178374609], [2.8088734097713681e-05, -3.6729380399589815e-06, 1.0320319173606198]])

# Homography matrix to warp image 5 to image 1
#H5_1:
warp_matrix = np.array([[0.80430932843520586, -0.23466538343562562, 8187.1254403288422], [0.013306843119166805, 0.85605781462190988, 460.28211249900471], [9.4861772267705146e-07, -7.0236161952253814e-06, 1.0833260015745363]])

# Convert images to grayscale
im2_gray = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

# Find size of im1
sz = im1.shape
h, w, _ = im1.shape

# Warp image
im2_aligned = cv2.warpPerspective (im2, (warp_matrix), (3*sz[1],3*sz[0]))
im2_aligned[0:h, 0:w, :] = im1


# Show final results
cv2.imwrite('Warped_Image.png',im2_aligned)

