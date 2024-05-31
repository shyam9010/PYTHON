from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class rectangle(shape):
    def __init__(self, lenght, breath):
        self.lenght = lenght
        self.breath = breath

    def area(self):
        return self.lenght * self.breath

    def perimeter(self):
        return 2 * (self.lenght + self.breath)


class square(rectangle):
    def __init__(self, lenght):
        super().__init__(lenght, lenght)


square1 = square(2)
print(square1.area())
