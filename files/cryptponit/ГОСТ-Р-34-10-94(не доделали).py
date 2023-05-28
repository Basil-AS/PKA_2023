# from math import gcd
# import math
from modulo import modulo
from random import randint

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
print()
# text = input('Введите текст: ')
text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
# text = ('когданеумеютписатьзптговорятзптчтопероплохоетчк')

# Перевод букв текста в цифры с записью из строки в лист
buffer = []
for i in range(len(text)):
    buffer.append(alphabet.index(text[i]) + 1)
print(buffer, '\n')

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

'''
р - большое простое число длиной от 509 до 512 бит либо от 1020 до 1024 бит;
q - простой сомножитель числа (р-1), имеющий длину 254...256 бит; 
а - любое число, большее 1 и меньшее (р-1), причем такое, что а^q mod p = 1;
--------------------------------  р, q и а являются открытыми
х - некоторое число, меньшее q;
у = а^x mod р ---> тоже открытый ключ
-------
p = 47
q = 23
a = 3
y = 42
х = 15
'''

# p = input('большое простое число: ')
p = 47
# q = input('Введите простой сомножитель числа (р-1): ')
q = 23

# 1. Пользователь А генерирует случайное число k, причем k<q.
# k = randint(1, q-1)
k = 3

a = 3

x = 15

print('p =', p, 'q =', q, 'k =', k, 'a =', a, 'x =', x, '\n')

# Создается хеш-код
hesh_nulevoe = 0
print('H(0) = ', hesh_nulevoe)
hesh = 0
for i in range(len(buffer)):
    if i == 1:
        hesh = int(modulo(((hesh_nulevoe + buffer[i])**2), n))
    else:
        hesh = int(modulo(((hesh + buffer[i])**2), n))
print('H({}) = '.format(len(buffer)), hesh)
# ---

# 2. Пользователь А вычисляет значения
# r = (а^k mod p) mod q,
# s = (х * r + k (Н(m))) mod q.

r=(a**k % p) % q

s=(x * r + k * hesh) % q

print(r, s)