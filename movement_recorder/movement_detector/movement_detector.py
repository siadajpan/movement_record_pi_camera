import cv2
import numpy as np

from movement_recorder import settings


class MovementDetector:
    def __init__(self):
        # self.movement_boxes: List[Rectangle] = []
        self.background_subtractor = cv2.createBackgroundSubtractorKNN(
            history=settings.PreProcessing.HISTORY,
            dist2Threshold=settings.PreProcessing.DIST_TO_THRESHOLD,
            detectShadows=settings.PreProcessing.DETECT_SHADOWS
        )
        # self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    def check_mean_threshold(self, binary_image):
        mean_above_threshold = np.mean(binary_image) \
                               > settings.PreProcessing.MOVEMENT_MEAN_THRESHOLD

        return mean_above_threshold

    def analyze_image(self, image: np.array):
        foreground = self.background_subtractor.apply(image)
        movement = self.check_mean_threshold(foreground)

        return movement, foreground
