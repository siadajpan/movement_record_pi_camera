import os

import cv2

if __name__ == '__main__':
    path = '/home/karol/Videos/2020-3-29'
    video_name = os.listdir(path)[-1]
    cap = cv2.VideoCapture(os.path.join(path, video_name))

    while True:
        _, frame = cap.read()
        cv2.imshow('f', frame)
        cv2.waitKey(1)
