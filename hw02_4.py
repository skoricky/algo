# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

print('Введите количество цифр последовательности: 1.0 -0.5 0.25 -0.125...n')
n = int(input('n = '))


def nums(n, result='1.0', num=1.0, inx=0):
    if inx == n + 1:
        return result

    num = float(num / 2) * -1
    result += ' ' + str(num)
    return nums(n, result, num, inx + 1)


print('Итоговая последовательность:', nums(n))
