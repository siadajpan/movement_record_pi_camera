import queue
import time
from threading import Thread

from movement_recorder import settings


class PiCamera(Thread):
    def __init__(self, image_queue: queue.Queue):
        super().__init__()
        self.camera = None
        self.raw_capture = None
        self.image_queue = image_queue
        self.stop = False
        self.record = False

    def init_camera(self):
        self.camera = picamera.PiCamera()
        self.raw_capture = PiRGBArray(self.camera)
        self.camera.resolution = settings.Camera.MOVEMENT_RESOLUTION
        self.camera.framerate = settings.Camera.MOVEMENT_FPS

    def set_fps(self, fps):
        self.camera.framerate = fps

    def set_resolution(self, resolution):
        self.camera.resolution = resolution

    def set_camera(self, recording: bool):
        if recording:
            self.set_fps(settings.Camera.RECORD_FPS)
            self.set_resolution(settings.Camera.RECORD_RESOLUTION)
        else:
            self.set_fps(settings.Camera.MOVEMENT_FPS)
            self.set_resolution(settings.Camera.MOVEMENT_RESOLUTION)

    def start_recording(self, file_name):
        print('start record')
        self.camera.start_recording(file_name)

    def stop_recording(self):
        print('stop record')
        self.camera.stop_recording()

    def make_recording(self, file_name, record_time):
        self.start_recording(file_name)
        start_time = time.time()

        while time.time() - start_time < record_time:
            if self.stop:
                break
            time.sleep(0.5)

        self.stop_recording()

    def capture(self):
        for frame in self.camera.capture_continuous(self.raw_capture,
                                                    format='bgr',
                                                    use_video_output=True):
            image = frame.array
            self.raw_capture.truncate(0)
            self.image_queue.put(image)

            if self.record or self.stop:
                return

    def run(self) -> None:
        while not self.stop:
            self.set_camera(recording=False)
            self.capture()

            if self.record:
                self.set_camera(recording=True)
                self.make_recording('video.mjpeg', 5)
                self.record = False
