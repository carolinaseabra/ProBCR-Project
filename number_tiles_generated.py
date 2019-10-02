import os
import numpy

def count_images(path_images):
    list_images = 0
    for j in os.listdir(path_images):
        if '._' not in j:
            if j.endswith('.png'):
                list_images = list_images + 1
    return list_images


n = []
dir_source = '/Volumes/Disk/ALL_IM/NORM_IM_FINAL/'
for i in os.listdir(dir_source):
    if '._' not in i:
        dir_in = os.path.join(dir_source, i)
        patches_dir = os.path.join(dir_in, 'patches_256')
        k = count_images(patches_dir)
        n.append(k)


n_images = numpy.array(n)
n_mean = numpy.mean(n_images)
n_max = numpy.max(n_images)
n_min = numpy.min(n_images)

print(n_images)
print(n_mean)
print(n_max)
print(n_min)
print(numpy.std(n_images))