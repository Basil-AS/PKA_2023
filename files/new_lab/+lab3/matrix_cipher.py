from random import randint
import numpy as np


#  1 2 1 1 3 2 1 1 1
#

def main():
    cipher_matrix()


def cipher_matrix():
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    while True:
        size_matr = int(input("Задайте размер квадратной матрицы-ключа: "))
        matr = str(input("Задайте элементы матрицы-ключа через пробел: "))
        matr = list(matr.split(" "))
        key = np.zeros((size_matr, size_matr))
        i = 0
        while i < len(matr):
            for x in range(size_matr):
                for y in range(size_matr):
                    key[x][y] = matr[i]
                    i += 1
        frstif = True
        scndif = True
        if len(matr) != size_matr ** 2:
            print("Размер матрицы не совпадает с количеством введенных элементов. Должно быть: ", size_matr ** 2,
                  "; введено: ", len(matr), " .")
            frstif = False
        if np.linalg.det(key) == 0:
            print("Обратной матрица не существует - определитель равен нулю! Расшифрование будет невозмоно")
            scndif = False
        if frstif == False or scndif == False:
            print("Попробуйте еще раз")
        else:
            break

    # обратная матрица
    key_inv = np.linalg.inv(key)

    action = str(input("Выполнить действие (шифровать/дешифоровать): "))
    message = input("Сообщение: ").upper()
    result = ''
    if action == 'шифровать':
        if len(message) % size_matr != 0:
            temp = len(message) % size_matr
            while len(message) % size_matr != 0:
                message += alphabet[randint(0, len(alphabet) - 1)]
        print(message)
        # присвоить каждому символу в сообщении номер индекса
        message = list(message)
        for i in range(len(message)):
            message[i] = alphabet.index(message[i]) + 1

        j = 0
        while j < len(message):
            buf = np.zeros((size_matr, 1))
            for k in range(size_matr):
                if j >= len(message):
                    buf[k][0] = len(alphabet)
                else:
                    buf[k][0] = message[j]
                j += 1
            buf = key.dot(buf)
            for i in range(len(buf)):
                result += str(buf[i]).replace(".", "").replace("[", "").replace("]", "") + " "
        print(result)

    if action == 'дешифоровать':
        message = list(message.split(" "))
        j = 0
        while j < len(message):
            buf = np.zeros((size_matr, 1))
            for k in range(size_matr):
                buf[k][0] = int(message[j])
                j += 1
            buf = key_inv.dot(buf)
            for i in range(len(buf)):
                result += str(buf[i]).replace(".", "").replace("[", "").replace("]", "") + " "
        result = result.split()
        res = ""
        for i in range(len(result)):
            res += alphabet[int(result[i]) % len(alphabet) - 1]
        result = res
        print(result)


if __name__ == '__main__':
    main()

