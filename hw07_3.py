# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой – не больше ее.


import random

SIZE = 10

array_ = [random.randint(0, 2 * SIZE) for _ in range(0, 2 * SIZE + 1)]

# исходный массив
print(array_)
# печатаем сортированный для удобства
print(sorted(array_))

# индекс середины
idx = len(array_) // 2 + 1
median = None

for i in range(0, 2 * SIZE + 1):
    if i in array_:
        # при повторах числа убавляем искомый индекс середины
        idx = idx - array_.count(i)
        # print(idx, i)
        if idx <= 0:
            median = i
            break


print('median', median)

