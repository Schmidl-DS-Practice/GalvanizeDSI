'''inital file names and jpgs from beginging of capstone, but this code is not used anywhere.
Keeping as an example.'''
from image_loader import open_images
import os

### start: part of initial EDA
def get_file_names(dir_name):
    '''gets the file names of the images'''
    list_of_file = os.listdir(dir_name)
    all_files = []
    for entry in list_of_file:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            all_files = all_files + get_file_names(full_path)
        else:
            all_files.append(full_path)
    return all_files

def get_jpgs(t_set, fruit_name):
    '''get the images as an array'''
    images_array = []
    for path in t_set:
        if path[-3:] == 'jpg':
            images_array.append(open_images(path, fruit_name))
    return images_array
### end: part of initial EDA

if __name__ == '__main__':
    ## returns all_files in path
    tomato_set = get_file_names('data/fruits_vegetables/Tomato')
    pear_set = get_file_names('data/fruits_vegetables/Pear')

    ## returns all .jpg files
    jpgs = get_jpgs(tomato_set, fruit_name=None)
    jpgs = get_jpgs(pear_set, fruit_name=None)
