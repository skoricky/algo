import random

SIZE = 10

list_ = [random.randint(0, SIZE) for i in range(0, SIZE)]
print(list_)
num_ = 0
times_ = 0
sub_times_ = 0

for i in list_:
    sub_times_ = 0

    for j in list_:
        if j == i:
            sub_times_ += 1

    if sub_times_ > times_:
        times_ = sub_times_
        num_ = i

print(num_, f'--> количество {times_}')
