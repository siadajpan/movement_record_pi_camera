import queue

from movement_recorder.camera.web_camera import WebCamera
from movement_recorder.controller import Controller
from movement_recorder.movement_detector.movement_detector import \
    MovementDetector

if __name__ == '__main__':
    image_queue = queue.Queue()
    camera = WebCamera(image_queue)
    movement_detector = MovementDetector()
    controller = Controller(camera, movement_detector)
    controller.run()
