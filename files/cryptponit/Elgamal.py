from modulo import modulo
import math

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
        # print('НОД чисел {} и {} не равен 1. Введите другое число "E": '.format(num1, num2))
        num2 = int(input(
            'НОД чисел {} и {} не равен 1. Введите другое число "k": '.format(num1, num2)))
        return nod(num1, num2)
    else:
        print('НОД чисел {} и {} равен 1, все верно.'.format(num1, num2), '\n')
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
y = modulo(g ** x, p)
print('Y =', int(y), '\n')
# Таким образом, открытые ключи: p, g, y. Секретный ключ: x.

# 4. Выбираются случайные секретные числа ki (рандомизаторы), взаимно простые с функцией Эйлера от числа р (φ(p) = p − 1)

euler_p = func_euler(p)

number = int(input(
    'Введите k1 такое, чтобы оно было взаимно простое с функцией эйлера от P: '))
k1 = nod(euler_p, number)

number = int(input(
    'Введите k2 такое, чтобы оно было взаимно простое с функцией эйлера от P: '))
k2 = nod(euler_p, number)

number = int(input(
    'Введите k3 такое, чтобы оно было взаимно простое с функцией эйлера от P: '))
k3 = nod(euler_p, number)

print(k1, k2, k3, '\n')

# Шифрование
# 5. Вычисляется для каждой шифрвеличины Mi :
# ai = g^ki (mod p)
# bi = y^ki Mi (mod p)
counter = -1
code = []
for element in range(len(buffer)):
    counter = (counter + 1) % 3

    if counter == 0:
        a = int(modulo(g ** k1, p))
        b = int(modulo(buffer[element], p) * (y ** k1))
        code.append([str(a), str(b)])

    if counter == 1:
        a = int(modulo(g ** k2, p))
        b = int(modulo(buffer[element], p) * (y ** k2))
        code.append([str(a), str(b)])

    if counter == 2:
        a = int(modulo(g ** k3, p))
        b = int(modulo(buffer[element], p) * (y ** k3))
        code.append([str(a), str(b)])

# print(code)
# print(len(code))

# Проверка на самое большое число, чтобы потом выводить и добавлять нужное кол-во нулей в начало, если не хватает цифр
elem = 0
for i in range(len(code)):
    if int(code[i][0]) > int(elem):
        elem = code[i][0]
    elif int(code[i][1]) > int(elem):
        elem = code[i][1]
# print(elem)
# print(len(elem))

# Вывод шифртекста
str_code = ''
for i in range(len(code)):
    for j in range(2):
        str_code = str_code + str(code[i][j]).zfill(len(elem))
print('Шифртекст:', str_code)
# print(len(str_code))

# Шифртекст:313215292915312415052935310115432935311015222935312315382917313915352917312315442921312715352917312315112945311315022939312715232941313915052945310615222925

# Расшифрование

# Максимальная длинна числа
elem = 99  # заглушка для получения 2-ки

# Ввод шифртекста
# str_code = input('Введите шифртекст для расшифрования: ')
str_code = '313215292915312415052935310115432935311015222935312315382917313915352917312315442921312715352917312315112945311315022939312715232941313915052945310615222925'
# print(len(str_code))

# Ввод ключей
# p = input('Введите открытый ключ "p": ')
p = int(47)
# g = input('Введите открытый ключ "g": ')
g = int(11)
# y = input('Введите открытый ключ "y": ')
y = int(19)
# x = input('Введите секретный ключ "x": ')
x = int(13)
print('p =', p, 'g =', g, 'y =', y, 'x =', x, '\n')

decode = ''
decode_list = []
for i in range(0, len(str_code)-2, len(str(elem*2))+1):
    decode_list.append(
        [str_code[i]+str_code[i+1], str_code[i+2]+str_code[i+3]])
# print(decode_list)

for i in range(len(decode_list)):
    # Mi ≡ bi/ ai^x (mod p)
    decode += alphabet[int(modulo(int(decode_list[i][1]),
                           p) // int(decode_list[i][0])**x)-1]
print(decode, '\n')
