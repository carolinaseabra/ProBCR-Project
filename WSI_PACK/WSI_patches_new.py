import cv2
import numpy
import matplotlib.pyplot as plt
import py_wsi
import py_wsi.imagepy_toolkit as tk
from multiprocessing import Pool
import os
import skimage.measure
import shutil



# SET THE PARAMETERS FOR FILE DIRECTORY

file_dir = '/Volumes/Disk/SORTED_SLIDES/14H00124_A10/'
db_location = '/Volumes/Disk/PATCHES/'
#db_location = ''
xml_dir = file_dir
db_name = 'patch_db'

#label_map = {'Normal': 0,
#             'Benign': 1,
#             'Carcinoma in situ': 2,
#             'In situ carcinoma': 2,
#             'Carcinoma invasive': 3,
#             'Invasive carcinoma': 3,
#            }

# TURTLE MANAGER OBJECT

turtle = py_wsi.Turtle(file_dir, db_location, db_name=db_name, storage_type='disk', xml_dir=xml_dir, label_map=None)

#for indx in range(len(turtle.files)-1, -1, -1):
#    if "._" in turtle.files[indx]:
#        turtle.files = numpy.delete(turtle.files, indx)


print("Total WSI images:    " + str(turtle.num_files))
print("LMDB name:           " + str(turtle.db_name))
print("File names:          " + str(turtle.files))

#print(len(turtle.files))

level_count, level_tiles, level_dims = turtle.retrieve_tile_dimensions(turtle.files, patch_size = 128)
print("Level count:         " + str(level_count))
print("Level tiles:         " + str(level_tiles))
print("Level dimensions:    " + str(level_dims))



patch_size = 128
#8256#129#2048
overlap = 0
level = 14

#turtle.sample_and_store_patches(patch_size, level, overlap, load_xml=False, limit_bounds=True)

#patches, coords, classes, labels = turtle.get_patches_from_file('14H00210_A8.svs', verbose=True)





#print(len(patches))
#print(coords)
#print(classes)


"""
# After storing the patches in a folder, discard the ones
# that do not contain relevant information

patches_location = '/Users/carolina/Desktop/project/TILES/'

listing = os.listdir(patches_location)

dest1 = '/Users/carolina/Desktop/NON_TILES'


nun_array = []
for i in range(len(listing)):
    nun_im = numpy.asarray(cv2.imread(patches_location+listing[i]))
    print(skimage.measure.shannon_entropy(nun_im))
    if skimage.measure.shannon_entropy(nun_im) >= 5.5:
        nun_array.append(nun_im)
    else:
        shutil.copy(patches_location + listing[i], dest1)

print(nun_array)

listing_non = os.listdir(dest1)
print(len(listing_non))

#numpy_array = numpy.asarray(cv2.imread(dest1+listing[0]))

#thresh = 200
#super_threshold_indices = numpy_array > thresh
#numpy_array[super_threshold_indices] = 0

"""