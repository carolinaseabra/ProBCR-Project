import pandas
import os

csv = '/Volumes/Disk/BCR/TRAININGVALIDATION/modality_label.csv'
df_new = pandas.read_csv(csv, delimiter=',', names=['name', 'label'])

index_0 = df_new[df_new['label'] == 0].index
index_1 = df_new[df_new['label'] == 1].index
#df_new['label'].replace('', numpy.nan, inplace = True)
#none = df_new['label'].isnull()
#b = [i for i, x in enumerate(none) if x]
df_new.drop(index_1, inplace=True)
#df_new.drop(index_1, inplace=True)
#df_new.dropna(subset=['label'], inplace=True)
#df_new.drop(b, inplace=True)

df_new.to_csv('/Users/carolina/Desktop/0.csv', index=False, header=False)