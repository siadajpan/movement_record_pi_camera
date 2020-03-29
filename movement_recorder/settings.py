class Files:
    SAVING_FOLDER = '/home/pi/Videos'


class Camera:
    MOVEMENT_FPS = 10
    MOVEMENT_RESOLUTION = (640, 480)
    RECORD_FPS = 20
    RECORD_RESOLUTION = (1920, 1080)
    RECORD_EXTENSION = 'mjpeg'
    RECORD_TIME = 5


class PreProcessing:
    HISTORY = 40
    DIST_TO_THRESHOLD = 300
    DETECT_SHADOWS = False
    MOVEMENT_MEAN_THRESHOLD = 10
