class Files:
    SAVING_FOLDER = '/home/pi/Videos'


def calculate_resolution(resolution, zoom):
    w, h = resolution
    new_w = int(w * zoom[2])
    new_h = int(w * zoom[3])

    return new_w, new_h


class Camera:
    BG = 1.3
    RG = 1.1
    ZOOM = (0.35, 0.3, 0.3, 0.3)  # x, y, w, h
    MOVEMENT_RESOLUTION_ORIGINAL = (320, 240)
    MOVEMENT_RESOLUTION = calculate_resolution(MOVEMENT_RESOLUTION_ORIGINAL,
                                               ZOOM)
    RECORD_FPS = 20
    RESOLUTION_ORIGINAL = (3280, 2464)
    RESOLUTION = calculate_resolution(RESOLUTION_ORIGINAL,
                                      ZOOM)

    RECORD_EXTENSION = 'mjpeg'
    SAVE_EXTENSION = 'avi'
    RECORD_TIME = 10


class PreProcessing:
    HISTORY = 10
    DIST_TO_THRESHOLD = 300
    DETECT_SHADOWS = False
    MOVEMENT_MEAN_THRESHOLD = 10
