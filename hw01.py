# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

X = input('Введите трехзначное число: ')
Y = int(X[0]) + int(X[1]) + int(X[2])
Z = int(X[0]) * int(X[1]) * int(X[2])

print(f'Сумма цифр числа: {Y}')
print(f'Произведение цифр числа: {Z}')


# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.
# При побитовом "И" числа побитово умножаются, то есть там где 1 и 1 остается 1, там где 1 и 0 остается 0.
# При побитовом "ИЛИ" числа побитово складываются, то есть там где один из битов 1, остается 1, оба бита 0 остается 0.
# При побитовом сдвиге влево в младшие разряды мы дописываем нули справа,  по количеству бит, на которое сдвигаем,
# фактически число увеличивается.
# При сдвиге вправо мы убираем биты справа, дописываем нули слева, в старшие разряды, по количеству бит,
# на которое сдвигаем, число уменьшается

Y = 5 | 6
print('Побитовое ИЛИ чисел 5 и 6:', Y)

Y = 5 & 6
print('Побитовое И чисел 5 и 6:', Y)

Y = 5 >> 2
print('Побитовый здвиг цифры 5 на 2 бита вправо:', Y)

Y = 5 << 2
print('Побитовый здвиг цифры 5 на 2 бита влево:', Y)


# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

print('Введите последовательно координаты двух точек в формате X1, Y1, X2, Y2')
X1 = int(input('X1 = '))
Y1 = int(input('Y1 = '))
X2 = int(input('X2 = '))
Y2 = int(input('Y2 = '))

K = (Y1 - Y2) / (X1 - X2)
B = Y2 - (K * X2)

print(f'Уравнение имеет вид Y = {K}X + {B}')


# 4. Написать программу, которая генерирует в указанных пользователем границах:
# Случайное целое;
# Случайное вещественное;
# Случайный символ.
# Например, если надо получить случайный символ от 'a' до 'f' то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

print('Введите границы числовой последовательности или последовательности букв в формате \'А =\', \'В = \'')
A = input('A = ').upper()
B = input('B = ').upper()

if A not in [str(i) for i in range(10)]:
    if ord(A) < ord(B):
        X = ord(A)
        Y = ord(B)
        string = (A, B)
    else:
        X = ord(B)
        Y = ord(A)
        string = (B, A)
    D = random.randint(X, Y)
    C = chr(D)
    print(f'Случайная буква из последовательности [{string[0]}...{string[1]}]: {C}')
else:
    if not float(A) < float(B):
        A, B = B, A

    if '.' in A or '.' in B:
        C = round(random.uniform(float(A), float(B)), 2)
    else:
        C = random.randint(int(A), int(B))
    print(f'Случайная цифра из последовательности [{A}...{B}]: {C}')


# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Введите две буквы русского алфавита')
A = input('Первая буква = ').upper()
B = input('Вторая буква = ').upper()

N0 = ord('А')
NA = ord(A)
NB = ord(B)

NX = NA - N0 + 1
NY = NB - N0 + 1

N = abs(NX - NY) - 1

print(f'Индекс первой буквы равен: {NX}\n'
      f'Индекс второй буквы равен: {NY}\n'
      f'Число букв между ними равно: {N}')


# 6. Пользователь вводит номер буквы в алфавите. Определить, какая эта буква

NA = int(input('Введите нормер буквы в русском алфавите: '))
N0 = ord('А')

NX = NA + N0 - 1
A = chr(NX)

print(f'Буква {A}')

# 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

print('Введите длины трех отрезков по очереди')
A = float(input('A = '))
B = float(input('B = '))
C = float(input('C = '))

if A + B > C and A + C > B and B + C > A:
    if A == B and B == C:
        print('Отрезки образуют треугольник равносторонний')
    else:
        if A == B or B == C or A == C:
            print('Отрезки образуют равнобедренный треугольник')
        else:
            print('Отрезки образуют треугольник с неравными сторонами')
else:
    print('Отрезки не образуют треугольник')


# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

X = int(input('Введите год: '))
X = X % 400

if X == 0:
    print('Введеный год високосный')
else:
    print('Введенный год обычный')


# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите последовательно три разных числа')
X = float(input('X = '))
Y = float(input('Y = '))
Z = float(input('Z = '))

A = X
B = Y
C = Z

if not A < B:
    A = Y
    B = X

if B < C:
    print('Число, являющееся средним:', B)
else:
    print('Число, являющееся средним:', C)






