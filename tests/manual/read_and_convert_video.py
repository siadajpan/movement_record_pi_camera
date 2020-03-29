import os

import cv2

from movement_recorder import settings
from movement_recorder.camera import file_utils


def get_video_paths():
    path = '/home/karol/Videos/judasz/new/Videos'
    path_out = '/home/karol/Videos/judasz/archive'
    file_utils.copy_folder_structure(path, path_out)

    video_in_paths = []
    video_out_paths = []

    for day_folder_in, day_folder_out in zip(os.listdir(path),
                                             os.listdir(path_out)):
        day_folder_in_path = os.path.join(path, day_folder_in)
        day_folder_out_path = os.path.join(path_out, day_folder_out)

        for video_name in os.listdir(day_folder_in_path):
            video_in_paths.append(os.path.join(day_folder_in_path, video_name))
            video_out_name = video_name.replace(
                settings.Camera.RECORD_EXTENSION,
                'avi')
            video_out_paths.append(
                os.path.join(day_folder_out_path, video_out_name))

    return video_in_paths, video_out_paths


if __name__ == '__main__':
    video_paths, video_out_paths = get_video_paths()

    codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    w, h = settings.Camera.RECORD_RESOLUTION
    h0, he, w0, we = int(0.3 * h), int(0.9 * h), int(0.3 * w), int(0.65 * w)

    for video_path, video_out_path in zip(video_paths, video_out_paths):
        print('reading ', video_path)
        cap = cv2.VideoCapture(video_path)
        video_writer = cv2.VideoWriter(video_out_path,
                                       codec, settings.Camera.RECORD_FPS,
                                       (we - w0, he - h0))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.rotate(frame, cv2.ROTATE_180)
            frame = frame[h0: he, w0: we]

            cv2.imshow('f', frame)
            cv2.waitKey(20)
            video_writer.write(frame)

        video_writer.release()
