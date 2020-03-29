import datetime
import os
from typing import Tuple


def get_datetime(extension) -> Tuple[str, str]:
    """ Makes path name from datetime """
    date = datetime.datetime.now()
    dir_path = f"{date.year}-{date.month}-{date.day}"
    img_name = f"{date.hour}-{date.minute}-{date.second}-" \
               f"{date.microsecond}.{extension}"

    return dir_path, img_name


def create_folder_structure(folder_path):
    if os.path.exists(folder_path):
        return

    os.mkdir(folder_path)


def create_new_folder_and_file_name(extension):
    dir_path, img_name = get_datetime(extension)
    create_folder_structure(dir_path)

    return os.path.join(dir_path, img_name)
