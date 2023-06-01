import math
'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# m - мощность алфавита
m = len(alphabet)
text = input('Введите текст: ')
# text = ('сынсапожникавсегдаходитбосикомтчк')
ti0 = 1
'''
# Функция проверки числа 'a' на нечетность
def nechetA(a):
    if a % 2 == 0:
        number = int(input('Число четное. Введите нечетное число "а": '))
        nechetA(number)
    else:
        print('Число', a, 'подходит.')
        return a

# Функция проверки числа 'c' на нечетность
def nechetC(c):
    if c % 2 == 0:
        number = int(input('Число четное. Введите нечетное число "c": '))
        nechetC(number)
    else:
        print('Число', c, 'подходит.')
        return c

# Проверка, что число 'a' и 'c' взаимно простые (НОД = 1)
def nod(m, c):
    if math.gcd(m, c) != 1:
        number = int(input('НОД чисел {} и {} не равен 1. Введите другое нечетное число "c": '.format(m, c)))
        c = nechetC(number)
        nod (m, c)
    else:
        print ('НОД чисел {} и {} равен 1, все верно.'.format(m, c), '\n')
'''
print()
number = int(input('Введите нечетное число "а": '))
a = nechetA(number)

print()
number = int(input('Введите нечетное число "c": '))
c = nechetC(number)

print()
nod(m, c)

# Линейный генератор: Т(i+1) = (aT(i) + с) mod m

# Создаем лист, заполненный нулями, длина которого равна тексту + 1
gen = []
for i in range(len(text)+1):
    gen.append(0)

# Заполняем лист гаммой
gen[0] = ti0
for i in range(1, len(gen), 1):
    gen[i] = ((a*gen[i-1]+c) % m)
# print(gen, '\n')

# Создаем лист, заполненный нулями, для дальнейшего его заполнения индексами букв алфавита из текста
text_to_num = []
for i in range(len(text)):
    text_to_num.append(0)

# Заполнение индексами букв алфавита из текста
for i in range(len(text_to_num)):
    text_to_num[i] = alphabet.index(text[i]) + 1
# print(text_to_num, '\n')

# Создаем лист, заполненный нулями, для шифрования текста
encryption = []
for i in range(len(text)):
    encryption.append(0)

# Шифрование текста
for i in range(len(encryption)):
    encryption[i] = ((text_to_num[i] + gen[i+1]) % 32)
    # Если появляется 0, то происходит замена на 32
    if encryption[i] == 0:
        encryption[i] = 32
1
# print(encryption)
# print()

code = ''
for i in range(len(encryption)):
    encryption[i] = encryption[i] - 1
    code = code + alphabet[encryption[i]]
print('Шифртекст:', code, '\n')

# Расшифровка
code = 'аьзщгшойзюзъянкцэхщнтсччгкажмюъимьеэико'
# code = 'лшъьэгшчезнвдцььгцочяйсцчвюсмонгушжэндвпзчэхзех'
a = 5
c = 5
m = 32
ti0 = 1

# Создаем лист, заполненный нулями, длина которого равна code + 1
gen = []
for i in range(len(code)+1):
    gen.append(0)

# Заполняем лист гаммой
gen[0] = ti0
for i in range(1, len(gen), 1):
    gen[i] = ((a*gen[i-1]+c) % m)
# print(gen, '\n')

# Создаем лист, заполненный нулями, для дальнейшего его заполнения индексами букв алфавита из code
code_to_num = []
for i in range(len(code)):
    code_to_num.append(0)

# Заполнение индексами букв алфавита из code
for i in range(len(code_to_num)):
    code_to_num[i] = alphabet.index(code[i]) + 1
# print(code_to_num, '\n')

# Создаем лист, заполненный нулями, для расшифрования code
decryption = []
for i in range(len(code)):
    decryption.append(0)

# Расшифрование code
for i in range(len(decryption)):
    decryption[i] = ((code_to_num[i] - gen[i+1] + m) % m)

# print(decryption)

decryption_to_text = ''
for i in range(len(decryption)):
    decryption[i] = decryption[i] - 1
    decryption_to_text = decryption_to_text + alphabet[decryption[i]]
print('Расшифровка:', decryption_to_text, '\n')
'''
# ----------- для терминала -----------

def shennon_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    m = len(alphabet)
    print()
    text = input('Введите текст: ')
    print()
    # ti0 = 1
    ti0 = int(input('Введите исходную величину T(0): '))
    print()

    number = int(input('Введите нечетное число "а": '))
    a = nechetA(number)
    print()
    number = int(input('Введите нечетное число "c": '))
    c = nechetC(number)
    print()
    nod(m, c)
    gen = []
    for i in range(len(text)+1):
        gen.append(0)
    gen[0] = ti0
    for i in range(1, len(gen), 1):
        gen[i] = ((a*gen[i-1]+c) % m)
    text_to_num = []
    for i in range(len(text)):
        text_to_num.append(0)
    for i in range(len(text_to_num)):
        text_to_num[i] = alphabet.index(text[i]) + 1
    encryption = []
    for i in range(len(text)):
        encryption.append(0)
    for i in range(len(encryption)):
        encryption[i] = ((text_to_num[i] + gen[i+1]) % 32)
        if encryption[i] == 0:
            encryption[i] = 32
    code = ''
    for i in range(len(encryption)):
        encryption[i] = encryption[i] - 1
        code = code + alphabet[encryption[i]]
    print('Шифртекст:', code)


def shennon_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    # code = 'аьзщгшойзюзъянкцэхщнтсччгкажмюъимьеэико'
    print()
    code = input('Введите шифртекст: ')
    print()
    # m = 32 все параметры менье 32х
    m = len(alphabet)

    # ti0 = 1
    ti0 = int(input('Введите исходную величину T(0): '))
    print()
    # a = 5 а-4 кратно 4 
    a = int(input('Введите константу "a": '))
    print()
    # c = 5
    c = int(input('Введите константу "c": '))
    print()

    gen = []
    for i in range(len(code)+1):
        gen.append(0)
    gen[0] = ti0
    for i in range(1, len(gen), 1):
        gen[i] = ((a*gen[i-1]+c) % m)
    code_to_num = []
    for i in range(len(code)):
        code_to_num.append(0)
    for i in range(len(code_to_num)):
        code_to_num[i] = alphabet.index(code[i]) + 1
    decryption = []
    for i in range(len(code)):
        decryption.append(0)
    for i in range(len(decryption)):
        decryption[i] = ((code_to_num[i] - gen[i+1] + m) % m)
    decryption_to_text = ''
    for i in range(len(decryption)):
        decryption[i] = decryption[i] - 1
        decryption_to_text = decryption_to_text + alphabet[decryption[i]]
    print('Расшифровка:', decryption_to_text)