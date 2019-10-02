import os
import random
import shutil
import pandas


def getImagesList(dir_images):
    slides_list = os.listdir(dir_images)
    patients_list = []
    for i in slides_list:
        if i[:8] not in patients_list:
            patients_list.append(i[:8])
    return patients_list


def splitData(patients_list):
    """Used to split the data into 2 different data-sets:
    training/validation and testing."""
    training_validation = 0.90
    test = 0.10
    n_patients = len(patients_list)
    training_validation_set = random.sample(patients_list, k=int(training_validation*n_patients))
    test_set = random.sample(patients_list, k=int(test*n_patients+1))
    return training_validation_set, test_set

def fiveFoldCrossValidation(patients_list):
    """Create a 5 fold cross to do  cross validation."""
    patients_list = sorted(patients_list)
    n_patients = len(patients_list)
    step = int(n_patients/5)
    folder_1 = [patients_list[x] for x in range(0, step, 1)]
    folder_2 = [patients_list[x] for x in range(step, 2*step, 1)]
    folder_3 = [patients_list[x] for x in range(2*step, 3*step, 1)]
    folder_4 = [patients_list[x] for x in range(3*step, 4*step, 1)]
    folder_5 = [patients_list[x] for x in range(4*step, n_patients, 1)]
    return folder_1, folder_2, folder_3, folder_4, folder_5


def list_to_csv(list, filename):
    df = pandas.DataFrame(list)
    df.to_csv(filename, index=False, header=False)
    csv = os.path.join('/Users/carolina/PycharmProjects/PROJECT', filename)
    shutil.move(csv, '/Volumes/Disk/')


#dir_images = '/Volumes/Disk/ANNOTADED_SLIDES_PAT/'
#dir_images = '/Volumes/Disk/TEST/'
dir_images = '/Volumes/Disk/BCR/TRAININGVALIDATION/'
#patients_list = getImagesList(dir_images)
#print(len(patients_list))
#print(patients_list)


#o_BCR = ['14H00124', '14H00151', '14H00241', '14H00245', '14H00249', '14H00286', '14H00424', '14H00442', '14H00525', '14H01117', '14H01127', '14H01738', '14H02050', '14H02577', '14H02580', '14H02581', '14H02723', '14H02994', '14H02995', '14H02996', '14H02997', '14H03136', '14H03428', '14H03451', '14H03609', '14H03758', '14H03762', '14H03763', '15H00312', '15H00313', '15H00314', '15H00315', '15H00616', '15H00934', '15H01206', '15H01207', '15H01249', '15H01277', '15H01279', '15H01281', '15H01422', '15H01683', '15H01704', '15H02218', '15H02242', '15H02243', '15H02244', '15H02245', '15H02777', '15H02847', '15H02849', '15H02850', '15H02908', '15H02913', '15H02993', '15H03063', '15H03156', '15H03163', '15H03220', '15H03284', '15H03287', '15H03346', '15H03347', '15H03348', '15H03713', '15H03717', '15H03782', '15H03892', '15H04337', '15H04381', '15H04409', '15H04410', '15H04603', '15H04726', '15H04739', '15H04841', '15H04917', '15H05142', '15H05263', '15H05389', '15H05428', '15H05488', '15H05586', '15H05697', '16H00075', '16H00093', '16H00141', '16H00142', '16H00269', '16H00360', '16H00492', '16H00510', '16H00544', '16H00892', '16H00934', '16H00986', '16H01230', '16H01241', '16H01243', '16H01340', '16H01373', '16H01436', '16H01965', '16H02180', '16H02947', '16H02953', '16H02954', '16H02956', '16H02957', '16H02976', '16H03098', '16H03182', '16H03301', '16H03438', '16H03866', '16H03919', '16H03981', '16H04020', '16H04184', '16H04380', '16H04458', '16H04496', '16H04614', '16H04799', '16H04861', '16H04875', '16H04913', '16H05010', '16H05038', '16H05108', '16H05132', '16H05245', '16H05304', '16H05328', '16H05427', '17H00057', '17H00062', '17H00088', '17H00144', '17H00198', '17H00232', '17H00335', '17H00357', '17H00412', '17H00555', '17H00749', '17H01093', '17H01129', '17H01203', '17H01224', '17H01312', '17H01363', '17H01407', '17H01461', '17H01469', '17H01534', '17H01559', '17H01574', '17H01594', '17H01752']
#u_BCR = ['14H00210', '14H02579', '15H02043', '15H02846', '15H03110', '15H04919', '15H05260', '16H01341', '16H02433', '16H02480', '16H04274', '16H04578', '16H04979', '17H00145', '17H00179', '17H00728', '17H00878', '17H01148']

