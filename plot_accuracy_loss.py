import numpy
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
import pandas
import seaborn

import sys
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
event_acc = EventAccumulator(sys.argv[1])
event_acc.Reload()
# Show all tags in the log file
print(event_acc.Tags())

# E. g. get wall clock, number of steps and value for a scalar 'Accuracy'
#w_times, step_nums, vals = zip(*event_acc.Scalars('Accuracy'))
at, ast, av = zip(*event_acc.Scalars('worker_0/accuracy'))
lt, ls, lv = zip(*event_acc.Scalars('worker_0/data_loss'))

with open(sys.argv[2]+'.csv', 'w') as f:
    for a, b, c in zip(at, ast, av):
        f.write('{0},{1},{2}\n'.format(a, b, c))
"""





#======================================================================================================================

df_training = pandas.read_csv('/Users/carolina/Desktop/output_files/BCR/BCR_model1_training.csv', delimiter=',', names=['n', 'Epochs', 'Accuracy', 'n1', 'Epochs1', 'Loss'])
df_validation = pandas.read_csv('/Users/carolina/Desktop/output_files/BCR/BCR_model1_validation.csv', delimiter=',', names=['n', 'Epochs', 'Accuracy', 'n1', 'Epochs1', 'Loss'])

df_xy_training = df_training.drop(['n'], axis=1)
x_training_accuracy = df_training['Epochs'].tolist()
y_training_accuracy = df_training['Accuracy'].tolist()

df_xy_validation = df_validation.drop(['n'], axis=1)
x_validation_accuracy = df_validation['Epochs'].tolist()
y_validation_accuracy = df_validation['Accuracy'].tolist()


#seaborn.lineplot(x='Epochs', y='Accuracy', data=df_xy_training)
#seaborn.lineplot(x='Epochs', y='Accuracy', data=df_xy_validation)
#plt.show()

new_x_training_accuracy = []
new_y_training_accuracy = []
for i in range(0, len(x_training_accuracy), 15):
    new_x_training_accuracy.append(x_training_accuracy[i])
    new_y_training_accuracy.append(y_training_accuracy[i])

new_x_validation_accuracy = []
new_y_validation_accuracy = []
for i in range(0, len(x_validation_accuracy), 15):
    new_x_validation_accuracy.append(x_validation_accuracy[i])
    new_y_validation_accuracy.append(y_validation_accuracy[i])

d_training_accuracy = {'Epochs': new_x_training_accuracy, 'Accuracy': new_y_training_accuracy}
d_validation_accuracy = {'Epochs': new_x_validation_accuracy, 'Accuracy': new_y_validation_accuracy}

new_df_training_accuracy = pandas.DataFrame(d_training_accuracy)
new_df_validation_accuracy = pandas.DataFrame(d_validation_accuracy)
"""
seaborn.set(style="whitegrid")
seaborn.set_style("darkgrid", {"axes.facecolor": ".9", 'axes.labelcolor': '.1', 'grid.color': '.99',
 'grid.linestyle': '-'})
ax = seaborn.lineplot(x='Epochs', y='Accuracy', data=new_df_training_accuracy, color='blue')
ax = seaborn.lineplot(x='Epochs', y='Accuracy', data=new_df_validation_accuracy, color='red')
ax.set_xlabel('Epochs')
ax.set_ylabel('Accuracy')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[1:], labels=labels[1:])
ax.legend(['Training', 'Validation'], facecolor='w')
ax.set_title('Accuracy Progression for Model II')
plt.ylim(0.1, 0.9)
plt.show()
"""
#=======

x_training_loss = df_training['Epochs1'].tolist()
y_training_loss = df_training['Loss'].tolist()

x_validation_loss = df_validation['Epochs1'].tolist()
y_validation_loss = df_validation['Loss'].tolist()

new_x_training_loss = []
new_y_training_loss = []
for i in range(0, len(x_training_loss), 10):
    new_x_training_loss.append(x_training_loss[i])
    new_y_training_loss.append(y_training_loss[i])

new_x_validation_loss = []
new_y_validation_loss = []
for i in range(0, len(x_validation_loss), 10):
    new_x_validation_loss.append(x_validation_loss[i])
    new_y_validation_loss.append(y_validation_loss[i])

d_training_loss = {'Epochs1': new_x_training_loss, 'Loss': new_y_training_loss}
d_validation_loss = {'Epochs1': new_x_validation_loss, 'Loss': new_y_validation_loss}

new_df_training_loss = pandas.DataFrame(d_training_loss)
new_df_validation_loss = pandas.DataFrame(d_validation_loss)

seaborn.set(style="whitegrid")
seaborn.set_style("darkgrid", {"axes.facecolor": ".9", 'axes.labelcolor': '.1', 'grid.color': '.99',
 'grid.linestyle': '-'})
ax = seaborn.lineplot(x='Epochs1', y='Loss', data=new_df_training_loss, color='blue')
ax = seaborn.lineplot(x='Epochs1', y='Loss', data=new_df_validation_loss, color='red')
ax.set_xlabel('Epochs')
ax.set_ylabel('Loss')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[1:], labels=labels[1:])
ax.legend(['Training', 'Validation'], facecolor='w')
ax.set_title('Loss Progression for Model II')
plt.ylim(0.4, 2.0)
plt.show()

