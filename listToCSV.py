import os
import shutil
import pandas

def get_images_list(main_dir):
    im_list = []
    for i in sorted(os.listdir(main_dir)):
        if '._' not in i:
            dir_in = os.path.join(main_dir, i)
            dir_in_in = os.path.join(dir_in, 'patches_256')
            for j in sorted(os.listdir(dir_in)):
                if '._' not in j:
                    if j.endswith('.png'):
                        im_list.append(j)
    return im_list


def list_to_csv(list, filename):
    df = pandas.DataFrame(list)
    df.to_csv(filename, index=False, header=False)
    csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', filename)
    shutil.move(csv, '/Volumes/Disk/')


def csv_to_list(filename):
    df = pandas.read_csv(filename, delimiter=';', names=['name', 'label'])
    list_names = df['name'].tolist()
    list_labels = df['label'].tolist()
    return list_names, list_labels

#images_list = get_images_list('/Volumes/Disk/TRAININGVALIDATION/G/')
#print(len(images_list))


list_nam, list_lab = csv_to_list('/Volumes/Disk/labels_BCR.csv')
#print(list_nam)
#print(len(list_nam))


def createFoldersFromList(dir, folders):
    dir_source = '/Volumes/Disk/ALL_IM/ANNOTADED_SLIDES_PAT/'
    for i in folders:
        for j in os.listdir(dir_source):
            if i == j[:8]:
                new_path = os.path.join(dir, j)
                try:
                    os.makedirs(new_path)
                    print("Directory ", new_path, " Created ")
                except FileExistsError:
                    print("Directory ", new_path, " already exists")

    return 'DONE'

list_to_csv(list_nam, '/Volumes/Disk/1.csv')
#createFoldersFromList('/Volumes/Disk/BCR/new/', list_nam)
#createFoldersFromList('/Volumes/Disk/BCR/TRAININGVALIDATION/', a)
#createFoldersFromList('/Volumes/Disk/BCR/TEST/', b)








