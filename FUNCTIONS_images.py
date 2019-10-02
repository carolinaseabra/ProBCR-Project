import os
import shutil
import numpy
import pandas
import cv2
import skimage.measure


# GERAR PATCHES A PARTIR DAS IMAGENS NORMALIZADAS

#images_list = os.listdir('')
#name = images_list[0]
#name_tile = im_name[:-4] + '_%d-%d.png'

#os.system(
#        "python tilemaker.py -s256 -Q9 -t" + name_tile + " -bFFFFFF -v " + im_dir)
"""
a = {'ola', 'hello', 'adeus', 'bye', 'boat'}
b = {'ola', 'hello', 'adeus', 'bye', 'morning', 'car'}
print(a.symmetric_difference(b))

print(set(['ola', 'hello', 'adeus', 'bye', 'boat']))
"""
def move_images_to_disk(dir_source, dir_dest):
    list_source_dir = os.listdir(dir_source)
    for indx in range(len(list_source_dir)):
        if list_source_dir[indx].endswith('.png'):
            shutil.move(dir_source + list_source_dir[indx], dir_dest)

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
            shutil.move(dir_tiles + '/' + listing[i], dest1)

"""

norm_im = os.listdir('/Volumes/Disk/NORM_IM/')
for i in norm_im:
    name = i[:-13]
    dir_final = '/Volumes/Disk/NORMALIZED/' + name
    im_dir = os.path.join('/Volumes/Disk/NORM_IM/', i)
    im_name_tile = i[:-9] + '_%d-%d_norm.png'
    os.system(
        "python tilemaker.py -s256 -Q9 -t" + im_name_tile + " -bFFFFFF -v " + im_dir)
    try:
        os.makedirs(dir_final)
        print("Directory ", dir_final, " Created ")
    except FileExistsError:
        print("Directory ", dir_final, " already exists")
    move_images_to_disk('/Users/carolina/PycharmProjects/PROJECT/', dir_final)

    delete_tiles(dir_final)

"""


"""
tiles_norm = '/Volumes/Disk/NORMALIZED/14H00124_A10/'
non_tiles_norm = '/Volumes/Disk/NORMALIZED/14H00124_A10/non_tiles/'

tiles = '/Volumes/Disk/ANNOTADED_SLIDES_PAT/14H00124_A10/patches_256/'
#non_tiles = '/Volumes/Disk/ANNOTADED_SLIDES_PAT/14H00124_A10/patches_256/non_tiles'


tiles_norm_list = os.listdir(tiles_norm)
non_tiles_norm_list = set(os.listdir(non_tiles_norm))

tiles_list = set(os.listdir(tiles))
#non_tiles_list = set(os.listdir(non_tiles))
tiles_norm_new_list = []
for i in tiles_norm_list:
    if i.endswith('.png'):
        tiles_norm_new_list.append(i[:-9] + '.png')
tiles_norm_list = set(tiles_norm_new_list)

differences = tiles_norm_list.difference(tiles_list)
differences = list(differences)
df = pandas.DataFrame(differences)
df.to_csv('differences.csv', index=False, header=False)
csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', 'differences.csv')
shutil.move(csv, '/Volumes/Disk/')


df = pandas.read_csv('/Volumes/Disk/ANNOTADED_SLIDES_PAT/14H00286_A19/patches_256/14H00286_A19_x10.csv', delimiter= ';;;', names=['name', 'label'])
col_1 = df[['name']]
list_a = list(col_1)
dir_b = '/Volumes/Disk/NORMALIZED/14H00286_A19/'
list_b = os.listdir(dir_b)
list_b_new = []
for i in list_b:
    if i.endswith('.png'):
        list_b_new.append(i[:-9] + '.png')
    list_b = set(list_b_new)
    list_a = set(list_a)

list_to_csv(list_b, 'list_b.csv')
differences = list_b.difference(list_a)
print(differences)


"""

def list_to_csv(list, filename):
    df = pandas.DataFrame(list)
    df.to_csv(filename, index=False, header=False)
    csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', filename)
    shutil.move(csv, '/Volumes/Disk/')

#list_to_csv(os.listdir('/Volumes/Disk/ANNOTADED_SLIDES_PAT/14H00442_A5/patches_256/'), 'od.csv')

def difference_operation(dir_a, dir_b, operation, filename):
    list_a = os.listdir(dir_a)
    list_b = os.listdir(dir_b)

    list_a_new = []
    for i in list_a:
        if i.endswith('.png'):
            list_a_new.append(i[:-9] + '.png')
    list_a = set(list_a_new)
    list_b = set(list_b)

    if operation == 'AB':
        differences = list_a.difference(list_b)
    else:
        differences = list_b.difference(list_a)

    differences = sorted(list(differences))
    list_to_csv(differences, filename)


def move_files(dir_source):
    list_source = os.listdir(dir_source)
    dir_final = os.path.dirname(dir_source)
    for i in list_source:
        dir_im = os.path.join(dir_source, i)
        shutil.move(dir_im, dir_final)

#move_files('/Volumes/Disk/NORMALIZED/15H01281_C16/non_tiles')
#delete_tiles('/Volumes/Disk/NORMALIZED/15H01281_C16/')
#difference_operation('/Volumes/Disk/NORMALIZED/15H01281_C16/', '/Volumes/Disk/ANNOTADED_SLIDES_PAT/15H01281_C16/patches_256/', 'AB', '15H01281_C16.csv')

#difference_operation('/Volumes/Disk/NORMALIZED/15H02244_9/', '/Volumes/Disk/ANNOTADED_SLIDES_PAT/15H02244_9/patches_256/', 'BA', '15H02244_9_1.csv')
#list_to_csv(os.listdir('/Volumes/Disk/NORMALIZED/15H01422_5/'), '15H01422_5_1.csv')
