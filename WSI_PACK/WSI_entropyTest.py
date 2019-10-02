import cv2
import numpy
import matplotlib.pyplot as plt
import py_wsi
import py_wsi.imagepy_toolkit as tk
from multiprocessing import Pool
import os
import skimage.measure

# SET THE PARAMETERS FOR FILE DIRECTORY

file_dir = '/Users/carolina/Desktop/project/'
db_location = '/Users/carolina/Desktop/project/TILES/'
xml_dir = file_dir
db_name = 'patch_db'

label_map = {'Normal': 0,
             'Benign': 1,
             'Carcinoma in situ': 2,
             'In situ carcinoma': 2,
             'Carcinoma invasive': 3,
             'Invasive carcinoma': 3,
            }

# TURTLE MANAGER OBJECT

turtle = py_wsi.Turtle(file_dir, db_location, db_name=db_name, storage_type='disk', xml_dir=xml_dir, label_map=label_map)


#turtle = py_wsi.Turtle(file_dir, db_location, db_name)

print("Total WSI images:    " + str(turtle.num_files))
print("LMDB name:           " + str(turtle.db_name))
print("File names:          " + str(turtle.files))


level_count, level_tiles, level_dims = turtle.retrieve_tile_dimensions(turtle.files[0], patch_size = 128)
print("Level count:         " + str(level_count))
print("Level tiles:         " + str(level_tiles))
print("Level dimensions:    " + str(level_dims))

patch_size = 128#8256#129#2048
overlap = 0
level = 7

patch_3 = turtle.retrieve_sample_patch('imagem1.svs', patch_size, level*2, overlap=overlap)

#tk.show_images([patch_3], 1, 1)

patch_size = 64
level = 10
overlap = 0

print("Patch size:", patch_size)
turtle.sample_and_store_patches(patch_size, level, overlap, load_xml=False, limit_bounds=True)

patches, coords, classes, labels = turtle.get_patches_from_file('imagem1.svs', verbose=True)

print(len(patches))
print(coords)
print(classes)

#tk.show_labeled_patches(patches[:10], coords[:10])

patch_size = 8256#129#2048
overlap = 0
level = 7

#patch_1 = turtle.retrieve_sample_patch('imagem1.svs', patch_size, level, overlap=overlap)
#patch_2 = turtle.retrieve_sample_patch('imagem1.svs', patch_size, level*1, overlap=overlap)
#patch_3 = turtle.retrieve_sample_patch('imagem1.svs', patch_size, level*2, overlap=overlap)

#tk.show_images([patch_1, patch_2, patch_3], 3, 1)

#turtle.sample_and_store_patches(patch_size, level, overlap, load_xml=False, limit_bounds=True)

# From database
turtle = py_wsi.Turtle(file_dir, db_location, db_name,  storage_type='disk')




# After storing the patches in a folder, discard the ones
# that do not contain relevant information

listing = os.listdir(db_location)

entropy_matrix = []
matrix_im = [] #[numpy.asarray(cv2.imread(x)) for x in listing]

#for i in range(len(listing)):
#    im = os.path.join("/Users/carolina/Desktop/project/TILES/", listing[i])
#    nun_im = numpy.asarray(cv2.imread(im))
#    matrix_im.append(nun_im)
#    entropy = skimage.measure.shannon_entropy(nun_im)
#    entropy_matrix.append(entropy)


#"""
im_1 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/imagem1_0_1_.png"))
im_2 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/imagem1_0_0_.png"))
im_3 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/imagem1_1_2_.png"))
im_4 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/imagem1_1_4_.png"))
im_5 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/IMAGEMDIGITAL_2_5_.png"))
im_6 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/IMAGEMDIGITAL_5_10_.png"))
im_7 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/IMAGEMDIGITAL_6_3_.png"))
im_8 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/IMAGEMDIGITAL_7_11_.png"))
im_9 = numpy.asarray(cv2.imread("/Users/carolina/Desktop/project/TILES/IMAGEMDIGITAL_12_8_.png"))



entropy_1_R = skimage.measure.shannon_entropy(im_1[:, :, 0])
entropy_1_G = skimage.measure.shannon_entropy(im_1[:, :, 1])
entropy_1_B = skimage.measure.shannon_entropy(im_1[:, :, 2])
entropy_1 = skimage.measure.shannon_entropy(im_1)

entropy_2_R = skimage.measure.shannon_entropy(im_2[:, :, 0])
entropy_2_G = skimage.measure.shannon_entropy(im_2[:, :, 1])
entropy_2_B = skimage.measure.shannon_entropy(im_2[:, :, 2])
entropy_2 = skimage.measure.shannon_entropy(im_2)

