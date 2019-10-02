import os
import pandas
import shutil
import cv2


modality_label = '/Volumes/Disk/NEW_BCR/modality_label.csv'

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
                    image = j
                    name = j.replace('-', '_')
                    name = name[:-4]
                    for k in sorted(df_list):
                        if '._' not in k:
                            if name == k:
                                number = i
                                dir_final_main = os.path.join('/Volumes/Disk/NEW_BCR/', number)
                                try:
                                    os.makedirs(dir_final_main)
                                    print("Directory ", dir_final_main, " Created ")
                                except FileExistsError:
                                    print("Directory ", dir_final_main, " already exists")
                                shutil.copy(os.path.join(images_dir, j), dir_final_main)

