import os
import pandas
import shutil
import random

modality_label = '/Volumes/Disk/BCR/TEST/modality_label_test.csv'

#modality_label = '/Volumes/Disk/BCR/TRAININGVALIDATION/modality_label.csv'

def ReadAndReturnCSV(csv_path):
    df = pandas.read_csv(csv_path, delimiter=',', names=['name', 'label'])
    index_0 = df[df['label'] == 0].index
    #index_1 = df[df['label'] == 1].index
    df.drop(index_0, inplace=True)
    #df.drop(index_1, inplace=True)
    final_dir = '/Volumes/Disk/NIKOS_BCR_1_test.csv'
    df.to_csv(final_dir, index=False, header=False)


def getSubjectID(source_dir_train, source_dir_test):
    slides_list_train = os.listdir(source_dir_train)
    slides_list_test = os.listdir(source_dir_test)
    slides_list = slides_list_train + slides_list_test
    patients_list = []
    for i in slides_list:
        if i[:8] not in patients_list:
            patients_list.append(i[:8])
    return patients_list


patients = getSubjectID('/Volumes/Disk/BCR/TRAININGVALIDATION/B/', '/Volumes/Disk/BCR/TEST/B/')
print(len(patients))


def splitData(patients_list):
    """Used to split the data into 2 different data-sets:
    training/validation and testing."""
    training = 0.70
    validation = 0.15
    test = 0.15
    n_patients = len(patients_list)
    training_set = random.sample(patients_list, k=int(training*n_patients))
    validation_set = random.sample(patients_list, k=int(validation*n_patients+1))
    test_set = random.sample(patients_list, k=int(test*n_patients+1))
    return training_set, validation_set, test_set


train = ['17H01203', '15H05586', '17H00878', '16H01241', '14H02579', '17H00412', '16H03438', '17H00728', '17H01559', '15H05697', '16H04020', '17H00088', '16H01340', '16H04913', '16H03098', '14H00424', '17H00335', '16H04184', '15H01683', '15H02908', '16H00142', '16H05245', '14H01117', '15H03110', '15H04381', '16H01373', '16H03182', '14H02580', '15H00313', '15H00616', '14H02581', '14H00245', '16H04496', '17H01224', '14H00286', '15H01277', '14H01738', '15H04337', '16H04875', '16H01230', '17H00179', '15H04919', '16H02947', '17H00145', '16H05010', '16H00269', '15H02218', '14H01127', '15H01279', '16H04799', '14H02723', '15H03287', '17H01469', '16H03866', '14H03609', '15H00314', '15H04409', '15H02244', '16H00141', '17H01312', '14H00151', '17H00357', '16H02957', '15H04726', '15H02850', '16H04861', '15H01206', '15H03284', '17H01574', '15H04917', '15H01422', '16H04380', '15H00315', '16H05304', '16H02953', '17H01752', '17H01461', '15H05488', '14H00210', '15H02846', '16H00360', '15H03892', '14H02050', '14H03428', '15H03782', '14H03758', '14H03451', '16H02976', '17H00232', '16H05132', '16H01965', '14H00442', '15H03717', '15H03348', '16H03301', '17H00062', '15H03163', '16H00986', '15H02043', '14H03136', '16H01341', '15H02242', '14H00525', '15H00934', '16H00892', '16H04578', '16H03981', '17H00198', '15H05428', '17H01363', '14H03762', '15H05142', '15H02777', '15H02245', '16H00510', '14H02994', '14H02996', '15H04603', '16H04979', '15H03156', '17H00057', '16H00934', '15H02847', '17H00144']
val = ['14H03758', '15H04337', '17H01363', '15H04841', '14H03763', '15H00312', '16H02957', '14H00151', '17H00728', '15H05260', '16H04614', '15H03156', '17H00057', '15H03220', '15H04409', '16H03182', '16H03438', '17H00749', '16H00269', '15H03347', '16H05132', '16H04578', '16H02954', '15H04603', '15H00616', '15H05488', '16H05010']
test = ['15H01279', '15H05389', '14H02580', '15H02243', '16H00141', '16H04614', '16H01340', '16H02947', '16H05132', '15H04726', '15H05142', '15H03063', '17H01752', '16H01373', '17H01093', '14H02579', '15H02043', '15H01704', '17H01559', '16H01436', '15H00312', '14H03136', '16H01241', '16H00075', '15H04739', '14H00210', '15H05260']


csv_0 = '/Volumes/Disk/NIKOS_BCR_0.csv'
csv_1 = '/Volumes/Disk/NIKOS_BCR_1.csv'

df_0 = pandas.read_csv(csv_0, delimiter=',', names=['name', 'label'])
df_1 = pandas.read_csv(csv_1, delimiter=',', names=['name', 'label'])

list_0 = df_0['name'].tolist()
list_1 = df_1['name'].tolist()


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


for i in sorted(list_0):
    index_i = list(find_all(i, '_'))
    index_0 = index_i[0]
    index_1 = index_i[1]
    for x in sorted(val):
        if x == i[:index_i[0]]:
            for j in os.listdir('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/'):
                if '._' not in j:
                    if i[:index_1] == j:
                        dir_in = os.path.join(os.path.join('/Volumes/Disk/ALL_IM/NORM_IM_FINAL/', j), 'patches_256')
                        for k in os.listdir(dir_in):
                            if '._' not in k:
                                if k.endswith('.png'):
                                    name = k
                                    name_k = name.replace('-', '_')
                                    if name_k[:-4] == i:
                                        dir_final_1 = '/Volumes/Disk/NIKOS_BCR/validation/noBCR/'
                                        shutil.copy(os.path.join(dir_in, k), dir_final_1)











