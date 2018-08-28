# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print('Введите натуральное число:')
num = input('Число = ')


def sum_even_digits(num_string, ev_sum=0, od_sum=0, inx=0):
    if inx == len(num_string):
        return f'четных цифр - {ev_sum}, нечетных цифр - {od_sum}'

    if int(num_string[inx]) % 2 == 0:
        return sum_even_digits(num_string, ev_sum + 1, od_sum, inx + 1)
    else:
        return sum_even_digits(num_string, ev_sum, od_sum + 1, inx + 1)


print('Во веденном числе', sum_even_digits(num))
