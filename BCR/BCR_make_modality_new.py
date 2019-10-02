import os
import pandas
import numpy

"""
csv_to_read = '/Volumes/Disk/NEW_BCR/class_1_BCR.csv'
df_to_read = pandas.read_csv(csv_to_read, names=['name'])
df_list_read = df_to_read['name'].tolist()

df_con = pandas.DataFrame(columns=['name', 'label'])
df = []

for i in sorted(df_list_read):
        for j in sorted(os.listdir('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/')):
            if i == j[:8]:
                path_in = os.path.join('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/', j)
                for k in os.listdir(path_in):
                    if '._' not in k:
                        if k.endswith('.csv'):
                            csv = os.path.join(path_in, k)
                            df_new = pandas.read_csv(csv, delimiter=';;;', names=['name', 'label'])
                            index_0 = df_new[df_new['label'] == 0].index
                            index_2 = df_new[df_new['label'] == 2].index
                            df_new['label'].replace('', numpy.nan, inplace=True)
                            none = df_new['label'].isnull()
                            b = [i for i, x in enumerate(none) if x]
                            print(df_new.iloc[b])
                            df_new.drop(index_0, inplace=True)
                            df_new.drop(index_2, inplace=True)
                            #df_new.dropna(subset=['label'], inplace=True)
                            #df_new.drop(b, inplace=True)
                            df_con = pandas.concat([df_con, df_new['name']], axis=0)
final_dir = '/Volumes/Disk/class_1_BCR_modality_label.csv'
df_con.to_csv(final_dir, index=False, header=False)
"""


df_0 = pandas.read_csv('/Volumes/Disk/NEW_BCR/class_0_BCR_modality_label.csv', sep=',', names=['name', 'label'])
df_1 = pandas.read_csv('/Volumes/Disk/NEW_BCR/class_1_BCR_modality_label.csv', sep=',', names=['name', 'label'])

df_con = pandas.concat([df_0, df_1], axis=0)
final_dir = '/Volumes/Disk/modality_label.csv'
df_con.to_csv(final_dir, index=False, header=False)
