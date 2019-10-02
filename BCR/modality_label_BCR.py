import os
import pandas
import numpy


#csv_to_read = '/Volumes/Disk/labels_BCR.csv'
#df = pandas.read_csv(csv_to_read, delimiter=';', names=['name', 'label'])
#patients_list = df[['name']]
#labels_list = df[['label']]
df_con = pandas.DataFrame(columns=['name', 'label'])
df = []
for i in sorted(os.listdir('/Volumes/Disk/BCR/')):
    if '._' not in i:
        for j in sorted(os.listdir('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/')):
            if i == j:
                path_in = os.path.join('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/', j)
                for k in os.listdir(path_in):
                    if '._' not in k:
                        if k.endswith('.csv'):
                            csv = os.path.join(path_in, k)
                            df_new = pandas.read_csv(csv, delimiter=';;;', names=['name', 'label'])
                            index_0 = df_new[df_new['label'] == 0].index
                            index_2 = df_new[df_new['label'] == 2].index
                            df_new['label'].replace('', numpy.nan, inplace = True)
                            none = df_new['label'].isnull()
                            b = [i for i, x in enumerate(none) if x]
                            df_new.drop(index_0, inplace=True)
                            df_new.drop(index_2, inplace=True)
                            #df_new.dropna(subset=['label'], inplace=True)
                            df_new.drop(b, inplace=True)
                            df_con = pandas.concat([df_con, df_new['name']], axis=0)
final_dir = '/Volumes/Disk/BCR_MD_new_new.csv'
df_con.to_csv(final_dir, index=False, header=False)

