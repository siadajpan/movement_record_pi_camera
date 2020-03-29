from abc import ABC, abstractmethod
from threading import Thread


class AbstractCamera(ABC, Thread):
    @abstractmethod
    def start_recording(self):
        pass

    @abstractmethod
    def stop_camera(self):
        pass

    @property
    def image_queue(self):
        return None

    @abstractmethod
    def run(self) -> None:
        pass
