# Написать два алгоритма нахождения i-того по счету простого числа.
# Первый - использовать алгоритм "решето Эротосфена".
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

from functools import lru_cache
from datetime import datetime

import cProfile

def get_erotos_number(count):
    erotos_list = []
    list_ = [i for i in range(2, count ** 2 + 1)]

    for idx, number in enumerate(list_, 2):
        if number != -1:
            if len(erotos_list) == count - 1:
                erotos_list.append(number)
                break
            else:
                erotos_list.append(number)

            j = number ** 2
            next_ = 1

            while j <= len(list_) - 1:
                list_[j - 2] = -1
                j = number ** 2 + (next_ * number)
                next_ += 1
    return erotos_list[-1]

# F:\PycharmProjects\pydb\hw04>python -m timeit -n 10 -s"import hw04_2" "hw04_2.get_erotos_number(100)"
# 10 loops, best of 5: 17.6 msec per loop

# F:\PycharmProjects\pydb\hw04>python -m timeit -n 10 -s"import hw04_2" "hw04_2.get_erotos_number(1001)"
# 10 loops, best of 5: 2.17 sec per loop


def get_prime_number(count):
    erotos_list = []
    list_ = [i for i in range(2, count ** 2 + 1)]

    for i in list_:
        key_ = True
        if len(erotos_list) == count:
            for j in range(2, i + 1):
                if i % j == 0 and i != j:
                    key_ = False
                    break
            if key_:
                erotos_list.append(i)
            break
        else:
            for j in range(2, i + 1):
                if i % j == 0 and i != j:
                    key_ = False
                    break
            if key_:
                erotos_list.append(i)
    return erotos_list[-1]

# F:\PycharmProjects\pydb\hw04>python -m timeit -n 10 -s"import hw04_2" "hw04_2.get_prime_number(100)"
# 10 loops, best of 5: 3.33 msec per loop

# F:\PycharmProjects\pydb\hw04>python -m timeit -n 10 -s"import hw04_2" "hw04_2.get_prime_number(1001)"
# 10 loops, best of 5: 466 msec per loop


def get_prime_number_n(count):

    prime_ = 0
    prime_count = 0
    i = 2

    while prime_count < count:
        key_ = True
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                key_ = False
                break
        if key_:
            prime_ = i
            prime_count += 1
        i += 1
    return prime_

# F:\PycharmProjects\pydb\hw04>python -m timeit -n 10 -s"import hw04_2" "hw04_2.get_prime_number(100)"
# 10 loops, best of 5: 3.32 msec per loop

# F:\PycharmProjects\pydb\hw04>python -m timeit -n 10 -s"import hw04_2" "hw04_2.get_prime_number_n(1001)"
# 10 loops, best of 5: 386 msec per loop


#          2129435 function calls in 2.456 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.008    0.008    2.456    2.456 <string>:1(<module>)
#         1    2.226    2.226    2.448    2.448 hw04_2.py:40(get_erotos_number)
#         1    0.067    0.067    0.067    0.067 hw04_2.py:42(<listcomp>)
#         1    0.000    0.000    2.456    2.456 {built-in method builtins.exec}
#   2128429    0.155    0.000    0.155    0.000 {built-in method builtins.len}
#      1001    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          8933 function calls in 0.473 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.014    0.014    0.473    0.473 <string>:1(<module>)
#         1    0.398    0.398    0.459    0.459 hw04_2.py:65(get_prime_number)
#         1    0.060    0.060    0.060    0.060 hw04_2.py:67(<listcomp>)
#         1    0.000    0.000    0.473    0.473 {built-in method builtins.exec}
#      7927    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      1001    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.399 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.399    0.399 <string>:1(<module>)
#         1    0.399    0.399    0.399    0.399 hw04_2.py:93(get_prime_number_n)
#         1    0.000    0.000    0.399    0.399 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


if __name__ == '__main__':
    print(get_erotos_number(40))
    print(get_prime_number(40))
    print(get_prime_number_n(40))

    cProfile.run('get_erotos_number(1001)')
    cProfile.run('get_prime_number(1001)')
    cProfile.run('get_prime_number_n(1001)')

