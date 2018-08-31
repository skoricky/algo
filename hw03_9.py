import random

ROWS = 5
COLUMNS = 4

SIZE = 10

matrix_ = [[random.randint(0, SIZE) for _ in range(COLUMNS)] for _ in range(ROWS)]

# Вывожу матрицу
for i in range(ROWS):
    for j in range(COLUMNS):
        print(f'{matrix_[i][j]:^5}', end='')
    print()

max_min_list = []
max_ = -1

for i in range(COLUMNS):
    min_ = SIZE + 1

    for j in range(ROWS):
        if matrix_[j][i] < min_:
            min_ = matrix_[j][i]

    max_min_list.append(min_)

for i in max_min_list:
    if max_ < i:
        max_ = i

print('\nмаксимальный из минимумов столбцов:', max_)