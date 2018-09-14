# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
#  случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

array_ = [round(random.uniform(0, 49), 2) for _ in range(0, 50)]
print(array_)


def merge_sort(random_array):
    if len(random_array) < 2:
        return random_array

    result = []

    i = 0
    j = 0

    median = len(random_array) // 2

    left_path = merge_sort(random_array[:median])
    right_path = merge_sort(random_array[median:])

    while i < len(left_path) and j < len(right_path):
        if left_path[i] <= right_path[j]:
            result.append(left_path[i])
            i += 1
        else:
            result.append(right_path[j])
            j += 1
    return result + left_path[i:] + right_path[j:]


print(merge_sort(array_))
