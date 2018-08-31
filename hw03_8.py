# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

ROWS = 5
COLUMNS = 4

matrix_ = [[-1 for _ in range(COLUMNS)] for _ in range(ROWS)]

for i in range(ROWS):
    sum_ = 0
    for j in range(COLUMNS - 1):
        matrix_[i][j] = int(input(f'введи заначение (целое число) строки {i + 1} столбца {j + 1} '))
        sum_ += matrix_[i][j]
    matrix_[i][COLUMNS - 1] = sum_

for i in range(ROWS):
    for j in range(COLUMNS):
        print(f'{matrix_[i][j]:^5}', end='')
    print()
