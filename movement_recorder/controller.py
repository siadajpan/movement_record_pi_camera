import queue

from movement_recorder.camera.pi_camera import PiCamera
from movement_recorder.movement_detector.movement_detector import \
    MovementDetector


class Controller:
    def __init__(self, camera: PiCamera, movement_detector: MovementDetector):
        self.camera = camera
        self.movement_detector = movement_detector

    def process_movement(self, movement):
        if movement:
            self.camera.start_recording()

    def process_image(self):
        image = self.camera.image_queue.get()
        movement, _ = self.movement_detector.analyze_image(image)
        self.process_movement(movement)

    def run(self):
        self.camera.start()
        while True:
            try:
                self.process_image()
            except KeyboardInterrupt:
                break
        self.camera.stop_camera()