entropy_3_R = skimage.measure.shannon_entropy(im_3[:, :, 0])
entropy_3_G = skimage.measure.shannon_entropy(im_3[:, :, 1])
entropy_3_B = skimage.measure.shannon_entropy(im_3[:, :, 2])
entropy_3 = skimage.measure.shannon_entropy(im_3)

entropy_4_R = skimage.measure.shannon_entropy(im_4[:, :, 0])
entropy_4_G = skimage.measure.shannon_entropy(im_4[:, :, 1])
entropy_4_B = skimage.measure.shannon_entropy(im_4[:, :, 2])
entropy_4 = skimage.measure.shannon_entropy(im_4)

entropy_5_R = skimage.measure.shannon_entropy(im_5[:, :, 0])
entropy_5_G = skimage.measure.shannon_entropy(im_5[:, :, 1])
entropy_5_B = skimage.measure.shannon_entropy(im_5[:, :, 2])
entropy_5 = skimage.measure.shannon_entropy(im_5)

entropy_6_R = skimage.measure.shannon_entropy(im_6[:, :, 0])
entropy_6_G = skimage.measure.shannon_entropy(im_6[:, :, 1])
entropy_6_B = skimage.measure.shannon_entropy(im_6[:, :, 2])
entropy_6 = skimage.measure.shannon_entropy(im_6)

entropy_7_R = skimage.measure.shannon_entropy(im_7[:, :, 0])
entropy_7_G = skimage.measure.shannon_entropy(im_7[:, :, 1])
entropy_7_B = skimage.measure.shannon_entropy(im_7[:, :, 2])
entropy_7 = skimage.measure.shannon_entropy(im_7)

entropy_8_R = skimage.measure.shannon_entropy(im_8[:, :, 0])
entropy_8_G = skimage.measure.shannon_entropy(im_8[:, :, 1])
entropy_8_B = skimage.measure.shannon_entropy(im_8[:, :, 2])
entropy_8 = skimage.measure.shannon_entropy(im_8)

entropy_9_R = skimage.measure.shannon_entropy(im_9[:, :, 0])
entropy_9_G = skimage.measure.shannon_entropy(im_9[:, :, 1])
entropy_9_B = skimage.measure.shannon_entropy(im_9[:, :, 2])
entropy_9 = skimage.measure.shannon_entropy(im_9)

print(entropy_1_R, entropy_1_G, entropy_1_B, entropy_1)
print(entropy_2_R, entropy_2_G, entropy_2_B, entropy_2)
print(entropy_3_R, entropy_3_G, entropy_3_B, entropy_3)
print(entropy_4_R, entropy_4_G, entropy_4_B, entropy_4)
print(entropy_5_R, entropy_5_G, entropy_5_B, entropy_5)
print(entropy_6_R, entropy_6_G, entropy_6_B, entropy_6)
print(entropy_7_R, entropy_7_G, entropy_7_B, entropy_7)
print(entropy_8_R, entropy_8_G, entropy_8_B, entropy_8)
print(entropy_9_R, entropy_9_G, entropy_9_B, entropy_9)



entropy_2 = skimage.measure.shannon_entropy(im_2)
entropy_3 = skimage.measure.shannon_entropy(im_3)
entropy_4 = skimage.measure.shannon_entropy(im_4)
entropy_5 = skimage.measure.shannon_entropy(im_5)
entropy_6 = skimage.measure.shannon_entropy(im_6)
entropy_7 = skimage.measure.shannon_entropy(im_7)
entropy_8 = skimage.measure.shannon_entropy(im_8)
entropy_9 = skimage.measure.shannon_entropy(im_9)

#entropy_matrix = [entropy_1, entropy_2, entropy_3, entropy_4, entropy_5,
                  #entropy_6, entropy_7, entropy_8, entropy_9]

#print(entropy_matrix)

plt.subplot(331), plt.imshow(im_1), plt.title(entropy_1)
plt.subplot(332), plt.imshow(im_2), plt.title(entropy_2)
plt.subplot(333), plt.imshow(im_3), plt.title(entropy_3)
plt.subplot(334), plt.imshow(im_4), plt.title(entropy_4)
plt.subplot(335), plt.imshow(im_5), plt.title(entropy_5)
plt.subplot(336), plt.imshow(im_6), plt.title(entropy_6)
plt.subplot(337), plt.imshow(im_7), plt.title(entropy_7)
plt.subplot(338), plt.imshow(im_8), plt.title(entropy_8)
plt.subplot(339), plt.imshow(im_9), plt.title(entropy_9)


plt.show()


#"""