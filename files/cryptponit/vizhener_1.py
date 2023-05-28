# alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# # key_symb = 'м'
# print()
# key_symb = input('Введите ключ-букву: ')
# # ключ-буква
# print()
# text = input('Введите текст: ')
# # text = ('цепьнекрепчесвоегосамогослабогозвенатчк')

# text_modified = key_symb + text[:-1]
# # добавляем в начало исходного текста ключ-букву и отнимаем последний симвл исх.текста

# length = len(text)
# # узнаю величину исходного текста и записываю ее в отдельную переменную

# code = ''
# for i in range(length):
#     symb = text[i]
#     # в цикле перебираем буквы исходного текста
#     index_symb = alphabet.index(symb)
#     # узнаем индекс буквы в алфавите (очередность)
#     shift = alphabet.index(text_modified[i])
#     # определяем сдвиг по символу из модифицированного текста
#     index_shift_mod = (index_symb + shift) % 32
#     # смещаем индекс по MODу
#     code = code + alphabet[index_shift_mod]
#     # по новому индексу узнаем букву и добавляем ее в строку
# print()
# print('Шифртекст:', code)

# decode = ''
# for i in range(length):
#     symb = code[i]
#     # в цикле перебираем буквы исходного текста
#     index_symb = alphabet.index(symb)
#     # узнаем индекс буквы в алфавите (очередность)
#     shift = alphabet.index(text_modified[i])
#     # определяем сдвиг по символу из модифицированного текста
#     index_shift_mod = (index_symb - shift) % 32
#     # смещаем индекс по MODу
#     decode = decode + alphabet[index_shift_mod]
#     # по новому индексу узнаем букву и добавляем ее в строку
# print()
# print('Расшифровка:', decode)
# print()

def vizhener_1_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    key_symb = input('Введите ключ-букву: ')
    print()
    text = input('Введите текст: ')
    text_modified = key_symb + text[:-1]
    length = len(text)
    code = ''
    for i in range(length):
        symb = text[i]
        index_symb = alphabet.index(symb)
        shift = alphabet.index(text_modified[i])
        index_shift_mod = (index_symb + shift) % 32
        code = code + alphabet[index_shift_mod]
    print()
    print('Шифртекст:', code)

def vizhener_1_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    code = input('Введите зашифрованный текст: ')
    key_symb = input('Введите ключ-букву: ')
    decode = ''
    length = len(code)
    text_modified = key_symb
    for i in range(length):
        symb = code[i]
        index_symb = alphabet.index(symb)
        shift = alphabet.index(text_modified[i])
        index_shift_mod = (index_symb - shift) % 32
        decode = decode + alphabet[index_shift_mod]
        text_modified += alphabet[index_shift_mod]
    print()
    print('Расшифровка:', decode)