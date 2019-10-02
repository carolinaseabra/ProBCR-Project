import os
import pandas
import shutil


def modality_label_maker(path_main):
    pandas_concatenated = pandas.DataFrame(columns=['name', 'label'])#columns=['image_name', 'tags']
    folder_names = sorted(os.listdir(path_main))
    for i in folder_names:
        if '._' not in i:
            folder_in = os.path.join(path_main, i)
            folder_in_list = os.listdir(folder_in)
            #for j in folder_in_list:
            #    if '.' not in j:
            #        folder_in_in = os.path.join(folder_in, j)
            #        patches_path = folder_in_in
            #        patches_path_list = os.listdir(patches_path)
            #for k in patches_path_list:
            for k in folder_in_list:
                if not k.startswith('._'):
                    if k.endswith('.csv'):
                        #path_csv = os.path.join(patches_path, k)
                        path_csv = os.path.join(folder_in, k)
                        df = pandas.read_csv(path_csv, delimiter=';;;', names=['name', 'label'])
                        #col_1 = patches_path + '/' + df[['name']]

                        #new_df_conc = pandas.concat(col_1)
                        pandas_concatenated = pandas.concat([pandas_concatenated, df], axis=0)

    final_dir = '/Volumes/Disk/Labels.csv'
    pandas_concatenated.to_csv(final_dir, index=False, header=False)


modality_label_maker('/Volumes/Disk/NORM_IM_FINAL/')
