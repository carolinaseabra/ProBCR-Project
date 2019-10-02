import os
import shutil


path_main = '/Volumes/Disk/SLIDES/'
images_list = os.listdir(path_main)
images_list_no_ext = []


for k in range(len(images_list)-1, -1, -1):
    new = os.path.splitext(images_list[k])
    images_list_no_ext.append(new[0])

#print(images_list_no_ext)

# Create a new directory
path_new = '/Volumes/Disk/SORTED_SLIDES/'
try:
    os.makedirs(path_new)
    print("Directory ", path_new, " Created ")
except FileExistsError:
    print("Directory ", path_new, " already exists")


#for indx in range(len(images_list_no_ext)-1, -1, -1):
#    path = os.path.join(path_new, images_list_no_ext[indx])
#    try:
#        os.mkdir(path)
#        print("Directory ", path, " Created ")
#    except FileExistsError:
#        print("Directory ", path, " Already exists")
        
folders_list = os.listdir(path_new)

for i in range(len(images_list)-1, -1, -1):
    for j in range(len(folders_list)-1, -1, -1):
        if str(images_list[i]) == str(folders_list[j] + '.svs'):
            path_to_file = os.path.join(path_new, folders_list[j])
            file_path = os.path.join(path_main, images_list[i])
            shutil.copy(file_path, path_to_file)



def create_folders_patients (list_fold, path):
    #list_fold = os.listdir('/Volumes/Disk/SORTED_SLIDES/')
    #path = '/Users/carolina/Desktop/CROPPED_SLIDES/'

    for indx in range(len(list_fold)-1, -1, -1):
        try:
            path_new = os.path.join(path, list_fold[indx])
            os.makedirs(path_new)
            print("Directory", path_new, "Created")
        except FileExistsError:
            print("Directory", path_new, "Already exists")



def create_folders_x_ampl (dir):
    #dir = '/Users/carolina/Desktop/CROPPED_SLIDES/'
    list_dir = os.listdir(dir)
    for indx in range (len(list_dir)-1, -1, -1):
        path_fold = dir + list_dir[indx]
        try:
            path_new = os.path.join(path_fold, 'x_40')
            os.mkdir(path_new)
            print("Directory", path_new, "Created")
        except FileExistsError:
            print("Directory", path_new, "Already exists")

