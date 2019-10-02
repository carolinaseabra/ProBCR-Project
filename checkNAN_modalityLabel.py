import pandas
import os
import cv2
import numpy
path_csv = '/Volumes/Disk/ALL_IM/CSVs/MODALITY_ALL.csv'
df = pandas.read_csv(path_csv, delimiter=',', names=['name', 'label'])
#print(df.size)
#print(df.shape)
a = df['label'].isnull()
b = [i for i, x in enumerate(a) if x]
ln = len(b)
print(ln)
print(b)

#df.to_csv('/Volumes/Disk/TRAININGVALIDATION/CROSS_FOLD_5_new.csv', index=False, header=False)











