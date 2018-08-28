# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

print('Введите последовательность чисел через пробел, например: 100 77 8 109')
in_put = input('Ваша последовательность: ')
number = input('Искомая цифра: ')


def get_sum_digit_times(numbers_string, number, inx=0, sum=0):
    if inx == len(numbers_string):
        return sum

    if numbers_string[inx] == number:
        return get_sum_digit_times(numbers_string, number, inx + 1, sum + 1)
    else:
        return get_sum_digit_times(numbers_string, number, inx + 1, sum)


print('Количество цифр, равных искомой:', get_sum_digit_times(in_put, number))