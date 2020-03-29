class Files:
    SAVING_FOLDER = '/home/pi/Videos'


class Camera:
    BG = 1.3
    RG = 1.1
    MOVEMENT_FPS = 2
    MOVEMENT_RESOLUTION = (320, 240)
    RECORD_FPS = 20
    RECORD_RESOLUTION = (1920, 1080)
    RECORD_EXTENSION = 'mjpeg'
    RECORD_TIME = 5


class PreProcessing:
    HISTORY = 10
    DIST_TO_THRESHOLD = 300
    DETECT_SHADOWS = False
    MOVEMENT_MEAN_THRESHOLD = 10
