'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
print()
text = input('Введите текст: ')
# text = ('цепьнекрепчесвоегосамогослабогозвенатчк')

length = len(text)
# узнаю величину исходного текста и записываю ее в отдельную переменную
print()
# index_shift_mod = ''
shift = int(input('Введите длину сдвига: '))
# Ввод числа сдвига
code = ''
for i in range(length):
    symb = text[i]
    # в цикле перебираем буквы исходного текста
    index_symb = alphabet.index(symb)
    # узнаем индекс буквы в алфавите (очередность)
    index_shift_mod = (index_symb + shift) % 32
    # смещвем индекс по MODу
    code = code + alphabet[index_shift_mod]
    # по новому индексу узнаем букву и добавляем ее в строку
print()
print('Шифртекст:', code)
print()
decode = ''
for i in range(length):
    symb = code[i]
    # в цикле перебираем буквы исходного текста
    index_symb = alphabet.index(symb)
    # узнаем индекс буквы в алфавите (очередность)
    index_shift_mod = (index_symb - shift) % 32
    # смещвем индекс по MODу
    decode = decode + alphabet[index_shift_mod]
    # по новому индексу узнаем букву и добавляем ее в строку
print('Расшифровка:', decode)
print()
'''

def cesar_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    text = input('Введите текст: ')
    # text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
    length = len(text)
    # узнаю величину исходного текста и записываю ее в отдельную переменную
    print()
    # index_shift_mod = ''
    shift = int(input('Введите длину сдвига: '))
    # Ввод числа сдвига
    code = ''
    for i in range(length):
        symb = text[i]
        # в цикле перебираем буквы исходного текста
        index_symb = alphabet.index(symb)
        # узнаем индекс буквы в алфавите (очередность)
        index_shift_mod = (index_symb + shift) % 32
        # смещвем индекс по MODу
        code = code + alphabet[index_shift_mod]
        # по новому индексу узнаем букву и добавляем ее в строку
    print()
    print('Шифртекст:', code)

def cesar_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    code = input('Введите зашифрованный текст: ')
    # text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
    length = len(code)
    # узнаю величину исходного текста и записываю ее в отдельную переменную
    print()
    # index_shift_mod = ''
    shift = int(input('Введите длину сдвига: '))
    # Ввод числа сдвига
    decode = ''
    for i in range(length):
        symb = code[i]
        # в цикле перебираем буквы исходного текста
        index_symb = alphabet.index(symb)
        # узнаем индекс буквы в алфавите (очередность)
        index_shift_mod = (index_symb - shift) % 32
        # смещвем индекс по MODу
        decode = decode + alphabet[index_shift_mod]
        # по новому индексу узнаем букву и добавляем ее в строку
    print('Расшифровка:', decode)