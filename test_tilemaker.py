import os
import shutil
import numpy
import skimage.measure
import cv2
import pandas
import matplotlib.pyplot as plt
import PIL
from PIL import Image



import tilemaker
#tilemaker.prepare('/Users/carolina/Desktop/14H00424_A11_new.tif', 'FFFFFF')
#tilemaker.main()
#os.system("python tilemaker.py -s256 -Q9 -t'15H03220_A10_x10_%d-%d_norm.png' -bFFFFFF -v /Volumes/Disk/untitled\ folder/15H03220_A10/15H03220_A10_x10_norm.tif")


def move_images_to_disk(dir_source, dir_dest):
    list_source_dir = os.listdir(dir_source)
    for indx in range(len(list_source_dir)):
        if list_source_dir[indx].endswith('.png'):
            shutil.move(dir_source + list_source_dir[indx], dir_dest)


# move_images_to_disk('/Users/carolina/PycharmProjects/PROJECT/', '/Volumes/Disk/CROPPED_SLIDES/14H00245_A11/x_10/patches_256/')

def delete_tiles(dir_tiles):
    listing = os.listdir(dir_tiles)

    dest1 = os.path.join(dir_tiles, 'non_tiles')

    try:
        os.mkdir(dest1)
        print("Directory ", dest1, " Created ")
    except FileExistsError:
        print("Directory ", dest1, " already exists")

    nun_array = []

    for i in range(len(listing)):
        img = cv2.imread(dir_tiles + listing[i])
        nun_im = numpy.asarray(img)
        if skimage.measure.shannon_entropy(nun_im) >= 5.6:
            nun_array.append(nun_im)
        else:
            shutil.move(dir_tiles + listing[i], dest1)

#delete_tiles('/Volumes/Disk/14H00124_A10_x10_norm/')


def create_csv(file_name, dir):
    list_files = os.listdir(dir)
    list_files = list(filter(lambda a: a != 'non_tiles', list_files))
    # list_files = list(filter(lambda a: a != '._', list_files))
    some_list = sorted(list_files, key=lambda s: (
        int(s[s.rfind('_') + 1:s.rfind('-')]), int(s[s.rfind('-') + 1:s.rfind('.')])))
    #df = pandas.DataFrame(some_list, columns=["colummn"])
    df = pandas.DataFrame(some_list)
    df.to_csv(file_name, index=False, header=False)
    csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', file_name)
    shutil.move(csv, dir)

#=================================================
"""
main_dir = '/Volumes/Disk/NORMALIZED/'
list_dir = os.listdir(main_dir)

for i in list_dir:
    folder = os.path.join(main_dir, i)
    im_folder = os.path.join(folder, 'x_10')
    im_name = sorted(os.listdir(im_folder))[1]

    dir_final = os.path.join(im_folder, 'patches_256')
    try:
        os.makedirs(dir_final)
        print("Directory ", dir_final, " Created ")
    except FileExistsError:
        print("Directory ", dir_final, " already exists")

    im_name_tile = im_name[:-4] + '_%d-%d.png'
    im_dir = os.path.join(im_folder, im_name)
    os.system(
        "python tilemaker.py -s256 -Q9 -t" + im_name_tile + " -bFFFFFF -v " + im_dir)

    move_images_to_disk('/Users/carolina/PycharmProjects/PROJECT/', dir_final)

    delete_tiles(dir_final + '/')

    #im_name_csv = im_name[:-4] + '.csv'
    #create_csv(im_name_csv, dir_final)

"""
#=================================================

def run_tilemaker_all(source_dir):
    list_source_dir = os.listdir(source_dir)
    for i in list_source_dir:
        dir_final = os.path.join(source_dir, i[:-4])
        if '._' not in i:
            try:
                os.makedirs(dir_final)
                print("Directory ", dir_final, " Created ")
            except FileExistsError:
                print("Directory ", dir_final, " already exists")

            im_name_tile = i[:-9] + '_%d-%d.png'
            im_dir = source_dir + i
            os.system(
                "python tilemaker.py -s256 -Q9 -t" + im_name_tile + " -bFFFFFF -v " + im_dir)

            move_images_to_disk('/Users/carolina/PycharmProjects/PROJECT/', dir_final)



#run_tilemaker_all('/Volumes/Disk/NORMALIZED/')




"""


patches_dir = '/Users/carolina/Desktop/folder/'
list_patches = os.listdir(patches_dir)
dest = '/Users/carolina/Desktop/folder/0/'
nun_array = []
for i in range(len(list_patches)):
    img = cv2.imread(patches_dir+list_patches[i])
    nun_im = numpy.asarray(img)
    img_bw = cv2.imread(patches_dir+list_patches[i], cv2.IMREAD_GRAYSCALE)
    nun_im_bw = numpy.asarray(img_bw)
    #plt.imshow(img, cmap='gray')
    #plt.show()
    n_white_pix = numpy.sum(img >= 200)
    size = img.size[0] * img.size[1]
    #print(skimage.measure.shannon_entropy(nun_im))
    if skimage.measure.shannon_entropy(nun_im) >= 5.6:

        #if 
        nun_array.append(nun_im)
    else:
        shutil.copy(patches_dir + list_patches[i], dest)



"""


"""
tile = Image.open('')
# A single tile is being read
#check the percentage of the image with "information". Should be above 50%
gray = tile.convert('L')
bw = gray.point(lambda x: 0 if x<220 else 1, 'F')
arr = numpy.array(numpy.asarray(bw))
avgBkg = numpy.average(bw)
bw = gray.point(lambda x: 0 if x<220 else 1, '1')
# check if the image is mostly background
if avgBkg <= (self._Bkg / 100):
    # if an Aperio selection was made, check if is within the selected region
    if PercentMasked >= (self._ROIpc / 100.0):
#if PercentMasked > 0.05:
        tile.save(outfile, quality=self._quality)
    #print("%s good: %f" %(outfile, avgBkg))
#elif level>5:
#    tile.save(outfile, quality=self._quality)
        #print("%s empty: %f" %(outfile, avgBkg))

"""

#CHECK THE EQUAL NUMBER OF SLIDES

def compare_patches(dir_source, dir_source_norm):
    list_source = os.listdir(dir_source)
    list_source_norm = os.listdir(dir_source_norm)
    dir_fin = os.path.join(dir_source_norm, 'tiles')
    try:
        os.makedirs(dir_fin)
        print("Directory ", dir_fin, " Created ")
    except FileExistsError:
        print("Directory ", dir_fin, " already exists")
    for i in list_source_norm:
        if '._' not in i:
            for j in list_source:
                if '._' not in j:
                    if i == j:
                        shutil.move(os.path.join(dir_source_norm,i), dir_fin)



def move_folders(dir_1):
    list_dir_1 = os.listdir(dir_1)
    for i in list_dir_1:
        list_dir_1_in = os.listdir(dir_1+ i)
        for j in list_dir_1_in:
            dir_to_move = os.path.join(dir_1 + i, j)
            shutil.move(dir_to_move, dir_1)
        if list_dir_1_in == []:
            os.rmdir(dir_1+ i)


def move_im(dir_source):
    list_source = os.listdir(dir_source)
    for i in list_source:
        if '._' not in i:
            dir_im = os.path.join(dir_source, i)
            dir_dest = os.path.join(dir_source, i[:-4])
            if i.endswith('.tif'):
                shutil.move(dir_im, dir_dest)

