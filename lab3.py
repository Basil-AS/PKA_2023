# 1.Зашифровать текст вручную по своему варианту из  файла ВАРИАНТЫ ЗАДАНИЙ, как минимум, одним из шифров блочной замены: Блок С: ШИФРЫ БЛОЧНОЙ ЗАМЕНЫ* :

# 8.Матричный шифр (матрица-ключ не меньше 3х3)
# 9.Шифр Плэйфера – шифр биграммной замены


# 2. Написать программу для выбранных шифров блочной замены (отладка и тестирование программы по своему варианту из  файла ВАРИАНТЫ ЗАДАНИЙ), при этом предусмотреть ввод ключевых параметров и их проверку.

# 3. Проверить работу программы на тексте не менее 1000 символов.

# 4. Подготовить отчет в соответствие с требованиями  Методических указаний*.
# https://lms.mospolytech.ru/mod/assign/view.php?id=227055

from color_output import color_print, Color
import numpy as np

def matrix_cipher(text, alphabet):
    key_matrix = np.array([[1, 4, 8] , [3, 7, 2], [6, 9, 5]])
    
    # Дополняем текст до кратного размеру ключевой матрицы
    while len(text) % 3 != 0:
        text += alphabet[0]

    num_equivalent = [alphabet.index(char) + 1 for char in text]  # Используем индекс + 1 вместо индекса
    num_vectors = np.array_split(np.array(num_equivalent), len(num_equivalent)//3)
    encrypted_vectors = []

    for vector in num_vectors:
        encrypted_vector = np.dot(key_matrix, vector) # Добавлен оператор % (len(alphabet) + 1) для корректного результата
        encrypted_vectors.append(encrypted_vector)

    encrypted_text = [item for sublist in encrypted_vectors for item in sublist]
    return encrypted_text



def playfair_cipher(text, alphabet):
    # Замените эту строку кодом для реализации шифра Плейфера
    pass

ALPH = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
color_print("Скрыпник Василий 211-331 Лаб 3 Шифры блочной заменыЗадание", color=Color.BLUE, bold=True)
input_text = input("\033[36m\033[1mВведите строку: \033[0m").lower()

while True:
    choice = input("\033[1m\033[32mВыберете действие:\n8.Матричный шифр \n9.Шифр Плэйфера \n0.Выход\n\033[0m")
    
    if choice == '8':
        encrypted_text = matrix_cipher(input_text, ALPH)
        color_print("Результат матричного шифрования:", color=Color.MAGENTA, bold=True)
        print(encrypted_text)

    elif choice == '9':
        # Раскомментируйте и дополните код после реализации шифра Плейфера
        # encrypted_text = playfair_cipher(input_text, ALPH)
        # color_print("Результат шифрования Плейфера:", color=Color.MAGENTA, bold=True)
        # print(encrypted_text)

        pass

    elif choice == '0':
        break
