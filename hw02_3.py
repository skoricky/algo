# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

print('Введите натуральное число:')
num = int(input('Число = '))


def invert_num(num, invert_num_='', inx=0):
    if int(num % 10 ** (inx + 1) / 10 ** inx) == 0:
        return invert_num_

    invert_num_ += str(int(num % 10 ** (inx + 1) / 10 ** inx))
    return invert_num(num, invert_num_, inx + 1)


print('Ваше число в обратном порядке =', invert_num(num))
