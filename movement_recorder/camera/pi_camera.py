import logging
import queue
import time

import picamera
from picamera.array import PiRGBArray

from movement_recorder import settings
from movement_recorder.camera import file_utils
from movement_recorder.camera.abstract_camera import AbstractCamera


class PiCamera(AbstractCamera):
    def __init__(self, image_queue: queue.Queue):
        super().__init__()
        self._camera = None
        self._raw_capture = None
        self._image_queue = image_queue
        self._stop_loop = False
        self._record = False
        self._init_camera()

    def start_recording(self):
        self._record = True

    def stop_camera(self):
        self._stop_loop = True
        if self._record:
            self._stop_recording()

    @property
    def image_queue(self):
        return self._image_queue

    def _init_camera(self):
        self._camera = picamera.PiCamera()
        self._raw_capture = PiRGBArray(self._camera)
        self._camera.awb_mode = 'off'
        self._camera.awb_gains = (settings.Camera.RG, settings.Camera.BG)
        self._set_resolution(settings.Camera.MOVEMENT_RESOLUTION)
        self._set_fps(settings.Camera.MOVEMENT_FPS)

    def _set_fps(self, fps):
        logging.debug(f'setting fps: {fps}')
        self._camera.framerate = fps

    def _set_resolution(self, resolution):
        logging.debug(f'settings resolution{resolution}')
        self._camera.resolution = resolution

    def _set_camera(self, recording: bool):
        if recording:
            self._set_fps(settings.Camera.RECORD_FPS)
            self._set_resolution(settings.Camera.RECORD_RESOLUTION)
        else:
            self._set_fps(settings.Camera.MOVEMENT_FPS)
            self._set_resolution(settings.Camera.MOVEMENT_RESOLUTION)

    def _start_recording(self, file_name):
        logging.info(f'------starting recording: {file_name}-------')
        self._camera.start_recording(file_name)

    def _stop_recording(self):
        logging.info(f'------stopping recording-------')
        self._camera.stop_recording()

    def _make_recording(self, record_time):
        file_name = file_utils.create_new_folder_and_file_name(
            settings.Camera.RECORD_EXTENSION)
        self._start_recording(file_name)
        start_time = time.time()

        while time.time() - start_time < record_time:
            logging.debug('waiting for stop recording')
            if self._stop_loop:
                break
            time.sleep(1)

        self._stop_recording()

    def _capture(self):
        logging.info('-----starting capture------')
        t = time.time()
        for frame in self._camera.capture_continuous(self._raw_capture,
                                                     format='bgr',
                                                     use_video_port=True):
            logging.debug(f'acquiring image time:{time.time() - t}')
            image = frame.array
            self._raw_capture.truncate(0)
            self._image_queue.put(image)
            t = time.time()
            if self._record or self._stop_loop:
                return

    def run(self) -> None:
        while not self._stop_loop:
            logging.debug('----preparing for capture------')
            self._set_camera(recording=False)
            self._capture()

            if self._record:
                logging.debug('-----preparing for recording-------')
                self._set_camera(recording=True)
                self._make_recording(settings.Camera.RECORD_TIME)
                self._record = False
