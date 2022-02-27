from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, measure: float):
        self.measure = measure


    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    @property
    def calculate(self):
        fabric = self.measure / 6.5 + 0.5
        return round(fabric, 2)


class Costume(Clothes):
    @property
    def calculate(self):
        fabric = 2 * self.measure + 0.3
        return round(fabric, 2)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)
    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
