import pandas
import numpy




file = '/Users/carolina/Desktop/output_files/NON_NORM/TEST/test_inference.csv'
modality_label = '/Users/carolina/Desktop/output_files/NON_NORM/TEST/TEST_labels.csv'

df_predicted = pandas.read_csv(file, delimiter=',', names=['name', 'predicted'])
df_actual = pandas.read_csv(modality_label, delimiter=',', names=['name', 'actual'])

df_final = pandas.merge(df_actual, df_predicted, on='name', how='inner')

actual = df_final['actual'].tolist()
predicted = df_final['predicted'].tolist()
print(len(predicted))


indx = []
for k in range(0, len(actual)-1):
    if actual[k] == predicted[k]:
        indx.append(k)

#df_wrong = df_final.copy()
df_final.drop(df_final.index[indx], inplace=True)

#df_wrong.to_csv('/Users/carolina/Desktop/output_files/NON_NORM/TEST/wrong_results_1.csv', index=False, header=False)

actual_updated = df_final['actual'].tolist()
predicted_updated = df_final['predicted'].tolist()

indx_0_1 = []
indx_0_2 = []
indx_1_0 = []
indx_1_2 = []
indx_2_0 = []
indx_2_1 = []

for k in range(0, len(actual_updated)-1):
    if actual_updated[k] == 0 & predicted_updated[k] == 1:
        indx_0_1.append(k)
    elif actual_updated[k] == 0 and predicted_updated[k] == 2:
        indx_0_2.append(k)
    elif actual_updated[k] == 1 and predicted_updated[k] == 0:
        indx_1_0.append(k)
    elif actual_updated[k] == 1 and predicted_updated[k] == 2:
        indx_1_2.append(k)
    elif actual_updated[k] == 2 and predicted_updated[k] == 0:
        indx_2_0.append(k)
    elif actual_updated[k] == 2 and predicted_updated[k] == 1:
        indx_2_1.append(k)

print(len(indx_0_1))

df_0_1 = df_final.copy()
df_0_1.drop(df_0_1.index[indx_0_1], inplace=True)

#df_0_2 = df_final.copy()
#df_0_2 = df_final.drop(df_final.index[indx_0_2], inplace=True)

#df_1_0 = df_final.copy()
#df_1_0 = df_final.drop(df_final.index[indx_1_0], inplace=True)

#df_1_2 = df_final.copy()
#df_1_2 = df_final.drop(df_final.index[indx_1_2], inplace=True)

#df_2_0 = df_final.copy()
#df_2_0 = df_final.drop(df_final.index[indx_1_2], inplace=True)

#df_2_1 = df_final.copy()
#df_2_1 = df_final.drop(df_final.index[indx_1_2], inplace=True)


df_0_1.to_csv('/Users/carolina/Desktop/output_files/NON_NORM/TEST/0_1_labels.csv', index=False, header=False)
#df_0_2.to_csv('/Users/carolina/Desktop/output_files/NON_NORM/TEST/0_2_labels.csv', index=False, header=False)
#df_1_0.to_csv('/Users/carolina/Desktop/output_files/NON_NORM/TEST/1_0_labels.csv', index=False, header=False)
#df_1_2.to_csv('/Users/carolina/Desktop/output_files/NON_NORM/TEST/1_2_labels.csv', index=False, header=False)
#df_2_0.to_csv('/Users/carolina/Desktop/output_files/NON_NORM/TEST/2_0_labels.csv', index=False, header=False)
#df_2_1.to_csv('/Users/carolina/Desktop/output_files/NON_NORM/TEST/2_1_labels.csv', index=False, header=False)