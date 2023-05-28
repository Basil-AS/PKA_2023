'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# 32 буквы в алфавите, с 0 по 31

rev_alphabet = alphabet[::-1]
# Задаю алафавит в обратном порядке
print()
text = input('Введите текст: ')
print()
# text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
# length = 39
length = len(text)

code = ''
for i in range(length):
    symb = text[i]
    index_symb = alphabet.index(symb)
    code = code + rev_alphabet[index_symb]
print('Шифртекст:', code, '\n')

decode = ''
for i in range(length):
    symb = code[i]
    index_symb = alphabet.index(symb)
    decode = decode + rev_alphabet[index_symb]
print('Расшифровка:', decode, '\n')
'''

# --------------------- АТБАШ ТЕРМИНАЛ ---------------------

def atbash_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rev_alphabet = alphabet[::-1]
    print()
    text = input('Введите текст: ')
    print()
    length = len(text)
    code = ''
    for i in range(length):
        symb = text[i]
        index_symb = alphabet.index(symb)
        code = code + rev_alphabet[index_symb]
    print('Шифртекст:', code)    

def atbash_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rev_alphabet = alphabet[::-1]
    print()
    code = input('Введите зашифрованный текст: ')
    print()
    length = len(code)
    decode = ''
    for i in range(length):
        symb = code[i]
        index_symb = alphabet.index(symb)
        decode = decode + rev_alphabet[index_symb]
    print('Расшифровка:', decode)
