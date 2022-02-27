from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for el in range(len(matrix) - 1):
            if len(matrix[el]) != len(matrix[el + 1]):
                raise ValueError('fail initialization matrix')


    def __str__(self):
        output_matrix =('|'+' '+' '.join(map(str, self.matrix[0]))+' '+'|')
        for raw in range (1, len(self.matrix)):
            line = ' '.join(map(str, self.matrix[raw]))
            output_matrix = f'{output_matrix} \n| {line} | '
        return output_matrix


    def __add__(self, other):
        matrix_sum = [[self.matrix[i][j] + other.matrix[i][j] for j in range
        (len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(matrix_sum)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(first_matrix + second_matrix)
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
