import math

def main():
    shannon_disposable_pad()
    #gamma_gost()


def shannon_disposable_pad():
    # Алфавит для шифрования/дешифрования
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#,.!?:;{ }[]\'\"-1234567890ZXCVBNMA'

    # Получение действия от пользователя (шифрование/дешифрование)
    action = str(input('Действие (1. encode/2. decode): '))

    # Ввод сообщения для шифрования/дешифрования
    message = input("Сообщение: ").upper()

    # Параметры генератора ПСЧ
    gamma = []
    a = int(input('Введите параметр "a" генератора ПСЧ (13): '))
    c = int(input('Введите параметр "c" генератора ПСЧ (19): '))
    m = int(input('Введите параметр "m" генератора ПСЧ (64): '))

    # Проверки ключевых параметров
    if math.gcd(c, m) != 1:
        return print("Неверно введены ключевые параметры c и m")
    if m % 4 != 0:
        return print("Ключ m не кратен 4")
    if c % 2 != 1:
        return print("Ключ c не является нечётным числом")
    if a % 4 != 1:
        return print("a mod 4 != 1, необходимо выполнение равенства")
    lstm = simple_nums(m)
    b = a - 1
    lstb = simple_nums(b)
    for i in lstm:
        if not i in lstb:
            return print("b не кратно некоторым простым делителям числа m")

    # Создание гаммы
    for i in range(len(message)+1):
        gamma.append("")
    gamma[0] = int(input('Введите порождающее число генератора ПСЧ (31): '))
    for i in range(len(message)):
        gamma[i + 1] = (a * gamma[i] + c) % m
    gamma = gamma[1::]
    print('Гамма: ', gamma)

    # Шифрование/дешифрование сообщения
    final = []
    for i in range(len(message)):
        final.append(alphabet[((alphabet.index(message[i]) ^ gamma[i]) % m)])
    result = ''.join(final)

    # Вывод результата
    if action == "1":
        return print('Результат шифрования: ', result)
    if action == '2':
        return print('Результат расшифровки: ', result)

def simple_nums(n):
    # Функция для нахождения простых чисел до n
    lst = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                if n % i == 0:
                    lst.append(i)
                break
            if (i % j == 0):
                break
            else:
                if n % i == 0:
                    lst.append(i)
    return list(set(lst))

def gamma_gost():
    action = str(input('Действие (encode/decode): '))
    message = str(input("Сообщение: "))

    # Код, который разбивает сообщение на блоки по 16 символов и добавляет пробелы между блоками
    array = []
    for i in range(16, len(message), 16):
        message[i] = ' ' + message[i]
    print(message)

if __name__ == '__main__':
    main()
