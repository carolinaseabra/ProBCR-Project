import os


def count_images(dir_images):
    #dir_images = '/Volumes/Disk/TRAININGVALIDATION/B/'
    list_images = 0
    for i in os.listdir(dir_images):
        path_images = os.path.join(dir_images, i)
        for j in os.listdir(path_images):
            if '._' not in j:
                #if j.endswith('.nii'):
                if j.endswith('.png'):
                    list_images = list_images + 1
    return list_images

n = count_images('/Volumes/Disk/NEW_BCR/B/')
print(n)