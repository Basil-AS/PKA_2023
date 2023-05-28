import math
from random import randint
from script.const import ABC as alphabet
from script.method import change_array, change_array_2, flip_vertical, flip_horizontal


def cardano_grid_cipher():
    question = str(input("Выполнить действие (шифровать/дешифоровать): "))
    proverb = input("Введите пословицу: ").lower()
    if question == 'шифровать':
        while True:
            grid_width = int(input('Введите сторону сетки кардано - четное число: '))
            if grid_width % 2 == 0:
                break
        grid_length = math.ceil(len(proverb) / grid_width)
        print('Длина сообщения: ', len(proverb))
        print('Рассчитаное число строк решётки: ', grid_length)
        if grid_length % 2 == 1:
            grid_length += 1
            print('Длина решётки - нечётное число, длина увеличена на 1')
        if len(proverb) != grid_width * grid_length:
            while len(proverb) != grid_width * grid_length:
                proverb += alphabet[randint(0, len(alphabet) - 1)]
            print('Сообщение дополнено символами, новый вид сообщения: ', proverb)
        else:
            print('Добавление букв не требуется')
        while True:
            grid_zeros = grid_width * grid_length * '0'
            for i in range(grid_length):
                rand_index = i * grid_width + randint(0, grid_width - 1)
                grid_zeros = grid_zeros[:rand_index] + '1' + grid_zeros[rand_index + 1:]
            while grid_zeros.count('1') != len(grid_zeros) / 4:
                rand_index = randint(0, len(grid_zeros) - 1)
                if grid_zeros[rand_index] == '0':
                    grid_zeros = grid_zeros[:rand_index] + '1' + grid_zeros[rand_index + 1:]
            count = 0
            for i in range(grid_length):
                for j in range(grid_width // 2):
                    if grid_zeros[i * grid_width + j] == '1' and grid_zeros[i * grid_width + grid_width - 1 - j] == '1':
                        count += 1
            for i in range(grid_width):
                for j in range(grid_length // 2):
                    if grid_zeros[j * grid_width + i] == '1' and grid_zeros[(grid_length - 1) * grid_width - grid_width * j + i] == '1':
                        count += 1
            for i in range(grid_length):
                for j in range(grid_width // 2):
                    if grid_zeros[i * grid_width + j] == '1' and grid_zeros[grid_width * (grid_length - i) - j - 1] == '1':
                        count += 1
            if count == 0:
                break
        array = []
        for item in range(len(grid_zeros)):
            array.append('0')
        print(proverb)
        print('Положения решётки Кардано:')
        print(grid_zeros)
        array, message = change_array(array, proverb, grid_zeros)
        grid_zeros = flip_horizontal(grid_zeros, grid_length, grid_width)
        array, message = change_array(array, message, grid_zeros)
        print(grid_zeros)
        grid_zeros = flip_vertical(grid_zeros, grid_length, grid_width)
        array, message = change_array(array, message, grid_zeros)
        print(grid_zeros)
        grid_zeros = flip_horizontal(grid_zeros, grid_length, grid_width)
        array, message = change_array(array, message, grid_zeros)
        print(grid_zeros)
        print('Результат шифрования:')
        print(''.join(array))
    if question == 'дешифоровать':
        grid_zeros = str(input('Введите первое положение решётки Кардано: '))
        while True:
            grid_width = int(input('Введите сторону сетки кардано - четное число: '))
            if grid_width % 2 == 0:
                break
        grid_length = math.ceil(len(proverb) / grid_width)
        print('Длина сообщения: ', len(proverb))
        print('Рассчитаное число строк решётки: ', grid_length)
        if grid_length % 2 == 1:
            grid_length += 1
        array = []
        count_change = 0
        for item in range(len(grid_zeros)):
            array.append('0')
        print(proverb)
        print('Положения решётки Кардано:')
        print(grid_zeros)
        array, count_change = change_array_2(array, proverb, grid_zeros, count_change)
        grid_zeros = flip_horizontal(grid_zeros, grid_length, grid_width)
        array, count_change = change_array_2(array, proverb, grid_zeros, count_change)
        print(grid_zeros)
        grid_zeros = flip_vertical(grid_zeros, grid_length, grid_width)
        array, count_change = change_array_2(array, proverb, grid_zeros, count_change)
        print(grid_zeros)
        grid_zeros = flip_horizontal(grid_zeros, grid_length, grid_width)
        array, count_change = change_array_2(array, proverb, grid_zeros, count_change)
        print(grid_zeros)
        print('Результат расшифровки:')
        print(''.join(array))

cardano_grid_cipher()