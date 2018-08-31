import random

SIZE = 10

list_ = [random.randint(0, SIZE) for i in range(0, SIZE)]
print(list_)
max_ = -1
min_ = SIZE + 1

# Меняю в массиве все миниальные на максимальные, а максимальные на минимальные
for item in list_:
    if item > max_:
        max_ = item
    if item < min_:
        min_ = item

for idx, item in enumerate(list_):
    if item == max_:
        list_[idx] = min_
    elif item == min_:
        list_[idx] = max_

print(list_)