from modulo import modulo
import math
from random import randint

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# print()
# text = input('Введите текст: ')
text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
# text = ('когданеумеютписатьзптговорятзптчтопероплохоетчк')

# Перевод букв текста в цифры с записью из строки в лист
buffer = []
for i in range(len(text)):
    buffer.append(alphabet.index(text[i]) + 1)
print()
print(buffer)

# Проверка P


def check_p(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0) and number > len(text):
        print("Число", number, "подходит.\n")
        return number
    else:
        number = int(input(
            "Число не является простым или оно не больше длины текста, попробуйте еще раз: "))
        return check_p(number)

# Проверка X и G


def check_x_and_g(number):
    if 1 < number and number < p:
        print()
        return number
    else:
        number = int(input(
            'Число либо меньше или равно 1, либо больше или равно p. \n Попробуйте еще раз. Введите x такое, чтобы 1 < x < p: '))
        return check_x_and_g(number)

# Проверка, что числа взаимно простые (НОД = 1)


def nod(num1, num2):
    if math.gcd(num1, num2) != 1:
        num2 = randint(2, p - 2)
        return nod(num1, num2)
    else:
        print('p-1 = {} \nk = {} \nНОД чисел {} и {} равен 1, все верно.'.format(num1, num2, num1, num2), '\n')
        return num2

# Функция Эйлера


def func_euler(number):
    value = 0
    for k in range(1, number + 1):
        if math.gcd(number, k) == 1:
            value += 1
    return value



# 1. Выбирается большое простое число p, p > Mi.
print()
print('Длинна исходного текста:', len(text))
number = int(input('Введите большое простое число p, p > длины текста: '))
p = check_p(number)

# 2. Выбираются числа x и g так, что 1 < x < p, 1 < g < p.
number = int(input('Введите x такое, чтобы 1 < x < p: '))
x = check_x_and_g(number)

number = int(input('Введите g такое, чтобы 1 < g < p: '))
g = check_x_and_g(number)

print('X =', x, '\n' 'G =', g, '\n')

# 3. Вычисляется Y
y = int(modulo(g ** x, p))
print('Y =', int(y), '\n')
# Таким образом, открытые ключи: p, g, y. Секретный ключ: x.

# Выбирается случайное число 1<k<p−1 взаимно простое с p−1 - разовый ключ
k = randint(2, p - 2)
k = nod((p - 1), k)
# k = 37

#  Вычисляется a=g^k(mod p)
a = int(modulo((g**k), p))
print('a =', a)

# Создается хеш-код
hesh_nulevoe = randint(1, p-1)
print('H(0) = ', hesh_nulevoe)
hesh = 0
for i in range(len(buffer)):
    if i == 1:
        hesh = int(modulo(((hesh_nulevoe + buffer[i])**2), p-1))
    else:
        hesh = int(modulo(((hesh + buffer[i])**2), p-1))
print('H({}) = '.format(len(buffer)), hesh)
# ---

# Вычисляется b=(m−xr)k^(−1)(mod p−1)
# print((hesh - x*a)/k)
b = int(modulo(((hesh - x*a)), p-1) // k)
print('b =', b, '\n')

print('Подписью сообщения M({}) является пара (a = {}, b = {}).\n'.format(text, a, b))

# ПРОВЕРКА!!!
# Зная открытый ключ (p,g,y), подпись (a,b) сообщения M проверяется следующим образом:
# Проверяется выполнимость условий: 0<a<p и 0<b<p−1

# Создается хеш-код
# hesh_nulevoe = randint(1, p-1)
print('H(0) = ', hesh_nulevoe)
hesh_poluchatela = 0
for i in range(len(buffer)):
    if i == 1:
        hesh_poluchatela = int(modulo(((hesh_nulevoe + buffer[i])**2), p-1))
    else:
        hesh_poluchatela = int(modulo(((hesh_poluchatela + buffer[i])**2), p-1))
print('H({}) = '.format(len(buffer)), hesh_poluchatela)

a1 = int(modulo(((y**a)*(a**b)), p))
a2 = int(modulo((g**hesh_poluchatela), p))
print()
print('a1 =', a1)
print('a2 =', a2)