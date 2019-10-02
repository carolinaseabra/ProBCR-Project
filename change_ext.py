import os


dir_images = '/Volumes/Disk/NEW_BCR/B/'
for i in os.listdir(dir_images):
    path_images = os.path.join(dir_images, i)
    for j in os.listdir(path_images):
        if '._' not in j:
            if j.endswith('.png'):
                newfile = j.replace('.png', '.nii')
                os.rename(os.path.join(path_images, j), os.path.join(path_images, newfile))

                #pre = os.path.splitext(j)
                #os.rename(j, pre + '.nii')


