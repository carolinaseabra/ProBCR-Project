import pandas
import os
import shutil
import numpy


n = 60
n_train = 50
n_val = 10
n_test = 10

def getSubjectID (source_dir):
    slides_list = os.listdir(source_dir)
    patients_list = []
    for i in slides_list:
        if i[:8] not in patients_list:
            patients_list.append(i[:8])
    return patients_list

patients_list = getSubjectID('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/')
training_set = ['14H00424', '14H00525', '14H01117', '14H01127', '14H01230', '14H01357', '14H01738', '14H02050', '14H02577', '14H02579', '14H02580', '14H02581', '14H02723', '14H02994', '14H02995', '14H02996', '14H02997', '14H03136', '14H03428', '14H03450', '14H03451', '14H03452', '14H03609', '14H03758', '14H03762', '14H03763', '15H00312', '15H00313', '15H00314', '15H00315', '15H00616', '15H00934', '15H01205', '15H01206', '15H01207', '15H01249', '15H01277', '15H01279', '16H03919', '16H03981']
validation_set = ['14H00151', '14H00210', '14H00241', '14H00245', '15H04337', '15H04381', '15H04409','16H02480', '16H02947', '16H02953']
test_set = ['16H04861', '16H04913', '16H04979', '16H05038', '17H00646', '17H01148', '17H01170', '17H01752', '17H01780', '17H01833']

def CSV_list(list_set):
    df_final = pandas.DataFrame(columns=['name', 'label'])
    for i in test_set:
        for j in os.listdir('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/'):
            if '._' not in j:
                if i == j[:8]:
                    path_patches = os.path.join('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/', j)
                    #path_in = os.path.join(path_patches, 'patches_256')
                    for k in os.listdir(path_patches):
                        if '._' not in k:
                            if k.endswith('.csv'):
                                path_csv = os.path.join(path_patches, k)
                                df = pandas.read_csv(path_csv, delimiter=';;;', names=['name', 'label'])
                                df_final = pandas.concat([df_final, df], axis=0)
    final_dir = '/Volumes/Disk/NIKOS/TEST.csv'
    df_final.to_csv(final_dir, index=False, header=False)

csv_training = '/Volumes/Disk/NIKOS/TRAIN.csv'
csv_validation = '/Volumes/Disk/NIKOS/VALID.csv'
csv_test = '/Volumes/Disk/NIKOS/TEST.csv'


def ReadAndReturnCSV(csv_path):
    df = pandas.read_csv(csv_path, delimiter=',', names=['name', 'label'])
    index_0 = df[df['label'] == 0].index
    index_1 = df[df['label'] == 1].index
    index_2 = df[df['label'] == 2].index
    df.drop(index_0, inplace=True)
    df.drop(index_1, inplace=True)
    df.drop(index_2, inplace=True)
    final_dir = '/Volumes/Disk/NIKOS/VALI_2.csv'
    df.to_csv(final_dir, index=False, header=False)


def DropNone(csv_path):
    df = pandas.read_csv(csv_path, delimiter=',', names=['name', 'label'])
    df['label'].replace('', numpy.nan, inplace=True)
    none = df['label'].isnull()
    b = [i for i, x in enumerate(none) if x]
    df.drop(b, inplace=True)
    final_dir = '/Volumes/Disk/NIKOS/TRAIN0.csv'
    df.to_csv(final_dir, index=False, header=False)


modality_label = '/Volumes/Disk/NIKOS/VALI_0.csv'
df = pandas.read_csv(modality_label, delimiter=',', names=['name', 'label'])
df_list = df['name'].tolist()
main_dir = '/Volumes/Disk/ALL_IM/NORM_IM_FINAL/'

for i in sorted(os.listdir(main_dir)):
    if'._' not in i:
        main_dir_in = os.path.join(main_dir, i)
        images_dir = os.path.join(main_dir_in, 'patches_256')
        for j in sorted(os.listdir(images_dir)):
            if '._' not in j:
                if j.endswith('.png'):
                    name = j.replace('-', '_')
                    for k in sorted(df_list):
                        if '._' not in k:
                            if name == k:
                                dir_final_0 = '/Volumes/Disk/NIKOS/VALIDATION/0/'
                                shutil.copy(os.path.join(images_dir, j), dir_final_0)
