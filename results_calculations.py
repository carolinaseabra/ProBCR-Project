import numpy
from sklearn.metrics import confusion_matrix
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import multilabel_confusion_matrix


# NON NORM IMAGES
cm_1 = numpy.array([[94767, 2377, 0], [4630, 39979, 0], [1847, 366, 0]])
cm_2 = numpy.array([[17636, 488, 0], [955, 7614, 0], [404, 96, 3]])
cm_3 = numpy.array([[17659, 516, 7], [1430, 7997, 4], [323, 87, 13]])
cm_4 = numpy.array([[18924, 524, 56], [1046, 5935, 29], [273, 73, 75]])
cm_5 = numpy.array([[18724, 941, 16], [656, 8694, 16], [346, 64, 46]])


# NORM IMAGES
cm_1_NORM = numpy.array([[20723, 293, 2], [2034, 8739, 8], [346, 61, 5]])
cm_2_NORM = numpy.array([[18146, 265, 0], [1526, 6526, 0], [420, 53, 0]])
cm_3_NORM = numpy.array([[19417, 361, 0], [1688, 5938, 3], [418, 74, 1]])
cm_4_NORM = numpy.array([[19141, 87, 0], [2261, 5099, 0], [452, 15, 0]])
cm_5_NORM = numpy.array([[19824, 377, 2], [1121, 8243, 0], [359, 46, 0]])


# NORM IMAGES NEW

cm_1_NORM_NEW = numpy.array([[19900, 1117, 1], [1064, 9716, 1],[287, 120, 5]])
cm_2_NORM_NEW = numpy.array([[18124, 252, 35], [1581, 6400, 71], [369, 46, 58]])
cm_3_NORM_NEW = numpy.array([[19477, 300, 1], [1733, 5894, 2], [415, 71, 7]])
cm_4_NORM_NEW = numpy.array([[18687, 541, 0], [940, 6420, 0], [398, 69, 0]])
cm_5_NORM_NEW = numpy.array([[19502, 688, 13], [1054, 8308, 2], [336, 54, 15]])

# NORM IMAGES MIXED

cm_1_MIXED_NORM = numpy.array([[19900, 1117, 1], [1064, 9716, 1],[287, 120, 5]])
cm_2_MIXED_NORM = numpy.array([[18146, 265, 0], [1526, 6526, 0], [420, 53, 0]])
cm_3_MIXED_NORM = numpy.array([[19477, 300, 1], [1733, 5894, 2], [415, 71, 7]])
cm_4_MIXED_NORM = numpy.array([[18687, 541, 0], [940, 6420, 0], [398, 69, 0]])
cm_5_MIXED_NORM = numpy.array([[19824, 377, 2], [1121, 8243, 0], [359, 46, 0]])


def cm_normalised(cm):
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, numpy.newaxis]
    return cm_normalized

def k_statistics(cm):
    total = numpy.sum(cm)
    diagonal = numpy.diag(cm)
    agreement = numpy.sum(diagonal)/total
    c_0 = numpy.sum(cm[:, 0])
    c_1 = numpy.sum(cm[:, 1])
    c_2 = numpy.sum(cm[:, 2])
    r_0 = numpy.sum(cm[0, :])
    r_1 = numpy.sum(cm[1, :])
    r_2 = numpy.sum(cm[2, :])
    p_0 = r_0/total * c_0/total
    p_1 = r_1 / total * c_1 / total
    p_2 = r_2 / total * c_2 / total
    chance_agreement = p_0 + p_1 + p_2
    k = 1-(1-agreement)/(1-chance_agreement)

    return k

k_1 = k_statistics(cm_1)
k_2 = k_statistics(cm_2)
k_3 = k_statistics(cm_3)
k_4 = k_statistics(cm_4)
k_5 = k_statistics(cm_5)

k = numpy.array([k_1, k_2, k_3, k_4, k_5])
k_mean = numpy.mean(k)
k_std = numpy.std(k)
#print('k (non_norm) = ', k_mean)
#print(k_std)

accuracy_NON_NORM = numpy.array([0.9359571009821763, 0.9285556699514634, 0.9155728349265231, 0.9257100426953777, 0.930888384232112])
accuracy_NON_NORM_mean = numpy.mean(accuracy_NON_NORM)
accuracy_NON_NORM_std = numpy.std(accuracy_NON_NORM)
#print('accuracy (non_norm)=', accuracy_NON_NORM_mean, '±', accuracy_NON_NORM_std)


k_1_NORM = k_statistics(cm_1_NORM)
k_2_NORM = k_statistics(cm_2_NORM)
k_3_NORM = k_statistics(cm_3_NORM)
k_4_NORM = k_statistics(cm_4_NORM)
k_5_NORM = k_statistics(cm_5_NORM)

k_NORM = numpy.array([k_1_NORM, k_2_NORM, k_3_NORM, k_4_NORM, k_5_NORM])
k_NORM_mean = numpy.mean(k_NORM)
k_NORM_std = numpy.std(k_NORM)
#print(k_NORM)
#print('k (norm) = ', k_NORM_mean)
#print(k_NORM_std)

accuracy_NORM = numpy.array([0.9148117102853063, 0.9159489159489159, 0.9088172043010753, 0.8959526889669193, 0.9364406779661016])
accuracy_NORM_mean = numpy.mean(accuracy_NORM)
accuracy_NORM_std = numpy.std(accuracy_NORM)
#print('accuracy (norm) =', accuracy_NORM_mean, '±', accuracy_NORM_std)


