import logging
import queue

from movement_recorder.camera.pi_camera import PiCamera
from movement_recorder.controller import Controller
from movement_recorder.movement_detector.movement_detector import \
    MovementDetector

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    image_queue = queue.Queue()
    camera = PiCamera(image_queue)
    movement_detector = MovementDetector()
    controller = Controller(camera, movement_detector)
    controller.run()
