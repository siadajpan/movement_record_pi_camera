import time

import cv2

from movement_recorder.camera.abstract_camera import AbstractCamera


class WebCamera(AbstractCamera):
    def __init__(self, image_queue):
        super().__init__()
        self._cap = cv2.VideoCapture(0)
        self._stop = False
        self._image_queue = image_queue
        self._recording = False

    def start_recording(self):
        print('starting recording')
        self._recording = True

    def stop(self):
        self._stop = True

    @property
    def image_queue(self):
        return self._image_queue

    def run(self) -> None:
        while not self._stop:
            _, frame = self._cap.read()
            self.image_queue.put(frame)

            if self._recording:
                print('-------------recording')
                time.sleep(3)
                print('stopping recording')
                self._recording = False
