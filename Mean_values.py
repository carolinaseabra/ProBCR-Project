import numpy
import pandas
from sklearn.metrics import accuracy_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import cohen_kappa_score

file = ['/Users/carolina/Desktop/output_files/NON_NORM/model1/inference_model1.csv',
        '/Users/carolina/Desktop/output_files/NON_NORM/model2/inference_model2.csv',
        '/Users/carolina/Desktop/output_files/NON_NORM/model3_new/inference_model3_new.csv',
        '/Users/carolina/Desktop/output_files/NON_NORM/model4/inference_model4.csv',
        '/Users/carolina/Desktop/output_files/NON_NORM/model5/inference_model5.csv']

def MetricsCalculater(file):
    modality_label = '/Users/carolina/Desktop/output_files/NON_NORM/modality_label.csv'

    df_predicted = pandas.read_csv(file, delimiter=',', names=['name', 'predicted'])
    df_actual = pandas.read_csv(modality_label, delimiter=',', names=['name', 'actual'])

    df_final = pandas.merge(df_actual, df_predicted, on='name', how='inner')

    actual = df_final['actual'].tolist()
    predicted = df_final['predicted'].tolist()

    acc = accuracy_score(actual, predicted)
    k = cohen_kappa_score(actual, predicted, labels=None, weights=None)
    mcc = matthews_corrcoef(actual, predicted)

    return acc, k, mcc


def MeanCalculater(l_acc, l_k, l_mcc):

    acc_matrix = numpy.array(l_acc)
    acc_mean = numpy.mean(acc_matrix)
    acc_std = numpy.std(acc_matrix)
    k_matrix = numpy.array(l_k)
    k_mean = numpy.mean(k_matrix)
    k_std = numpy.std(k_matrix)
    mcc_matrix = numpy.array(l_mcc)
    mcc_mean = numpy.mean(mcc_matrix)
    mcc_std = numpy.std(mcc_matrix)
    acc = acc_mean, '±', acc_std
    k = k_mean, '±', k_std
    mcc = mcc_mean, '±', mcc_std

    return acc, k, mcc


acc_list = []
k_list = []
mcc_list = []
for i in file:
    acc, k, mcc = MetricsCalculater(i)
    acc_list.append(acc)
    k_list.append(k)
    mcc_list.append(mcc)

acc, k, mcc = MeanCalculater(acc_list, k_list, mcc_list)
print('Accuracy=', acc)
print('K=', k)
print('MCC=', mcc)

