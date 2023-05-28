# from math import gcd
import math
from modulo import modulo
from random import randint

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# print()
text = input('Введите текст: ')
# text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
# text = ('когданеумеютписатьзптговорятзптчтопероплохоетчк')

# Перевод букв текста в цифры с записью из строки в лист
buffer = []
for i in range(len(text)):
    buffer.append(alphabet.index(text[i]) + 1)
print(buffer)

# Функция проверки числа на простоту


def simple_number(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        print("Число", number, "— простое.")
        return number
    else:
        number = int(input("Число не является простым, попробуйте еще раз: "))
        return simple_number(number)

# Функция Эйлера


def func_euler(number):
    value = 0
    for k in range(1, number + 1):
        if math.gcd(number, k) == 1:
            value += 1
    return value

# Проверка, что числа взаимно простые (НОД = 1)


def nod(num1, num2):
    if math.gcd(num1, num2) != 1:
        # print('НОД чисел {} и {} не равен 1. Введите другое число "E": '.format(num1, num2))
        num2 = int(input(
            'НОД чисел {} и {} не равен 1. Введите другое число "E": '.format(num1, num2)))
        return nod(num1, num2)
    else:
        print('НОД чисел {} и {} равен 1, все верно.'.format(num1, num2), '\n')
        return num1, num2


print()
number = int(input('Введите простое число "p": '))
p = simple_number(number)

print()
number = int(input('Введите простое число "q": '))
q = simple_number(number)

print()
n = p * q
print('N = ', n, '\n')

# ---
# Создается хеш-код
hesh_nulevoe = randint(1, n)
print('H(0) = ', hesh_nulevoe)
hesh = 0
for i in range(len(buffer)):
    if i == 1:
        hesh = int(modulo(((hesh_nulevoe + buffer[i])**2), n))
    else:
        hesh = int(modulo(((hesh + buffer[i])**2), n))
print('H({}) = '.format(len(buffer)), hesh)
# ---

print()
euler_N = func_euler(n)
print('Функция Эйлера от N =', euler_N)

print()
e = int(input('Введите целое число E, взаимно простое с функцией Эйлера от N: '))
euler_N, e = nod(euler_N, e)

d = int(modulo(1, euler_N) // e)
print('D равно:', d, '\n')

# ---
# Вычисление ЦП
s = int(modulo((hesh ** d), n))
print('S =', s, '\n') 
# ---

print('Получателю отправляется сообщение M = {}, и подпись S = {}.\n'.format(text, s))

# E и N публикуются как открытый ключ, D сохраняется в тайне
# Получатель сообщения хеширует M, получает хеш-код m’.
# Получателю отправляется сообщение M и подпись S.

# ПРОВЕРКА!!!
# ---
# Создается хеш-код
hesh_nulevoe = randint(1, n)
print('H(0) = ', hesh_nulevoe)
hesh_poluchatela = 0
for i in range(len(buffer)):
    if i == 1:
        hesh_poluchatela = int(modulo(((hesh_nulevoe + buffer[i])**2), n))
    else:
        hesh_poluchatela = int(modulo(((hesh_poluchatela + buffer[i])**2), n))
print('H({}) = '.format(len(buffer)), hesh_poluchatela)
# 
m = int(modulo((s ** e), n))
print('m =', m, '\n')
print('m* получателя = {}, и m = {} равны, верно!'.format(hesh_poluchatela, m))
# 3, 11, 3 и пословица