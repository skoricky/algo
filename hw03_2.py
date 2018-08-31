import random

SIZE = 100

list_ = [random.randint(0, SIZE) for i in range(0, SIZE)]
print(list_)
index_list = []

for idx, item in enumerate(list_):
    if item % 2 == 0:
        index_list.append(idx)

print(index_list)
