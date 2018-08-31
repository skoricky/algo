# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

sum_ = 0
even_list = []

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0 and i not in even_list:
            even_list.append(i)
            sum_ += 1

print(sum_)