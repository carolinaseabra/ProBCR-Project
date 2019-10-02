import os
import shutil
import numpy
import skimage.measure
import cv2
import pandas
import tilemaker


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
            shutil.move(dir_tiles + listing[i], dest1)


def create_csv(file_name, dir):
    list_files_dir = os.listdir(dir)
    df = pandas.DataFrame()
    for i in list_files_dir:
        dir_in = os.path.join(dir, i)
        dir_patches = dir_in + '/tiles'
        list_files = os.listdir(dir_patches)
    #list_files = list(filter(lambda a: a != 'non_tiles', list_files))
        some_list = sorted(list_files, key=lambda s: (
             int(s[s.rfind('_') + 1:s.rfind('-')]), int(s[s.rfind('-') + 1:s.rfind('.')])))
    #df = pandas.DataFrame(some_list, columns=["colummn"])
    #df = pandas.DataFrame(some_list)
        df1 = pandas.DataFrame(some_list)
        df = df.append(df1)
    df.to_csv(file_name, index=False, header=False)
    csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', file_name)
    shutil.move(csv, dir)

#create_csv('ALL_1.csv', '/Volumes/Disk/NORMALIZED/')


def get_labels(path_main):
    folder_names = os.listdir(path_main)
    df_new = pandas.DataFrame()
    for i in folder_names:
        folder_in = os.path.join(path_main, i)
        folder_in_list = os.listdir(folder_in)
        for j in folder_in_list:
            if '.' not in j:
                folder_in_in = os.path.join(folder_in, j)
                patches_path_list = os.listdir(folder_in_in)
                for k in patches_path_list:
                    if k.endswith('.csv'):
                        if not k.startswith('._'):
                            path_csv = os.path.join(folder_in_in, k)
                            df = pandas.read_csv(path_csv, delimiter= ';;;', names=['name', 'label'])
                            df_new = df_new.append(df)
    final_dir = 'ALL_labels_2.csv'
    df_new.to_csv(final_dir, index=False, header=False, sep=',')
    csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', final_dir)
    shutil.move(csv, '/Volumes/Disk/ALL_IM/CSVs/')

#get_labels('/Volumes/Disk/ANNOTADED_SLIDES_PAT/')








"""


dir_final = '/Volumes/Disk/CROPPED_SLIDES/16H01436_A3/x_10/patches_256/'

try:
    os.makedirs(dir_final)
    print("Directory ", dir_final, " Created ")
except FileExistsError:
    print("Directory ", dir_final, " already exists")

os.system("python tilemaker.py -s256 -Q9 -t'16H01436_A3_x10_i_%d-%d.png' -bFFFFFF -v /Volumes/Disk/CROPPED_SLIDES/16H01436_A3/x_10/16H01436_A3_x10_i.tif")

move_images_to_disk('/Users/carolina/PycharmProjects/PROJECT/',
                        dir_final)

delete_tiles(dir_final)

create_csv('16H01436_A3_x10.cvs', dir_final)
"""


def create_folders(name):

    the_list = os.listdir(name)
    for i in the_list:
        indx = i[:8]
        dir_final = os.path.join(name, indx)
        try:
            os.makedirs(dir_final)
            print("Directory ", dir_final, " Created ")
        except FileExistsError:
            print("Directory ", dir_final, " already exists")
        dir_mid = os.path.join(name, i)
        shutil.move(dir_mid, dir_final)


#create_folders('/Volumes/Disk/TO_DO/')



def move_stuff(path):
    path_list = os.listdir(path)
    dir_final = '/Volumes/Disk/SAMPLE_CROPP/'

    for i in path_list:
        path_in = os.path.join(path, i)
        list_new = os.listdir(path_in)

        for j in list_new:
            new_dir = os.path.join(dir_final, j)
            try:
                os.makedirs(new_dir)
                print("Directory ", new_dir, " Created ")
            except FileExistsError:
                print("Directory ", new_dir, " already exists")

            new_path = os.path.join(path_in, j)

            path_in_in_x30 = os.path.join(new_path, 'x_30')
            path_in_in_x40 = os.path.join(new_path, 'x_40')

            shutil.move(path_in_in_x30, new_dir)
            shutil.move(path_in_in_x40, new_dir)

#move_stuff('/Volumes/Disk/TO_DO/')


