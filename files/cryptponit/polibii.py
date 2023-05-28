'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
print()
text = input('Введите текст: ')
# text = ('цепьнекрепчесвоегосамогослабогозвенатчк')

length = len(text)

code = ''
for i in range(length):
    symb = text[i]
    index_symb = alphabet.index(symb)
    code = code + str(index_symb // 6 + 1) + str(index_symb % 6 + 1) + ' '
# +1 везде т.к счет идет с нуля (первая строчка и первый столбец не нулевые, а единичные)
print()
print('Шифртекст:', code)

code = code.replace(' ', '')
decode = ''
for i in range(0, len(code)-1, 2):
    symb1, symb2 = code[i], code[i+1]
    decode = decode + alphabet[(int(symb1)-1)*6+(int(symb2)-1)]
print()
print('Расшифровка:', decode)
print()
'''

def polibii_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    text = input('Введите текст: ')
    # text = ('цепьнекрепчесвоегосамогослабогозвенатчк')

    length = len(text)

    code = ''
    for i in range(length):
        symb = text[i]
        index_symb = alphabet.index(symb)
        code = code + str(index_symb // 6 + 1) + str(index_symb % 6 + 1) + ' '
    # +1 везде т.к счет идет с нуля (первая строчка и первый столбец не нулевые, а единичные)
    print()
    print('Шифртекст:', code)
def polibii_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    code = input('Введите зашифрованный текст: ')
    code = code.replace(' ', '')
    # text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
    length = len(code)
    decode = ''
    for i in range(0, len(code)-1, 2):
        symb1, symb2 = code[i], code[i+1]
        decode = decode + alphabet[(int(symb1)-1)*6+(int(symb2)-1)]
    print()
    print('Расшифровка:', decode)
    print()