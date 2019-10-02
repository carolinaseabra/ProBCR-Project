import pandas
from sklearn.metrics import confusion_matrix
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import classification_report
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import balanced_accuracy_score
from sklearn import metrics
from sklearn.metrics import precision_score
import scikitplot as skplt
import numpy
import seaborn
import matplotlib.pyplot as plt




file = '/Users/carolina/Desktop/output_files/NON_NORM/model1/inference_model1.csv'
#file_prob = '/Users/carolina/Desktop/output_files/NON_NORM/TEST/test_inference_prob.csv'
df_predicted = pandas.read_csv(file, delimiter=',', names=['name', 'predicted'])
#df_predicted_prob = pandas.read_csv(file_prob, delimiter=',', names=['name', 'label_0', 'label_1', 'label_2'])
#print(df_predicted_prob.dtypes)

modality_label = '/Users/carolina/Desktop/output_files/NON_NORM/modality_label.csv'
df_actual = pandas.read_csv(modality_label, delimiter=',', names=['name', 'actual'])

#convert_dict_0 = {'name': object}
#convert_dict_1 = {'name': object, 'actual': float}

#df_predicted_prob = df_predicted_prob.astype(convert_dict_0)
#df_actual = df_actual.astype(convert_dict_1)

df_final = pandas.merge(df_actual, df_predicted, on='name', how='inner')
#df_final = pandas.merge(df_actual, df_predicted_prob, left_on='name', right_on='name')


actual = df_final['actual'].tolist()
predicted = df_final['predicted'].tolist()
#predicted = df_final.as_matrix(columns=['label_0', 'label_1', 'label_2'])

target_names = ['class 0', 'class 1', 'class 2']
#target_names = ['class 0', 'class 1']
metrics = classification_report(actual, predicted, target_names=target_names)
print(metrics)

print('Accuracy=', accuracy_score(actual, predicted))
#print('MCC=', matthews_corrcoef(actual, predicted))


binary_metrics = multilabel_confusion_matrix(actual, predicted)
print(binary_metrics)

#skplt.metrics.plot_roc_curve(actual, predicted)
#plt.show()


cm = confusion_matrix(actual, predicted)
#print('Confusion Matrix \n', cm)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, numpy.newaxis]
#print('Confusion Matrix Normalised \n', cm_normalized)

k = cohen_kappa_score(actual, predicted, labels=None, weights=None)
print('Cohen kappa score =', k)

recall = recall_score(actual, predicted, average='binary')
print('Recall=', recall)

precision = precision_score(actual, predicted, average='binary')
print('Precision=', precision)

f1score = f1_score(actual, predicted, average='binary')
print('F1 score=', f1score)

#skplt.metrics.plot_confusion_matrix(actual, predicted, normalize=True)
#skplt.metrics.plot_confusion_matrix(actual, predicted, normalize=False)
#plt.show()



"""
class_0_cm = binary_metrics[0]
class_1_cm = binary_metrics[1]
class_2_cm = binary_metrics[2]

class_0_total = numpy.sum(class_0_cm)
class_1_total = numpy.sum(class_1_cm)
class_2_total = numpy.sum(class_2_cm)

class_0_tn = class_0_cm[0, 0]
class_1_tn = class_1_cm[0, 0]
class_2_tn = class_2_cm[0, 0]

class_0_fp = class_0_cm[0, 1]
class_1_fp = class_1_cm[0, 1]
class_2_fp = class_2_cm[0, 1]

class_0_fn = class_0_cm[1, 0]
class_1_fn = class_1_cm[1, 0]
class_2_fn = class_2_cm[1, 0]

class_0_tp = class_0_cm[1, 1]
class_1_tp = class_1_cm[1, 1]
class_2_tp = class_2_cm[1, 1]

sens_0 = class_0_tp / (class_0_tp + class_0_fn)
spec_0 = class_0_tn / (class_0_tn + class_0_fp)

sens_1 = class_1_tp / (class_1_tp + class_1_fn)
spec_1 = class_1_tn / (class_1_tn + class_1_fp)

sens_2 = class_2_tp / (class_2_tp + class_2_fn)
spec_2 = class_2_tn / (class_2_tn + class_2_fp)

accuracy_0 = (class_0_tp + class_0_tn) / class_0_total
accuracy_1 = (class_1_tp + class_1_tn) / class_1_total
accuracy_2 = (class_2_tp + class_2_tn) / class_2_total

fnr_0 = class_0_fn / (class_0_fp + class_0_tp)
fnr_1 = class_1_fn / (class_1_fp + class_1_tp)
fnr_2 = class_2_fn / (class_2_fp + class_2_tp)

fpr_0 = class_0_fp / (class_0_fn + class_0_tn)
fpr_1 = class_1_fp / (class_1_fn + class_1_tn)
fpr_2 = class_2_fp / (class_2_fn + class_2_tn)

#print('False Negative Rate =', fnr_0)
#print('False Negative Rate =', fnr_1)
#print('False Negative Rate =', fnr_2)

#print('False Positive Rate =', fpr_0)
#print('False Positive Rate =', fpr_1)
#print('False Positive Rate =', fpr_2)


#print('Specificity =', spec_0)
#print('Specificity =', spec_1)
#print('Specificity =', spec_2)

#print('Accuracy =', accuracy_0)
#print('Accuracy =', accuracy_1)
#print('Accuracy =', accuracy_2)


skplt.metrics.plot_confusion_matrix(actual, predicted, normalize=True)
#skplt.metrics.plot_confusion_matrix(actual, predicted, normalize=False)
plt.show()

#df_final.to_csv('/Users/carolina/Desktop/output_files/model2/2labels.csv', index=False, header=True)


"""



