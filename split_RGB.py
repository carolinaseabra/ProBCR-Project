import os
import pandas
import numpy
import shutil
import cv2




#dir_images = '/Volumes/Disk/untitledfolder/'
dir_images = '/Volumes/Disk/NEW_BCR/'

for i in sorted(os.listdir(dir_images)):
    dir_in = os.path.join(dir_images, i)
#number = str(input('slide:'))
    number = i
    #dir_in_in = str(input('dir:'))
    #dir_in_in = os.path.join(dir_in, 'patches_256')
    #for j in sorted(os.listdir(dir_in_in)):
    for j in sorted(os.listdir(dir_in)):
        tile_dir = os.path.join(dir_in, j)
        if '._' not in j:
            if j.endswith('.png'):
                image = cv2.imread(tile_dir)
                nun_im = numpy.asarray(image)
                name = j
                index = name.find('-')
                name = name.replace('-', '_')
                #name_new = name + 'nii'
                dir_B_main = os.path.join('/Volumes/Disk/NEW_BCR/B/', number)
                dir_G_main = os.path.join('/Volumes/Disk/NEW_BCR/G/', number)
                dir_R_main = os.path.join('/Volumes/Disk/NEW_BCR/R/', number)
                try:
                    os.makedirs(dir_B_main)
                    print("Directory ", dir_B_main, " Created ")
                except FileExistsError:
                    print("Directory ", dir_B_main, " already exists")
                try:
                    os.makedirs(dir_G_main)
                    print("Directory ", dir_G_main, " Created ")
                except FileExistsError:
                    print("Directory ", dir_G_main, " already exists")
                try:
                    os.makedirs(dir_R_main)
                    print("Directory ", dir_R_main, " Created ")
                except FileExistsError:
                    print("Directory ", dir_R_main, " already exists")
                dir_B = os.path.join(dir_B_main, name)
                dir_G = os.path.join(dir_G_main, name)
                dir_R = os.path.join(dir_R_main, name)
                b, g, r = cv2.split(image)
                cv2.imwrite(dir_B, b)
                cv2.imwrite(dir_G, g)
                cv2.imwrite(dir_R, r)





"""

dir_in = str(input('dir:'))
for i in os.listdir(dir_in):
    image_dir = os.path.join(dir_in, i)
    if '._' not in i:
        if not i.endswith('.csv'):
            image = cv2.imread(image_dir)
            nun_im = numpy.asarray(image)
            new_name = i[:-4]
            #new_name_B = new_name + '.png'
            #new_name_G = new_name + '.png'
            index = new_name.find('-')
            new_name = new_name.replace('-', '_')
            new_name_R = new_name + '.png'
            #dir_B = os.path.join('/Volumes/Disk/B/', new_name_B)
            #dir_G = os.path.join('/Volumes/Disk/G/', new_name_G)
            dir_R = os.path.join('/Volumes/Disk/R/16H04020_A6/', new_name_R)
            (b, g, r) = cv2.split(image)
            #cv2.imwrite(dir_B, b)
            #cv2.imwrite(dir_G, g)
            cv2.imwrite(dir_R, r)
"""