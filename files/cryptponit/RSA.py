# from math import gcd
import math
from modulo import modulo

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# print()
# text = input('Введите текст: ')
text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
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
print('N = ', n)

print()
euler_N = func_euler(n)
print('Функция Эйлера от N =', euler_N)

print()
e = int(input('Введите целое число E, взаимно простое с функцией Эйлера от N: '))
euler_N, e = nod(euler_N, e)

d = modulo(1, euler_N) // e
print('D равно:', int(d), '\n')

# Шифрование
# Ci = Mi^E MOD N
for element in range(len(buffer)):
    buffer[element] = alphabet[int(modulo(buffer[element] ** e, n)) - 1]
print(buffer)

code = ''
for element in range(len(buffer)):
    code += str(buffer[element])
print()
print(code, '\n')

# Расшифрование33

# E и N публикуются как открытый ключ, D сохраняется в тайне
# code = 'цсгбдскьсгэсчъисюичатиюичлазиюиръсдаыэк'

# Перевод букв текста в цифры с записью из строки в лист
buffer = []
for i in range(len(code)):
    buffer.append(alphabet.index(code[i]) + 1)
print(buffer)

print()
euler_N = func_euler(n)
print('Функция Эйлера от N =', euler_N)

print()
d = modulo(1, euler_N) // e
print('D равно:', int(d), '\n')

for element in range(len(buffer)):
    buffer[element] = alphabet[int(modulo(buffer[element] ** int(d), n)) - 1]
print(buffer)

decode = ''
for element in range(len(buffer)):
    decode += str(buffer[element])
print()
print(decode)

# 3, 11, 3 и пословица
