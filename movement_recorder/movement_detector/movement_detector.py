import cv2
import numpy as np

from movement_recorder import settings


class MovementDetector:
    def __init__(self):
        self.background_subtractor = cv2.createBackgroundSubtractorKNN(
            history=settings.PreProcessing.HISTORY,
            dist2Threshold=settings.PreProcessing.DIST_TO_THRESHOLD,
            detectShadows=settings.PreProcessing.DETECT_SHADOWS
        )
        self.history_count = 0
        self.full_history_count = settings.PreProcessing.HISTORY

    def _check_mean_threshold(self, binary_image):
        mean_above_threshold = np.mean(binary_image) \
                               > settings.PreProcessing.MOVEMENT_MEAN_THRESHOLD

        return mean_above_threshold

    def reset_history_count(self):
        self.history_count = 0

    def _check_history_count(self):
        print(f'history count:{self.history_count}/{self.full_history_count}')
        if self.history_count <= self.full_history_count:
            self.history_count += 1
            return False
        else:
            return True

    def analyze_image(self, image: np.array):
        foreground = self.background_subtractor.apply(image)

        movement = False
        if self._check_history_count():
            movement = self._check_mean_threshold(foreground)
        print(f'++++++++ movement : {movement} +++++++++')
        return movement, foreground
