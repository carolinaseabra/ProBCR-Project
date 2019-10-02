import tensorflow as tf
from numpy import random

"""
Plotting multiple scalars on the same graph
"""

writer_val = tf.summary.FileWriter('/Volumes/ccig/carolina.seabra/out/model5/inference_niftynet.log')
writer_train = tf.summary.FileWriter('/Volumes/ccig/carolina.seabra/out/model5/training_niftynet.log')
loss_var = tf.Variable(0.0)
tf.summary.scalar("loss", loss_var)
write_op = tf.summary.merge_all()
session = tf.InteractiveSession()
session.run(tf.global_variables_initializer())
for i in range(100):
    # loss validation
    summary = session.run(write_op, {loss_var: random.rand()})
    writer_val.add_summary(summary, i)
    writer_val.flush()
    # loss train
    summary = session.run(write_op, {loss_var: random.rand()})
    writer_train.add_summary(summary, i)
    writer_train.flush()