def move_more_stuff(path):

    path_list = os.listdir(path)
    for i in path_list:
        path_in = os.path.join(path, i)
        path_in_list = os.listdir(path_in)

        for j in path_in_list:
            path_in_nr = os.path.join(path_in, j)
            path_in_x10 = os.path.join(path_in_nr, 'x_10')
            path_in_x10_list = os.listdir(path_in_x10)
            new_list = []
            new_list.append(path_in_x10_list[0])
            new_list.append(path_in_x10_list[-1])
            for k in new_list:
                path_to_move = os.path.join(path_in_x10, k)
                shutil.move(path_to_move, path_in_nr)

            if os.listdir(path_in_x10) == []:
                os.rmdir(path_in_x10)

#move_more_stuff('/Volumes/Disk/TO_DO/')


def find_filenames(path_main, suffix):
    pandas_concatenated = pandas.DataFrame(columns=['name', 'label'])#columns=['image_name', 'tags']
    folder_names = sorted(os.listdir(path_main))
    for i in folder_names:
        if '._' not in i:
            folder_in = os.path.join(path_main, i)
            folder_in_list = os.listdir(folder_in)
            for j in folder_in_list:
                if '.' not in j:
                    folder_in_in = os.path.join(folder_in, j)
                    patches_path = folder_in_in
                    patches_path_list = os.listdir(patches_path)
                    for k in patches_path_list:
                        if k.endswith(suffix):
                            if not k.startswith('._'):
                                path_csv = os.path.join(patches_path, k)
                                df = pandas.read_csv(path_csv, delimiter= ';;;', names=['name', 'label'])
                                #col_1 = patches_path + '/' + df[['name']]
                                col_1 = df[['name']]
                                col_2 = df[['label']]
                                new_df_conc = pandas.concat([col_1, col_2], axis=1, join='inner')
                                pandas_concatenated = pandas.concat([pandas_concatenated, new_df_conc], axis=0, join='inner')
    final_dir = 'LABELS.csv'
    pandas_concatenated.to_csv(final_dir, index=False, header=False, sep=',')
    csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', final_dir)
    shutil.move(csv, '/Volumes/Disk/')

#find_filenames('/Volumes/Disk/ANNOTADED_SLIDES_PAT/', '.csv')




def move_non_tiles(path):
    path_list = os.listdir(path)
    dir_final = '/Volumes/Disk/ALL_IM/SAMPLE_CROPP/'

    for i in path_list:
        path_in = os.path.join(path, i)
        new_dir = os.path.join(dir_final + i[:8], i)
        path_non_tiles = os.path.join(path_in, 'patches_256/non_tiles')
        shutil.move(path_non_tiles, new_dir)

        #for j in list_new:
        #    new_dir = os.path.join(dir_final, i)
        #    new_dir_in = os.path.join(new_dir, j)
        #    new_path = os.path.join(path_in, j)
        #    path_non_tiles = os.path.join(new_path, 'patches_256/non_tiles')
        #    shutil.move(path_non_tiles, new_dir_in)


#move_non_tiles('/Volumes/Disk/untitled folder/')


def count_total_images(dir_source):
    list_source = os.listdir(dir_source)
    images_count = 0
    for i in list_source:
        dir_in = os.path.join(dir_source, i)
        list_dir_in = os.listdir(dir_in)
        images_count = images_count + len(list_dir_in)
    print(images_count)
    return images_count

#count_total_images('/Volumes/Disk/ANNOTADED_SLIDES_PAT/')





def copy_im_to_norm(dir_source):
    list_source = os.listdir(dir_source)
    for i in list_source:
        dir_in = os.path.join(dir_source, i)
        list_dir_in = os.listdir(dir_in)
        for j in list_dir_in:
            dir_in_in = os.path.join(dir_in, j)
            list_dir_in_in = os.listdir(dir_in_in)
            #print(list_dir_in_in)
            #print(sorted(list_dir_in_in))
            for k in list_dir_in_in:
                if k.endswith('.tif'):
                    shutil.copy(dir_in_in + '/' + k, '/Volumes/Disk/ALL_IM_TO_NORM')



#copy_im_to_norm('/Volumes/Disk/ANNOTADED_SLIDES_PAT/')




def del_non_norm_im (dir_source):
    list_source = os.listdir(dir_source)
    for i in list_source:
        if '._' not in i:
            if i.endswith('_norm.tif'):
                shutil.move(dir_source + i,  '/Volumes/Disk/untitled folder')

#del_non_norm_im('/Volumes/Disk/NORMALIZED/')
