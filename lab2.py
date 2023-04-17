"""Зашифровать текст по своему варианту из  файла ВАРИАНТЫ ЗАДАНИЙ, как минимум, одним из шифров многозначной замены - Блок B: ШИФРЫ МНОГОЗНАЧНОЙ ЗАМЕНЫ* :

4.Шифр Тритемия
5.Шифр Белазо
6.Шифр Виженера
7.S-блок замены ГОСТ Р 34.12-2015 («МАГМА»)"""

from color_output import Color, color_print

def trithemia(input_str, alphabet):
    n = len(alphabet)
    res = ""
    for j in range(len(input_str)):
        i = alphabet.find(input_str[j])
        res += alphabet[(i+j) % n]
    return res


def belazo(input_str, alphabet):
    n = len(alphabet)
    res = ""

    key = input("Введите ключ: ")
    n_key = len(key)

    for j in range(len(input_str)):
        i = alphabet.find(input_str[j])
        j_key = alphabet.find(key[j % n_key])
        res += alphabet[(i+j_key) % n]
    return res


def vigener(input_str, alphabet):
    n = len(alphabet)
    res = ""

    key = input("Введите букву-ключ: ")
    j_key = alphabet.find(key[0])

    for j in range(len(input_str)):
        i = alphabet.find(input_str[j])
        res += alphabet[(i+j_key) % n]
        j_key = i
    return res

if __name__ == '__main__':
    ALPH = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    color_print("Скрыпник Василий 211-331 Лаб 2 Шифры многозначной замены", bold=True)
    color_print("Введите строку: ", color=Color.CYAN, bold=True, end="")

    input_str = input().lower()

    while (True):
        color_print("Выберете действие:\n4.Шифр Тритемия \n5.Шифр Белазо \n6.Шифр Виженера\n7.S-блок замены ГОСТ Р 34.12-2015 («МАГМА»)\n0.Выход\n",
                    color=Color.GREEN, bold=True)
        choice = input()

        if choice == '4':
            result = trithemia(input_str, ALPH)
            color_print(
                f"Результат шифровки Тритемия: {result}", color=Color.MAGENTA, bold=True, underline=True)
        elif choice == '5':
            result = belazo(input_str, ALPH)
            color_print(
                f"Результат шифровки Белазо: {result}", color=Color.MAGENTA, bold=True, underline=True)
        elif choice == '6':
            result = vigener(input_str, ALPH)
            color_print(
                f"Результат шифровки Виженера с самоключом : {result}", color=Color.MAGENTA, bold=True, underline=True)
        elif choice == '0':
            break
        else:
            color_print(
                "Некорректный выбор. Пожалуйста, попробуйте снова.", color=Color.RED)

        print()
