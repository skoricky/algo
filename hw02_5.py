# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

print('\nСимволы ASCII c 32 по 127:\n')


def rows_ascii(row='', row_cells=0, inx=32, inx_stop=128):
    if inx == inx_stop:
        return row

    if row_cells == 10:
        row_cells = 0
        row += '\n'

    row += f'{inx: >5}: {chr(inx): ^5} '
    return rows_ascii(row, row_cells + 1, inx + 1, inx_stop)


print(rows_ascii())
