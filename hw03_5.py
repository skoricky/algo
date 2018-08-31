import random

SIZE = 100

list_ = [random.randint(SIZE // 2 * -1, SIZE // 2) for i in range(SIZE // 2 * -1, SIZE // 2)]
print(list_)

num_ = 0
idx_ = 0

# Беру первый индекс максимального отрицательного числа в массиве
for idx, item in enumerate(list_):
    if item < 0:
        if num_ < item or num_ == 0:
            num_ = item
            idx_ = idx

print(f'значение {num_}, индекс {idx_}')
