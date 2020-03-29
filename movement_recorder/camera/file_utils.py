import datetime
import os
from typing import Tuple

from movement_recorder import settings


def get_datetime(extension) -> Tuple[str, str]:
    """ Makes path name from datetime """
    date = datetime.datetime.now()
    dir_path = f"{date.year}-{date.month}-{date.day}"
    img_name = f"{date.hour}-{date.minute}-{date.second}.{extension}"

    return dir_path, img_name


def create_folder_structure(folder_path):
    if os.path.exists(folder_path):
        return

    os.mkdir(folder_path)


def create_new_folder_and_file_name(extension):
    parent_dir = settings.Files.SAVING_FOLDER
    dir_path, img_name = get_datetime(extension)
    dir_path = os.path.join(parent_dir, dir_path)
    create_folder_structure(dir_path)

    return os.path.join(dir_path, img_name)


def copy_folder_structure(folder_in, folder_out):
    for folder in os.listdir(folder_in):
        folder_path = os.path.join(folder_out, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
