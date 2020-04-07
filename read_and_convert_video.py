import os

import cv2

from movement_recorder import settings


def copy_folder_structure(folder_in, folder_out):
    for folder in os.listdir(folder_in):
        folder_path = os.path.join(folder_out, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)


def get_video_paths():
    path = '/home/karol/Videos/judasz/new/Videos'
    path_out = '/home/karol/Videos/judasz/archive'
    copy_folder_structure(path, path_out)

    video_in_paths = []
    video_out_paths = []

    for day_folder in os.listdir(path):
        day_folder_in_path = os.path.join(path, day_folder)
        day_folder_out_path = os.path.join(path_out, day_folder)

        video_names = os.listdir(day_folder_in_path)
        video_names.sort()
        for video_name in video_names:
            video_in_paths.append(os.path.join(day_folder_in_path, video_name))
            video_out_name = video_name.replace(
                settings.Camera.RECORD_EXTENSION,
                settings.Camera.SAVE_EXTENSION)
            video_out_paths.append(
                os.path.join(day_folder_out_path, video_out_name))

    return video_in_paths, video_out_paths


if __name__ == '__main__':
    video_paths, video_out_paths = get_video_paths()

    codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

    stop = True

    for video_path, video_out_path in zip(video_paths, video_out_paths):
        print('reading ', video_path)
        name = os.path.split(video_path)[1]
        cap = cv2.VideoCapture(video_path)
        video_writer = cv2.VideoWriter(video_out_path,
                                       codec, settings.Camera.RECORD_FPS,
                                       settings.Camera.RESOLUTION)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.rotate(frame, cv2.ROTATE_180)
            video_writer.write(frame)

            cv2.putText(frame, name.split('.')[0], (10, 30), cv2.FONT_ITALIC, 1,
                        (255, 255, 255), lineType=cv2.LINE_AA)
            cv2.imshow('f', frame)
            if stop:
                cv2.waitKey(0)
                stop = False

            cv2.waitKey(15)

        video_writer.release()
