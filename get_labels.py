import os
import shutil
import numpy
import pandas
import cv2
import skimage.measure
import tilemaker



def move_images_to_disk(dir_source, dir_dest):
    list_source_dir = os.listdir(dir_source)
    for indx in range(len(list_source_dir)):
        if list_source_dir[indx].endswith('.png'):
            shutil.move(dir_source + list_source_dir[indx], dir_dest)

"""

main_dir = '/Volumes/Disk/untitled folder/'
main_dir_list = os.listdir(main_dir)
for i in sorted(main_dir_list):
    if '._' not in i:
        slide_number = i
        dir_o = '/Volumes/Disk/untitled folder/' + slide_number
        o = os.listdir(dir_o)
        for j in o:
            if '._' not in j:
                if j.endswith('.tif'):
                    im_dir = os.path.join('/Volumes/Disk/untitled\ folder/' + slide_number, j)
        im_name_tile = slide_number + '_x10_%d-%d_norm.png'
        os.system(
            "python tilemaker.py -s256 -Q9 -t" + im_name_tile + " -bFFFFFF -v " + im_dir)

        #os.system('python tilemaker.py -s256 -Q9 -t "15H04409_C6_x10_%d-%d_norm.png" -bFFFFFF -v /Volumes/Disk/untitled\ folder/15H04409_C6/15H04409_C6_x10_norm.tif')
        move_images_to_disk('/Users/carolina/PycharmProjects/PROJECT/', dir_o)

        dir_t = '/Volumes/Disk/ANNOTADED_SLIDES_PAT/' + slide_number + '/patches_256/'
        t = os.listdir(dir_t)
        dir_final = '/Volumes/Disk/untitled folder/' + slide_number + '/patches_256/'
        try:
            os.makedirs(dir_final)
            print("Directory ", dir_final, " Created ")
        except FileExistsError:
            print("Directory ", dir_final, " already exists")

#dir_final = str(input('final_dir:'))
        for k in os.listdir(dir_o):
            if k.endswith('.png'):
                name_o = k[:-9]
                for y in t:
                    if y.endswith('.png'):
                        name_t = y[:-4]
                        if name_o == name_t:
                            shutil.move(os.path.join(dir_o, k), dir_final)
                            break

        o_new = os.listdir(dir_o)
        for a in o_new:
            if a.endswith('.png'):
                file_dir = os.path.join(dir_o, a)
                os.remove(file_dir)
#        dir_non = os.path.join(dir_final, 'non_tiles')
#        try:
#            os.makedirs(dir_non)
#            print("Directory ", dir_non, " Created ")
#        except FileExistsError:
#            print("Directory ", dir_non, " already exists")
#        non_im_dir = os.path.join(dir_o, k)
#        shutil.move(non_im_dir, dir_non)


"""


os.system("python tilemaker.py -s256 -Q9 -t'15H00616_A7_x10_ii_%d-%d_norm.png' -bFFFFFF -v /Volumes/Disk/NORM_IM_FINAL/15H00616_A7/15H00616_A7_x10_ii_norm.tif")
move_images_to_disk('/Users/carolina/PycharmProjects/PROJECT/', '/Volumes/Disk/NORM_IM_FINAL/15H00616_A7/')
dir_o = '/Volumes/Disk/NORM_IM_FINAL/15H00616_A7/'
o = os.listdir(dir_o)
dir_t = '/Volumes/Disk/ANNOTADED_SLIDES_PAT/15H00616_A7/patches_256/'
t = os.listdir(dir_t)
dir_final = '/Volumes/Disk/NORM_IM_FINAL/15H00616_A7/patches_256/'
for k in o:
    if k.endswith('.png'):
        name_o = k[:-9]
        for y in t:
            if y.endswith('.png'):
                name_t = y[:-4]
                if name_o == name_t:
                    shutil.move(os.path.join(dir_o, k), dir_final)
                    break
o_new = os.listdir(dir_o)
for a in o_new:
    if a.endswith('.png'):
        file_dir = os.path.join(dir_o, a)
        os.remove(file_dir)








"""
dir_csv = '/Volumes/Disk/untitled folder/rightNew.csv'
df = pandas.read_csv(dir_csv, delimiter=';;;', names=['name', 'label'])
df_new = df[['name', 'label']].copy()
filename = 'rightNew_1.csv'
df_new.to_csv('rightNew_1.csv', index=False, header=False)
csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', filename)
shutil.move(csv, '/Volumes/Disk/')

"""





