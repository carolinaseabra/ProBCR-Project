import os
import pandas
import shutil



def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

#list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]

dir_csv = '/Volumes/Disk/BCR/TEST/modality_label_test.csv'
df = pandas.read_csv(dir_csv, delimiter=',', names=['name', 'label'])
col1 = df[['name']]
print(len(col1))
col_1 = list(df['name'])
print(len(col1))
df_list = []
for i in sorted(os.listdir('/Volumes/Disk/BCR/TEST/R/')):
    print(i)
    if '._' not in i:
        for j in col_1:
            if '._' not in j:
                print(j)
                indx = list(find_all(j, '_'))[1]
                name = j[:indx]
                if i == name:
                    path = '/mnt/disk/BCR/TEST/R/' + i + '/' + j + '.nii'
                    print(path)
                    df_list.append(path)
print(len(df_list))
new_df = pandas.DataFrame(df_list)
new = df[['name']].copy()
new_df_conc = pandas.concat([new, new_df], axis=1, join='inner')
filename = 'R_path_file.csv'
new_df_conc.to_csv(filename, index=False, header=False)
csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', filename)
shutil.move(csv, '/Volumes/Disk/')