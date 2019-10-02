import py_wsi
import numpy
import openslide
import py_wsi.imagepy_toolkit as tk
import os
import PIL
from PIL import Image, ImageFile
import matplotlib.pyplot as plt
import cv2


"""
file_dir = "/Users/carolina/Desktop/project/"
db_location = "/Users/carolina/Desktop/project/data/"
xml_dir = file_dir
patch_size = 64
level = 10
db_name = "patch_db"
overlap = 0

label_map = {'Normal': 0,
             'Benign': 1,
             'Carcinoma in situ': 2,
             'In situ carcinoma': 2,
             'Carcinoma invasive': 3,
             'Invasive carcinoma': 3,}

turtle = py_wsi.Turtle(file_dir, db_location, db_name, xml_dir, label_map)

print("Total WSI images:    " + str(turtle.num_files))
print("LMDB name:           " + str(turtle.db_name))
print("File names:          " + str(turtle.files))
print("XML files found:     " + str(turtle.get_xml_files()))

print(turtle.num_files)

level_count, level_tiles, level_dims = turtle.retrieve_tile_dimensions('imagem1.svs', patch_size=64)
print("Level count:         " + str(level_count))
print("Level tiles:         " + str(level_tiles))
print("Level dimensions:    " + str(level_dims))

# Fetches a sample patch from the centre of a whole slide image for testing.
patch_1 = turtle.retrieve_sample_patch('imagem1.svs', 256, 12, overlap=0)
patch_2 = turtle.retrieve_sample_patch("imagem1.svs", 128, 12, overlap=0)
patch_3 = turtle.retrieve_sample_patch("imagem1.svs", 64, 12, overlap=0)

patch_1.save("/Users/carolina/Desktop/project/out.jpg", "JPEG")
np_im = numpy.array(patch_1)
print(np_im.shape)
patch_1_red = np_im[:, :, 0]
patch_1_green = np_im[:, :, 1]
patch_1_blue = np_im[:, :, 2]

#plt.hist(patch_1_blue.flatten(), bins=100)
#plt.show()
#print("passed patch_1")

tk.show_images([patch_1, patch_2, patch_3], 3, 1)

load com o SITK
get array from image
otsu threshold
get threshold
hough transform (identificar a zona dentro da caneta)
"""

#image = Image.open('/Users/carolina/Desktop/project/imagem1.png')

#print(image_png.level_count)
#print(image_png.level_dimensions)
#print(image.shape)
#print(image_png.level_downsamples)

image_cv2 = cv2.imread('/Users/carolina/Desktop/project/imagem1.png')
image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
#plt.imshow(image_cv2)
plt.show()

array = numpy.asarray(image_cv2)
array_B = array[:, :, 0]
array_G = array[:, :, 1]
array_R = array[:, :, 2]
"""
plt.hist(array_B.flatten(), bins=100)
plt.hist(array_R.flatten(), bins=100)
plt.hist(array_G.flatten(), bins=100)
plt.show()
"""
color = ('r', 'g', 'b')
for i, col in enumerate(color):
    histr = cv2.calcHist([image_cv2], [i], None, [256], [0, 256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.show()















