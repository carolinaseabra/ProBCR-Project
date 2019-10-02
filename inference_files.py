import pandas
import numpy


#file = '/Users/carolina/Desktop/output_files/NORM_NEW/model5/_niftynet_out.csv'
file = '/Users/carolina/Desktop/output_files/BCR/TEST/_niftynet_out_prob.csv'
df = pandas.read_csv(file, delimiter=',', names=['name', 'label_0', 'label_1'])#, 'label_2'])
#df = pandas.read_csv(file, delimiter=',', names=['name', 'label'])
print(df.head())
print(df.tail())

df.drop_duplicates('name', inplace=True)

#df.to_csv('/Users/carolina/Desktop/output_files/NORM_NEW/model5/inference_model5.csv', index=False, header=False)
df.to_csv('/Users/carolina/Desktop/output_files/BCR/TEST/inferred_bcr_test_prob.csv', index=False, header=False)

print(df)

"""
file = '/Volumes/Disk/cross_fold_5.csv'
df = pandas.read_csv(file, delimiter=';;;', names=['name', 'label'])
df.to_csv('/Volumes/Disk/NEW_BCR/cross_fold_5.csv', index=False, header=False)
"""