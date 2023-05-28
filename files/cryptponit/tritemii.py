'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# print()
# text = input('Введите текст: ')
text = ('цепьнекрепчесвоегосамогослабогозвенатчк')

length = len(text)
# узнаю величину исходного текста и записываю ее в отдельную переменную

shift = 0
# сдвиг по-умолчанию

code = ''
for i in range(length):
    symb = text[i]
    # в цикле перебираем буквы исходного текста
    index_symb = alphabet.index(symb)
    # узнаем индекс буквы в алфавите (очередность)
    index_shift_mod = (index_symb + shift) % 32
    # смещвем индекс по MODу
    shift = shift + 1
    # осуществляем сидвиг на одну строчку вниз
    code = code + alphabet[index_shift_mod]
    # по новому индексу узнаем букву и добавляем ее в строку
print()
print('Шифртекст:', code)

decode = ''
shift = 0
for i in range(length):
    symb = code[i]
    # в цикле перебираем буквы исходного текста
    index_symb = alphabet.index(symb)
    # узнаем индекс буквы в алфавите (очередность)
    index_shift_mod = (index_symb - shift) % 32
    # смещвем индекс по MODу
    shift = shift + 1
    # осуществляем сидвиг на одну строчку вниз
    decode = decode + alphabet[index_shift_mod]
    # по новому индексу узнаем букву и добавляем ее в строку
print()
print('Расшифровка:', decode)
print()
'''

def tritemii_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    text = input('Введите текст: ')
    length = len(text)
    shift = 0
    code = ''
    for i in range(length):
        symb = text[i]
        index_symb = alphabet.index(symb)
        index_shift_mod = (index_symb + shift) % 32
        shift = shift + 1
        code = code + alphabet[index_shift_mod]
    print()
    print('Шифртекст:', code)

def tritemii_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    code = input('Введите зашифрованный текст: ')
    length = len(code)
    decode = ''
    shift = 0
    for i in range(length):
        symb = code[i]
        index_symb = alphabet.index(symb)
        index_shift_mod = (index_symb - shift) % 32
        shift = shift + 1
        decode = decode + alphabet[index_shift_mod]
    print()
    print('Расшифровка:', decode)