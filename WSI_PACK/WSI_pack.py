import numpy
import py_wsi
import py_wsi.imagepy_toolkit as tk
import matplotlib
import cv2
import scipy
from scipy.spatial.distance import directed_hausdorff
from scipy import ndimage
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import PIL


"""=================================================================================================================="""
# 1st step: read the image at highest level (now magnification)
"""
file_dir = "/Users/carolina/Desktop/project/"
db_location = "/Users/carolina/Desktop/project/data/"
db_name = "patch_db"

turtle = py_wsi.Turtle(file_dir, db_location, db_name)

level_count, level_tiles, level_dims = turtle.retrieve_tile_dimensions('imagem1.svs', patch_size = 262144)
print("Level count:         " + str(level_count))
print("Level tiles:         " + str(level_tiles))
print("Level dimensions:    " + str(level_dims))


# does not run because of the database
# patches, coords, classes, labels = turtle.get_patches_from_file('imagem1.svs')

patch_1 = turtle.retrieve_sample_patch('imagem1.svs', 262144, 18, overlap=0)
"""

"""=================================================================================================================="""
# 1st step: read a png/jpeg image - only to do the threshold

image_BGR = cv2.imread('/Users/carolina/Desktop/project/imagem1.png')
image_RGB = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2RGB)
# print(image.shape)  # (9063, 11971, 3)


#plt.subplot(121), plt.imshow(image_BGR)
#plt.subplot(122), plt.imshow(image_RGB)
#plt.show()

"""
# there are no differences between the two color spaces
p_BGR_1 = image_BGR[2293, 5919]
p_RGB_1 = image_RGB[2293, 5919]
print(p_BGR_1, p_RGB_1)
p_BGR_2 = image_BGR[3306, 3699]
p_RGB_2 = image_RGB[3306, 3699]
print("Pixel_pen           " + str(p_RGB_2))
p_BGR_3 = image_BGR[4892, 3793]
p_RGB_3 = image_RGB[4892, 3793]
print("Pixel_pen           " + str(p_RGB_3))
p_BGR_4 = image_BGR[5545, 4787]
p_RGB_4 = image_RGB[5545, 4787]
print("Pixel_pen           " + str(p_RGB_4))
p_BGR_5 = image_BGR[4954, 6373]
p_RGB_5 = image_RGB[4954, 6373]
print("Pixel_pen           " + str(p_RGB_5))
p_BGR_6 = image_BGR[3151, 7088]
p_RGB_6 = image_RGB[3151, 7088]
print("Pixel_pen           " + str(p_RGB_6))
p_BGR_7 = image_BGR[5731, 5565]
p_RGB_7 = image_RGB[5731, 5565]
print("Pixel_pen           " + str(p_RGB_7))
p_BGR_1_norm = image_BGR[4021, 5129]
p_RGB_1_norm = image_RGB[4021, 5129]
print("Pixel_normal        " + str(p_RGB_1_norm))
p_BGR_2_norm = image_BGR[3808, 7154]
p_RGB_2_norm = image_RGB[3808, 7154]
print("Pixel_normal        " + str(p_RGB_2_norm))
"""

"""=================================================================================================================="""
# 2nd step: convert the image to an array

# get the histograms of the three different color channels
np_im = numpy.array(image_RGB)
np_im_1 = numpy.asarray(image_RGB)
#print(np_im_1.shape)
#print(np_im.shape)

np_im_R = np_im[:, :, 0]
np_im_G = np_im[:, :, 1]
np_im_B = np_im[:, :, 2]

#plt.hist(np_im_B.flatten(), bins=300)

"""
def binarize_array(numpy_array, threshold=200):
    #Binarize a numpy array.
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 0
            else:
                numpy_array[i][j] = 1
    return numpy_array

thresh_1 = binarize_array(np_im_B, threshold=85)
"""

#img, thresh = cv2.threshold(np_im_B, 0, 255, cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)

img1, thresh1 = cv2.threshold(np_im_B, 85, 255, cv2.THRESH_BINARY_INV)
print(img1, thresh1)

#thresh1[thresh1 <= 85] = 1
#thresh1[thresh1 > 85] = 0

#plt.axvline(img, color='r', linewidth=1)
#plt.show()

kernel = numpy.ones((40, 40), numpy.uint8)
dilation = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
#dilation1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1)))

print("shape_dilation after opening:", dilation.shape)
cimg = cv2.cvtColor(dilation, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(dilation, cv2.HOUGH_GRADIENT, 1, 200000, param1=50, param2=30, minRadius=0, maxRadius=0)
circles = numpy.uint16(numpy.around(circles))



for i in circles[0, :]:
    cv2.circle(dilation, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(dilation, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.subplot(121), plt.imshow(dilation, cmap='gray'), plt.axis('off')
#plt.subplot(122), plt.imshow(dilation), plt.axis('off')
#plt.show()
#plt.close()

#hausdorff distance

print(circles.shape)
print(cimg.shape)
print(dilation.shape)

dist = scipy.spatial.distance.directed_hausdorff(cimg[0], dilation)


"""=================================================================================================================="""
# 3rd step: find the pen contours







"""=================================================================================================================="""
# 4th step: apply a method to discard all the image which is not contained within that round contour

"""=================================================================================================================="""
# 5th step: apply a mask to that image and tile it at a specific magnification
# (use several possible magnifications to compare the results between them)

"""=================================================================================================================="""
# 6th step: put it in to the neural network :-)


