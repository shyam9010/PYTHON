from abc import ABC, abstractmethod


class vehicle(ABC):
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass


class car(vehicle):
    def __init__(self, fuel_type, speed, color):
        super().__init__(speed, color)
        self.fuel_type = fuel_type

    def start(self):
        self.speed = self.speed + 1000
        return self.speed

    def stop(self):
        self.stop = self.stop - 1000


class bicycle(vehicle):
    def __init__(self, no_of_gears, speed, color):
        super().__init__(speed, color)
        self.no_of_gears = no_of_gears

    def start(self):
        self.no_of_gears = self.no_of_gears + 1

    def stop(self):
        self.no_of_gears = self.no_of_gears - 1


vehicle1 = car("diesel", 100, "white")
print(vehicle1.start())
