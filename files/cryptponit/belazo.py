'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
key_word = 'арбуз'
# key_word = input('Введите ключ-слово: ')
# слово-ключ

# text = input('Введите текст: ')
text = ('цепьнекрепчесвоегосамогослабогозвенатчк')

length = len(text)
# узнаю величину исходного текста и записываю ее в отдельную переменную
key_num = 0
# Счетчик, используемый в сдвиге
shift = alphabet.index(key_word[key_num])
# сдвиг относительно индекса в алфавите по первому символу ключа

index_symb = ''
code = ''
for i in range(length):
    symb = text[i]
    # в цикле перебираем буквы исходного текста
    index_symb = alphabet.index(symb)
    # узнаем индекс буквы в алфавите (очередность)
    index_shift_mod = (index_symb + shift) % 32
    # смещаем индекс по MODу
    key_num = (key_num + 1) % len(key_word)
    # сдвиг по символу в ключе
    shift = alphabet.index(key_word[key_num])
    # осуществляем сидвиг на одну строчку вниз
    code = code + alphabet[index_shift_mod]
    # по новому индексу узнаем букву и добавляем ее в строку
print()
print('Шифртекст:', code)

decode = ''
key_num = 0
shift = alphabet.index(key_word[key_num])
for i in range(length):
    symb = code[i]
    # в цикле перебираем буквы исходного текста
    index_symb = alphabet.index(symb)
    # узнаем индекс буквы в алфавите (очередность)
    index_shift_mod = (index_symb - shift) % 32
    # смещаем индекс по MODу
    key_num = (key_num + 1) % len(key_word)
    # сдвиг по символу в ключе
    shift = alphabet.index(key_word[key_num])
    # осуществляем сидвиг на одну строчку вниз
    decode = decode + alphabet[index_shift_mod]
    # по новому индексу узнаем букву и добавляем ее в строку
print()
print('Расшифровка:', decode)
print()
'''

def belazo_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    key_word = input('Введите ключ-слово: ')
    text = input('Введите текст: ')
    length = len(text)
    key_num = 0
    shift = alphabet.index(key_word[key_num])
    index_symb = ''
    code = ''
    for i in range(length):
        symb = text[i]
        index_symb = alphabet.index(symb)
        index_shift_mod = (index_symb + shift) % 32
        key_num = (key_num + 1) % len(key_word)
        shift = alphabet.index(key_word[key_num])
        code = code + alphabet[index_shift_mod]
    print()
    print('Шифртекст:', code)

def belazo_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    key_word = input('Введите ключ-слово: ')
    code = input('Введите текст: ')
    length = len(code)
    decode = ''
    key_num = 0
    shift = alphabet.index(key_word[key_num])
    for i in range(length):
        symb = code[i]
        index_symb = alphabet.index(symb)
        index_shift_mod = (index_symb - shift) % 32
        key_num = (key_num + 1) % len(key_word)
        shift = alphabet.index(key_word[key_num])
        decode = decode + alphabet[index_shift_mod]
    print()
    print('Расшифровка:', decode)
    print()