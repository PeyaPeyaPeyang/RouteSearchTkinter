from abc import ABCMeta, abstractmethod


class Algorithm(metaclass=ABCMeta):
    @abstractmethod
    def on_step(self):
        pass

    @abstractmethod
    def on_bt(self):
        pass

