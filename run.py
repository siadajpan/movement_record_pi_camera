import queue
import time

from movement_recorder.camera.pi_camera import PiCamera

if __name__ == '__main__':
    image_queue = queue.Queue()
    cam = PiCamera(image_queue)
    cam.start()
    time.sleep(2)
    print('starting recording')
    cam.record = True
    time.sleep(6)
    print('stopping')
    cam.stop = True
