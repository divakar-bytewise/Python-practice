from abc import ABC, abstractmethod

class Bike(ABC):
    @abstractmethod
    def move_forward(self):
        pass

    @abstractmethod
    def move_backword(self):
        pass

    @abstractmethod
    def gear(self):
        pass

class RE(Bike):
    def move_forward(self):
        print("Moving forward")

    def move_backword(self):
        print("Moving backward")

    def gear(self):
        print("There are 6 gears")

RE=RE()
RE.gear()