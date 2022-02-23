import sys


class Car:
    is_police: bool = False


    def __init__(self, speed: int, colour: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed = speed
        self.colour = colour
        self.name = name


    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed = self.speed + 15
        sys.stdout.write(f'Машина {self.name} повысила скорость на 15: {self.speed}\n')


    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        sys.stdout.write(f'{self.name}: остановилась\n')


    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        self.direction = direction
        if self.direction != 'направо' and self.direction != 'налево' and self.direction != 'прямо' and self.direction != 'назад':
            raise ValueError('нераспознанное направление движения\n')
        else:
            sys.stdout.write(f'{self.name}: движется {direction}\n')


    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.is_police != True:
            sys.stdout.write(f'{self.name}: текущая скорость {self.speed} км/час\n')
        else:
            sys.stdout.write(f'{self.name}: текущая скорость {self.speed} км/час\n')
            sys.stdout.write(f'Вруби мигалку и забудь про скорость!\n')


class TownCar(Car):


    def show_speed(self) -> None:
        if self.speed > 60:
            sys.stdout.write(f'Alarm!!! Speed!!!\n')
        else:
            sys.stdout.write(f'{self.name}: текущая скорость {self.speed} км/час\n')


class WorkCar(Car):


    def show_speed(self) -> None:
        if self.speed > 40:
            sys.stdout.write(f'Alarm!!! Speed!!!\n')
        else:
            sys.stdout.write(f'{self.name}: текущая скорость {self.speed} км/час\n')


class SportCar(Car):
    pass

class PoliceCar(Car):
    is_police: bool = True



if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()
    town_car.show_speed()
    work_car.show_speed()
    town_car.stop()
    police_car.show_speed()
    sport_car.turn('назад')
    sport_car.turn('right')
