# Написать программу сложения и умножения двух шеснадцатиричных чисел.
# При этом каждое число представлять как массив, элементы которого - это цифры числа.

from collections import deque

list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']


# Вместо массива реализовал tuple
# К сожалению успел только сложение
# Огнаничения: необходио цифры, которые записываются не буквами указывать в формате int
def calc_16(number_1: tuple, number_2: tuple, operator='+'):
    result = deque([])

    num_1 = deque(number_1)
    num_1.reverse()
    num_2 = deque(number_2)
    num_2.reverse()

    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1

    if operator == '+':
        for idx, i in enumerate(num_1):
            # Проверка соответствия разрядности чисел
            if idx >= len(num_2):
                if len(num_1) == len(result):
                    # Складываю в старшем разряде, если разряд не пустой
                    # для этого забираю значение страшго разряда и рекурсивно запускаю функцию
                    temp = calc_16((result.popleft(),), (i,))
                    temp.reverse()

                    # Заполняю результат, начиная со старшего разряда
                    for n in temp:
                        result.appendleft(n)
                else:
                    result.appendleft(i)
                return result

            # Определяем индексы табличного значения
            idx_1 = list_1.index(i)
            idx_2 = list_1.index(num_2[idx])
            # Табличные значения
            table_num = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'], maxlen=16)
            # Аккумулятор старшего разряда, суда запишется 1 при свиге табличных значений
            master_ = deque([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], maxlen=16)

            # Делаем свиг табличных значений, для того чтобы исчисление начиналось с цифры первого числа, над которым
            # проводится вычисление
            for _ in range(0, idx_1):
                n_ = table_num.popleft()
                table_num.append(n_)
                master_.append(1)

            if len(result) - 1 < idx:
                result.appendleft(table_num[idx_2])
                if master_[idx_2] > 0:
                    result.appendleft(master_[idx_2])
            else:
                # Складываю в старшем разряде, если старший разряд не пустой
                if master_[idx_2] > 0:
                    temp = calc_16((result.popleft(),), (1, table_num[idx_2]))
                    temp.reverse()
                else:
                    temp = calc_16((result.popleft(),), (table_num[idx_2],))
                    temp.reverse()

                for n in temp:
                    result.appendleft(n)

    return result


if __name__ == '__main__':
    a = calc_16(('a', 2,), ('c', 4, 'f'))
    print(''.join([str(i) for i in a]))