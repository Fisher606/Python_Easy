# Создайте класс Матрица.
# Добавьте методы для:
# 1) вывода на печать
# 2) сравнения
# 3) сложения
# 4) умножения матриц

import numpy as np


class Matrix:


    def __init__(self, list_of_lists: list):

        self.list_of_lists = np.array(list_of_lists)

    def __add__(self, other):
        return self.list_of_lists + other.list_of_lists

    def __mul__(self, other):
        return self.list_of_lists.dot(other.list_of_lists)

    def __eq__(self, other):
        return np.array_equal(self.list_of_lists, other.list_of_lists)

    def __str__(self):
        return f'{self.list_of_lists}'

    def __repr__(self):
        return f'({self.list_of_lists = })'


if __name__ == "__main__":
    arr1 = Matrix([[1, 2, 3], [1, 3, 4]])
    arr2 = Matrix([[2, 3], [5, 6], [3, 4]])

    print(arr1 * arr2)
    print(arr1 == arr2)