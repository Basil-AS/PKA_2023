""" Лабораторная работа 3. Шифры блочной замены

1.Зашифровать текст вручную по своему варианту из  файла ВАРИАНТЫ ЗАДАНИЙ, как минимум, одним из шифров блочной замены: Блок С: ШИФРЫ БЛОЧНОЙ ЗАМЕНЫ* :

8.Матричный шифр (матрица-ключ не меньше 3х3)
9.Шифр Плэйфера – шифр биграммной замены


2. Написать программу для выбранных шифров блочной замены (отладка и тестирование программы по своему варианту из  файла ВАРИАНТЫ ЗАДАНИЙ), при этом предусмотреть ввод ключевых параметров и их проверку.

3. Проверить работу программы на тексте не менее 1000 символов.

4. Подготовить отчет в соответствие с требованиями  Методических указаний*.
https://online.mospolytech.ru/mod/assign/view.php?id=227055"""

from color_output import Color, color_print
from sympy import Matrix
import numpy as np

ALPH = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def matrix_cipher(input_text, alphabet):
    size = int(input('Введите размер квадратной матрицы (число от 3 и далее): '))
    if len(input_text) % size != 0:
        input_text = input_text + ((size - (len(input_text) % size)) * 'ф')

    key = []
    for i in range(size):
        key.append([0] * size)

    count = 1
    for i in range(size):
        for j in range(size):
            key[i][j] = input('Введите {}-ый элемент матрицы: '.format(count))
            count += 1
            if key[i][j] == '':
                print('Матрица заполнена пустыми элементами')
                exit()

    keynp = np.array(key, dtype=np.int32)

    if np.linalg.det(keynp) == 0:
        print('Детерминант матрицы равен нулю, попробуйте ввести другую')
        exit()

    result = []
    counter = 0
    for k in range(int(len(input_text) / (size))):
        text_to_matr = []
        for i in range(size):
            text_to_matr.append(alphabet.index(''.join([input_text[counter]])) + 1)
            counter = counter + 1
        result.append(list(np.dot(keynp, text_to_matr)))

    code = ''
    for i in range(len(result)):
        for j in range(size):
            code = code + str(result[i][j]) + ' '

    return code


if __name__ == '__main__':
    color_print("Скрыпник Василий 211-331 Лаб 3 Шифры блочной замены", color=Color.BLUE, bold=True)
    input_text = input("\033[36m\033[1mВведите строку: \033[0m").lower()

    while True:
        choice = input("\033[1m\033[32mВыберете действие:\n8.Матричный шифр \n9.Шифр Плэйфера \n0.Выход\n\033[0m")

        if choice == '8':
            encrypted_text = matrix_cipher(input_text, ALPH)
            color_print("Результат матричного шифрования:", color=Color.MAGENTA, bold=True)
            print(encrypted_text)

        elif choice == '9':
            pass

        elif choice == '0':
            break
