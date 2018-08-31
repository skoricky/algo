# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10

list_ = [random.randint(0, SIZE) for i in range(0, SIZE)]
print(list_)

max_ = -1
idx_max = 0
min_ = SIZE + 1
idx_min = 0
sum_ = 0

for idx, item in enumerate(list_):
    if item > max_:
        max_ = item
        idx_max = idx
    if item < min_:
        min_ = item
        idx_min = idx

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

print(idx_min, idx_max)

list_ = list_[idx_min + 1: idx_max]
print(list_)

for item in list_:
    sum_ += item

print(sum_)
