import sys


class Stationery:


    def __init__(self, title: str) -> None:
        self.title = title


    def draw(self) -> None:
        sys.stdout.write(f'Запуск отрисовки\n')


class Pen(Stationery):


    def draw(self) -> None:
        sys.stdout.write(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"\n')


class Pencil(Stationery):


    def draw(self) -> None:
        sys.stdout.write(f'Запуск отрисовки\n')
        sys.stdout.write(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"\n')


class Handle(Stationery):


    def draw(self) -> None:
        sys.stdout.write(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"\n')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()
    handle.draw()
    pencil.draw()
