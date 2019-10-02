import py_wsi
import os
import shutil

# SET THE PARAMETERS FOR FILE DIRECTORY

#dir_DISK = '/Volumes/Disk/'

dir_DISK = '/Users/carolina/Desktop/SlideJ/'

#files_dir = '/Volumes/Disk/SORTED_SLIDES/17H01833_A3/'

files_dir = '/Users/carolina/Desktop/'

patches_dir = '/Users/carolina/Desktop/SlideJ'

try:
    os.makedirs(os.path.join(dir_DISK, 'PATCHES'))
    print("Directory ", patches_dir, " Created ")
except FileExistsError:
    print("Directory ", patches_dir, " already exists")


#db_location = '/Volumes/Disk/PATCHES/'

db_location = '/Users/carolina/Desktop/SlideJ'

try:
    os.makedirs(db_location)
    print("Directory ", db_location, " Created ")
except FileExistsError:
    print("Directory ", db_location, " already exists")

xml_dir = files_dir
db_name = 'patch_db'

turtle = py_wsi.Turtle(files_dir, db_location, db_name=db_name, storage_type='disk', xml_dir=xml_dir, label_map=None)
print("Total WSI images:    " + str(turtle.num_files))
print("LMDB name:           " + str(turtle.db_name))
print("File names:          " + str(turtle.files))

#a = turtle.files
#if a.endswith('svs'):
#    print ('FIXE')


level_count, level_tiles, level_dims = turtle.retrieve_tile_dimensions(turtle.files[0], patch_size = 512)
print("Level count:         " + str(level_count))
print("Level tiles:         " + str(level_tiles))
print("Level dimensions:    " + str(level_dims))


patch_size = 512
level = 6  #[0-18]
overlap = 0

#turtle.sample_and_store_patches(patch_size, level, overlap, load_xml=False, limit_bounds=True)


#patches, coords, classes, labels = turtle.get_patches_from_file(turtle.files[0], verbose=True)
