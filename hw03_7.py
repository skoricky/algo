import random

SIZE = 25

list_ = [random.randint(0, SIZE) for i in range(0, SIZE)]
print(list_)
min_1 = min_2 = SIZE + 1

for item in list_:
    if item < min_1:
        min_1 = item

for item in list_:
    if min_1 < item < min_2:
        min_2 = item

print(f'наименьшее минимальное {min_1}')
print(f'второе минимальное {min_2}')
