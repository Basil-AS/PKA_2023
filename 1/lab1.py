"""Лабораторная работа 1. Шифрование шифрами однозначной замены

1. Зашифровать текст по своему варианту из  файла ВАРИАНТЫ ЗАДАНИЙ, как минимум, одним из шифров простой замены или воспользоваться результатами работы на карточках КМЗИ - Блок А: ШИФРЫ ОДНОЗНАЧНОЙ ЗАМЕНЫ* :

    Шифр АТБАШ
    Шифр Цезаря
    Квадрат Полибия

2. Написать программу (шифрование/расшифрование), как минимум, для одного из шифров простой замены (отладка и тестирование программы по своему варианту из  файла ВАРИАНТЫ ЗАДАНИЙ)**.

3. Проверить работу программы на тексте не менее 1000 символов.

4. Подготовить отчет в соответствие с требованиями  Методических указаний*.
https://online.mospolytech.ru/mod/assign/view.php?id=227049"""
from color_output import Color, color_print

def atbash(input_str, alph):
    rev_ALPH = alph[::-1]
    res = ""
    for i in range(len(input_str)):
        res += rev_ALPH[alph.find(input_str[i])]
    return res

def cesar(input_str, n, alph):
    res = ""
    for i in range(len(input_str)):
        res += alph[(alph.find(input_str[i]) + int(n)) % len(alph)]
    return res

def polibii(input_str, n, alph):
    res = []
    for i in range(len(input_str)):
        x = alph.find(input_str[i])
        res.append((x // int(n) + 1) * 10 + (x % int(n) + 1))
    return res

if __name__ == '__main__':
    ALPH = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    color_print("Скрыпник Василий 211-331 Лаб 1 Шифры однозначной замены", bold=True)
    color_print("Введите строку: ", color=Color.CYAN, bold=True, end="")

    input_str = input()
    input_str = input_str.lower()

    while (True):
            color_print("Выберете действие:\n1.Шифр АТБАШ \n2.Шифр Цезаря \n3.Квадрат Полибия\n0.Выход\n",
                        color=Color.GREEN, bold=True)
            choice = input()
            if choice == '1':
                result = atbash(input_str, ALPH)
                color_print(
                    f"Результат шифровки Атбаш: {result}", color=Color.MAGENTA, bold=True, underline=True)
            elif choice == '2':
                color_print("Введите сдвиг: ", color=Color.CYAN, bold=True, end="")
                n = input()
                result = cesar(input_str, n, ALPH)
                color_print(
                    f"Результат шифровки Цезарь со сдвигом {n}: {result}", color=Color.MAGENTA, bold=True, underline=True)
            elif choice == '3':
                color_print("Введите размер квадрата: ",
                            color=Color.CYAN, bold=True, end="")
                n = input()
                result = polibii(input_str, n, ALPH)
                color_print(
                    f"Результат шифровки Полибий со стороной квадрата {n}:", color=Color.MAGENTA, bold=True, underline=True)
                print(" ".join(str(x) for x in result))
            elif choice == '0':
                break
            else:
                color_print(
                    "Некорректный выбор. Пожалуйста, попробуйте снова.", color=Color.RED)
            print()