# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random

# Алгоритм "странный пузырек", скорее это "метод кругов на воде")
array_ = [random.randint(-100, 99) for _ in range(-100, 100)]

print(array_)

len_array = len(array_) - 1
idx = 0

while idx < len_array:
    flag = False

    n = 1
    print(len_array)

    while n <= len_array:
        if array_[n - 1] < array_[n]:
            flag = True
            array_[n - 1], array_[n] = array_[n], array_[n - 1]
            k = n - 1
            while k > 0:
                if array_[k - 1] < array_[k]:
                    array_[k - 1], array_[k] = array_[k], array_[k - 1]
                k -= 1
        n += 1

    print(array_)

    if not flag:
        break

    idx += 1
    len_array -= 1
