# python 3.7, 32
# os - win8.1, 64
import sys

# переменные программы
sum_ = 0
even_list = []

# служебная переменная
locals_ = {}

# начало программы
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0 and i not in even_list:
            even_list.append(i)
            sum_ += 1
# окончание программы

# служебные переменные, для того, чтобы сделать цикл по locals() без расширения самого locals()
item = 0
list_item = 0

# собираем все переменные модуля
for item in locals():
    locals_.update({item: sys.getsizeof(locals()[item])})
    if isinstance(locals()[item], list):
        for list_item in locals()[item]:
            locals_.update({f'list_item{list_item}': sys.getsizeof(list_item)})

# считаем сумму пользовательских переменных, без учета обязательных и служебных
sum_bytes = 0
for i in locals_:
    if '__' not in i:
        if i != 'sys' and i != 'locals_' and i != 'item' and i != 'list_item':
            sum_bytes += locals_[i]
            print(f'переменная {i} заняла {locals_[i]} байт')


print(f'переменные заняли: {sum_bytes} байт')