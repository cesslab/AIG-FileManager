import os
import shutil


def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as e:
        print('Directory ({}) not created. Error: {}'.format(directory, e))


def copy_director(source, destination):
    try:
        shutil.copy_tree(source, destination)
    except shutil.Error as e:
        print('Directory ({}) not copied to ({}). Error: {}'.format(source, destination, e))
