import operator
import sys
import csv

reader = csv.reader(open('/Volumes/Disk/modality_label_test.csv'), delimiter=",")

# for id, surv, age in reader:
    # print(age)

# sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=True)
sortedlist = sorted(reader, key=lambda row: row[0], reverse=False)

#print(sortedlist)

# with open(r"D:\teachingLabFiles\NiftyNet\Brats\Data4mod\modality_labels_sort.csv", 'w') as myfile:
#     wr = csv.writer(myfile)
#     wr.writerow(sortedlist)

with open('/Volumes/Disk/BCR/TEST/modality_label_test.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sortedlist)
