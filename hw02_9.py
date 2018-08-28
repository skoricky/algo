# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

print('Введите последовательность чисел через пробел, например: 100 77 8 109')
in_put = input('Ваша последовательность: ')


def get_biggest_digits_sum(numbers_string, digits_dict, subsum=0, sum=0, inx=0, digits=''):
    if inx == len(numbers_string):
        digits_dict.update({subsum: digits})
        return max(subsum, sum), digits_dict[max(subsum, sum)]

    if len(numbers_string) == 1:
        return numbers_string

    if numbers_string[inx] != ' ':
        subsum += int(numbers_string[inx])
        digits += numbers_string[inx]
        return get_biggest_digits_sum(numbers_string, digits_dict, subsum, sum, inx + 1, digits)
    else:
        digits_dict.update({subsum: digits})
        return get_biggest_digits_sum(numbers_string, digits_dict, 0, max(subsum, sum), inx + 1, '')


sum_ = get_biggest_digits_sum(in_put, {})
print('Наибольшая сумма цифр в представленных числах =', sum_[0], f'(число - {sum_[1]})')
