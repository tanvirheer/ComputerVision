################################################################
## part6.py
## Tanvir Heer and Marco Carmona
## CMPE 264
## 
## This file stitches two images together. So each time two
## images are stiched together it is saves and this new
## stiched image is then used as the left image. Therefore,
## since two pictures are stitched at a time we had to call
## this file four different times. Each time stitching images
## that we took located further right from the first image
## taken. This file assumes that the images inputted are
## already warped.
################################################################

import numpy as np
import cv2
OFFSET = 3
def mix_match(leftImage, warpedImage):
    i1y, i1x = leftImage.shape[:2]
    i2y, i2x = warpedImage.shape[:2]


    for i in range(0, i1x):
        for j in range(0, i1y):
            try:
                if(np.array_equal(leftImage[j,i],np.array([0,0,0])) and  \
                    np.array_equal(warpedImage[j,i],np.array([0,0,0]))):
                    # check 1
                    # both left and warp images are black

                        # instead of just putting it with black, 
                        # take average of all nearby values and avg it.
                    x_median = np.median(leftImage[j,i-OFFSET], leftImage[j,i+OFFSET])
                    y_median = np.median(leftImage[j-OFFSET,i], leftImage[j+OFFSET,i])
                    warpedImage[j,i] = (x_median+y_median)/2
                else:
                    if(np.array_equal(warpedImage[j,i],[0,0,0])):
                        # check 2
                        # warp image is black just print
                        # i.e. edges and such
                        warpedImage[j,i] = leftImage[j,i]
                    else:
                        if not np.array_equal(leftImage[j,i], [0,0,0]) and \
                        	not np.warpedImage(warpedImage[j,i], [0,0,0]):
                            # check 3
                            # If here already checked the following:
                        	# left image has colored pixels
                        	# check 1: both pixels are black
                        	# check 2: right image has black pixel
                        	# check 3: both images have colored pixels
                            bl,gl,rl = leftImage[j,i]
                            b2,g2,r2 = warpedImage[j,i]                               
                            warpedImage[j, i] = [np.median(b1,b2),np.median(g1,g2),np.median(r1,r2)]
                        else:
                        	if not np.array_equal(leftImage[j,i], [0,0,0]):
                                # check 4
                                # When all else fails just send pixel
                                # to the new "warped" image
                        		bl,gl,rl = leftImage[j,i]
                        		warpedImage[j, i] = [b1,g1,r1]
            except:
                pass

    return warpedImage

img1 = cv2.imread('Warped_Image2_1.png')
img2 = cv2.imread('Warped_Image3_1.png')

# Print out stitched image
cv2.imwrite("image.png",mix_match(img1,img2))
