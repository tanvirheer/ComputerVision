# ComputerVision
#########################################################
## README
## Tanvir Heer and Marco Carmona
## CMPE 264
## Project 2
##
## This README will try to address our steps that
## we took to run the programs in parts 1-7
#########################################################

Part 1: Part1 folder contains 20 images that were used for calibration (pic1-pic20.png). Run file "python ./part1.py". Outputs are stored in mtx.out (Calibration Parameter) and dist.out (Distortion parameters). .npy files are used for file input/output in next parts.

Part 2: Part2 folder contains 5 images of photos we took. Run file "python ./part2.py". Output is the undistorted image, which the K matrix and distortion parameters were applied to. In the code, we manually change input image file name and output the distorted image 1 by 1 named as calibresult.png.

Part 3: Part3 folder contains 5 images where pairwise homogrpahy is implemented. Run file "python ./part3.py". Output is corresponding H2_1.out, H3_2.out, H4_3.out, H5_4.out that contains the matrix data. The .npy files are created to be exported to next part.

Part4: Part4 folder contains part4.py, this code does the homography multiplications and computes H2_1.npy, H3_2.npy, H4_3.npy, H5_4.npy and outputs p4_H2_1.npy, p4_H3_1.npy, p4_h4_1.npy, p4_H5_1.npy for next part.

Part5: Part5 folder contains warping code. Run "python ./part5.py" on the images. If im2 in code reads in "5.png" and im1 read in "1.png" this will then output warped image that is related to the image read in by im1. The output in code
is named as "Warped_Image.png" but the files in the folder are cropped out images of the original ones, which will be used for the next part. Cropping out the excess empty black areas from output a large image.

Part6: Part6 folder contains the fully stitched image. Run "python ./part6.py" on images. First on images "W2_1c.png" and "W3_1c.png" which output an image called "image.png". This "image.png" will now be uses on the next Run to stich the 
next picture to make one whole panoramic image. Once panoramic image is produced this will then be used for the next part. NOTE: (This part takes time to compile!)

Part 7: Part7 folder contains the rotated stitched image. Run "python ./part7.py" on stiched_img.png. It output
a rotated image.