#o = ['16H04614', '17H01534', '16H00986', '15H01719', '16H02433', '15H05428', '15H03782', '14H01230', '16H04979', '15H04337', '16H00892', '16H02480', '15H03717', '15H03163', '17H01203', '16H05038', '15H05488', '15H04603', '14H01357', '14H01127', '17H00062', '16H00360', '16H00222', '17H00088', '14H02996', '15H03110', '16H00075', '16H02957', '15H03156', '17H00145', '16H03438', '16H03301', '15H01277', '15H02777', '17H01752', '15H02849', '16H04875', '15H04409', '17H00144', '17H01407', '16H02956', '16H03098', '15H02243', '15H05263', '17H01559', '16H02976', '15H00315', '17H01780', '15H02993', '17H00728', '15H05697', '16H05304', '15H03346', '15H03348', '16H01965', '14H03758', '16H00142', '15H03287', '14H03762', '17H00412', '16H00093', '15H02908', '15H01207', '16H05328', '15H00313', '17H00357', '16H04913', '15H03713', '16H04184', '14H02050', '15H02850', '14H00424', '15H01249', '17H01833', '17H01093', '16H00269', '16H03981', '15H02847', '16H05132', '15H02245', '15H02043', '17H00232', '14H03452', '14H02995', '16H04274', '17H01148', '17H01170', '15H04841', '16H00492', '16H01243', '15H01422', '16H04020', '14H02723', '14H00210', '14H00124', '16H01051', '16H00934', '17H01469', '16H03182', '15H04919', '15H05260', '14H02580', '14H03609', '15H03059', '15H02390', '15H02846', '16H03866', '16H02180', '15H05142', '16H03455', '15H00312', '15H04900', '16H01373', '15H05586', '16H01241', '16H02947', '15H02242', '15H04410', '15H01281', '16H00666', '16H05108', '17H01594', '15H03220', '16H04799', '15H03892', '15H03347', '17H00514', '16H02953', '15H04726', '14H01738', '16H04380', '14H03136', '15H03750', '15H01683', '17H00878', '15H03284', '15H02244', '14H03451', '15H05389', '16H02954', '15H00616', '16H05245', '15H04917', '14H00442', '16H00614', '16H01341', '17H01461', '17H01312', '16H04578', '16H05010', '14H02581', '15H00314', '14H01117', '17H01129', '16H04458', '14H00525', '14H03450', '15H01205', '14H00249', '16H01340', '15H01279', '15H01206', '17H00198', '14H03763', '14H00245', '16H04817', '14H02994', '15H02913', '17H00179', '17H00335', '14H00241', '14H02997', '14H00286', '14H03428', '16H03919', '14H02577', '17H01224', '15H04739', '16H00544', '14H00151']
#u = ['17H00514', '16H02947', '15H02847', '16H05328', '17H01129', '16H00986', '15H03156', '17H01469', '15H02243', '15H04410', '15H01206', '14H03428', '16H03301', '16H03981', '17H01559', '17H00198', '14H02050', '15H01279', '16H05245', '15H02390']

df = pandas.read_csv('/Volumes/Disk/NEW_BCR/data_new_BCR.csv', delimiter=';', names=['name', 'label'])
patients_list = df['name'].tolist()
folder_1, folder_2, folder_3, folder_4, folder_5 = fiveFoldCrossValidation(patients_list)
print('start:', folder_1[0], 'finish:', folder_1[-1])
print('start:', folder_2[0], 'finish:', folder_2[-1])
print('start:', folder_3[0], 'finish:', folder_3[-1])
print('start:', folder_4[0], 'finish:', folder_4[-1])
print('start:', folder_5[0], 'finish:', folder_5[-1])
