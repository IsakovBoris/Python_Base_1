class Cell:


    def __init__(self, cells: int):
        self.cells = cells


    def check_cell(self, other):
        if type(self) != type(other):
            raise TypeError(f'действие допустимо только для экземпляров того же класса')


    def make_order(self, number: int) -> str:
        if self.cells <= number:
            result = self.cells * '*'
        else:
            result = number * '*'
            rest = self.cells - number
            while rest > 0:
                if rest >= number:
                    stars = number * '*'
                else:
                    stars = rest * '*'
                result = f'{result} \n{stars}'
                rest -= number
        return result


    def __add__(self, other):
        self.check_cell(other)
        sum = self.cells + other.cells
        return Cell(sum)


    def __sub__(self, other):
        self.check_cell(other)
        if self.cells > other.cells:
            diff = self.cells - other.cells
        else:
            raise ValueError('недопустимая операция')
        return Cell(diff)


    def __mul__(self, other):
        self.check_cell(other)
        mul = self.cells * other.cells
        return Cell(mul)


    def __truediv__(self, other):
        self.check_cell(other)
        truediv = int(self.cells / other.cells)
        return Cell(truediv)


    def __floordiv__(self, other):
        self.check_cell(other)
        floordiv = self.cells // other.cells
        return Cell(floordiv)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)
    print(cell_1.make_order(10))
    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)
    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)
    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)
    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)
    try:
        cell_1 * 123
    except TypeError as err:
        print(err)
