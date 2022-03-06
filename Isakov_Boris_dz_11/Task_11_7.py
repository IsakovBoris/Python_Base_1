class ComplexNumber:
    def __init__(self, number_x, number_y):
        self.number_x=number_x
        self.number_y=number_y

    def __str__(self):
        if self.number_y > 0:
            complex_number = f'{self.number_x} + {self.number_y}i'
        if self.number_y == 0:
            complex_number = f'{self.number_x} + i'
        else:
            complex_number = f'{self.number_x} - {self.number_y//self.number_y}i'
        return complex_number


    def __add__(self, other):
        new_number_x = self.number_x + other.number_x
        new_number_y = self.number_y + other.number_y
        return ComplexNumber(new_number_x, new_number_y)


    def __mul__(self, other):
        new_number_x = self.number_x * other.number_x + self.number_x * other.number_y
        new_number_y = self.number_y * other.number_x - self.number_y * other.number_y
        return ComplexNumber(new_number_x, new_number_y)


if __name__ == '__main__':
    number_1 = ComplexNumber(0, -1)
    print(number_1)
    number_2 = ComplexNumber(2, 0)
    print(number_2)
    sum_numbers = number_1 + number_2
    print(sum_numbers)
    multiply_numbers = number_1 * number_2
    print(multiply_numbers)