k_1_NORM_NEW = k_statistics(cm_1_NORM_NEW)
k_2_NORM_NEW = k_statistics(cm_2_NORM_NEW)
k_3_NORM_NEW = k_statistics(cm_3_NORM_NEW)
k_4_NORM_NEW = k_statistics(cm_4_NORM_NEW)
k_5_NORM_NEW = k_statistics(cm_5_NORM_NEW)

k_NORM_NEW = numpy.array([k_1_NORM_NEW, k_2_NORM_NEW, k_3_NORM_NEW, k_4_NORM_NEW, k_5_NORM_NEW])
k_NORM_NEW_mean = numpy.mean(k_NORM_NEW)
k_NORM_NEW_std = numpy.std(k_NORM_NEW)
#print(k_NORM_NEW)
#print('k (norm_new) = ', k_NORM_NEW_mean)
#print(k_NORM_NEW_std)

accuracy_NORM_NEW = numpy.array([0.9195926857284779, 0.9126076626076626, 0.9096057347670251, 0.9279985215302162, 0.9283664753770186])
accuracy_NORM_NEW_mean = numpy.mean(accuracy_NORM_NEW)
accuracy_NORM_NEW_std = numpy.std(accuracy_NORM_NEW)
#print('accuracy (norm_new)=', accuracy_NORM_NEW_mean, '±', accuracy_NORM_NEW_std)


# MIXED NORM
k_MIXED_NORM = numpy.array([k_1_NORM_NEW, k_2_NORM, k_3_NORM_NEW, k_4_NORM_NEW, k_5_NORM])
print('k_norm=', k_MIXED_NORM)
k_MIXED_NORM_mean = numpy.mean(k_MIXED_NORM)
k_MIXED_NORM_std = numpy.std(k_MIXED_NORM)
#print('k (norm_new) = ', k_MIXED_NORM_mean)
#print(k_MIXED_NORM_std)

accuracy_MIXED_NORM = numpy.array([0.9195926857284779, 0.9159489159489159, 0.9096057347670251, 0.9279985215302162, 0.9364406779661016])
accuracy_MIXED_NORM_mean = numpy.mean(accuracy_MIXED_NORM)
accuracy_MIXED_NORM_std = numpy.std(accuracy_MIXED_NORM)
#print('accuracy (mixed) =', accuracy_MIXED_NORM_mean, '±', accuracy_MIXED_NORM_std)





# ==================== BCR =============================

cm_1_BCR = numpy.array([[7536, 0], [1761, 0]])
cm_2_BCR = numpy.array([[5774, 0], [1450, 0]])
cm_3_BCR = numpy.array([[4507, 0], [3470, 0]])
cm_4_BCR = numpy.array([[4965, 0], [2688, 0]])
cm_5_BCR = numpy.array([[4024, 0], [4271, 0]])


def k_statistics_BCR(cm):
    total = numpy.sum(cm)
    p0 = (cm[0, 0] + cm[1, 1]) / total
    pclass0 = (cm[0, 0] + cm[0, 1]) / total * (cm[0, 0] + cm[1, 0]) / total
    pclass1 = (cm[1, 0] + cm[1, 1]) / total * (cm[0, 1] + cm[1, 0]) / total
    pe = pclass0 + pclass1
    k = (p0 - pe) / (1 - pe)
    return k


k_1_BCR = k_statistics_BCR(cm_1_BCR)
k_2_BCR = k_statistics_BCR(cm_2_BCR)
k_3_BCR = k_statistics_BCR(cm_3_BCR)
k_4_BCR = k_statistics_BCR(cm_4_BCR)
k_5_BCR = k_statistics_BCR(cm_5_BCR)

k_BCR = numpy.array([k_1_BCR, k_2_BCR, k_3_BCR, k_4_BCR, k_5_BCR])
print('BCR_k', k_BCR)
k_BCR_mean = numpy.mean(k_BCR)
k_BCR_std = numpy.std(k_BCR)
#print('k (BCR) =', k_BCR_mean, '±', k_BCR_std)


def CalculateAccuracy(cm):
    total = numpy.sum(cm)
    tp = cm[0, 0]
    tn = cm[1, 1]
    accuracy = (tp+tn)/total
    return accuracy


accuracy_BCR = numpy.array([CalculateAccuracy(cm_1_BCR), CalculateAccuracy(cm_2_BCR), CalculateAccuracy(cm_3_BCR),
                            CalculateAccuracy(cm_4_BCR), CalculateAccuracy(cm_5_BCR)])
accuracy_BCR_mean = numpy.mean(accuracy_BCR)
accuracy_BCR_std = numpy.std(accuracy_BCR)
#print('accuracy (BCR) =', accuracy_BCR_mean, '±', accuracy_BCR_std)

print('BCR_accuracy', accuracy_BCR)



#====================================================================================================

"""
binary_metrics = multilabel_confusion_matrix(actual, predicted)
#print(binary_metrics)

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

print('Specificity =', spec_0)
print('Specificity =', spec_1)
print('Specificity =', spec_2)

print('Accuracy =', accuracy_0)
print('Accuracy =', accuracy_1)
print('Accuracy =', accuracy_2)
"""