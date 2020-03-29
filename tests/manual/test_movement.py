import cv2

from movement_recorder.movement_detector.movement_detector import \
    MovementDetector

if __name__ == '__main__':
    m = MovementDetector()
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        movement, foreground = m.analyze_image(frame)
        print(movement)
        cv2.imshow('f', foreground)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
