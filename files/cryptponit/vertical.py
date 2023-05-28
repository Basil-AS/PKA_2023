'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
key_word = 'свитер'
# key_word = 'монитор'
# key_word = 'коситься'
# key_word = input('Введите ключ-слово: ')

width = len(key_word)

text = input('Введите текст: ')
# text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
# text = ('небоисясобакибрехливоизптабоисямолчаливоитчк')
# text = ('когданеумеютписатьзптговорятзптчтопероплохоетчк')

while len(text) % width != 0:
    text = text + ' '
# print(text)

# code = 'нчггон цксссот пеомавк ееоога ервалзч ьпеобе'

# если не добалять заполнение пустых клеток 'ф'ками, то приписать в эту строку (+ 1)
height = len(text) // width

print('\nРазмер таблицы: {}x{}'.format(width, height))
print()

table = []
for i in range(height):
    table.append([' ']*width)

# print(table)

counter = 0
for i in range(height):
    for j in range(width):
        try:
            table[i][j] = (text[counter])
            counter = counter + 1
        except IndexError:
            pass

# print(table)
for i in range(height):
    print(table[i])

num = 1  # временно поставил ноль, изначально была единица
index_symb_in_key = []
index_symb_in_key2 = []

for i in range(width):
    index_symb_in_key2.append([''])

for symb in key_word:
    index_symb_in_key.append(alphabet.index(symb))
print()
# print(index_symb_in_key, '\n')

for i in range(width):
    for j in range(width):
        if min(index_symb_in_key) == index_symb_in_key[j]:
            if num > width:
                break
            index_symb_in_key2[j] = num
            num += 1
            index_symb_in_key[j] = 33
            # print(index_symb_in_key2)
        else:
            pass
# print(index_symb_in_key2)

bufer_list = []
for element in index_symb_in_key2:
    bufer_list.append(element - 1)
index_symb_in_key2 = bufer_list
# print(index_symb_in_key2, '\n')

code = ''
for j in index_symb_in_key2:
    # print()
    for i in range(height):
        # print(j+1, i+1, table[i][j])
        # pass
        # print(j+1, i+1)
        code = code + table[i][j]
        # print(code)
    # break
# code = code.replace(' ', '')
print('\nШифртекст:', code.replace(' ', ''), '\n')
# code = 'нчггон цксссот пеомавк ееоога ервалзч ьпеобе'

# Расшифровка
decode = ''
width_code = len(key_word)
height_code = len(code) // len(key_word)
# print(width_code, height_code, '\n')
code_table = []

for i in range(height):
    code_table.append([' ']*width_code)

# print(table)

counter = 0
for i in range(width_code):
    for j in range(height_code):
        try:
            code_table[j][index_symb_in_key2[i]] = (code[counter])
            counter = counter + 1
        except IndexError:
            pass

# for i in range(height_code):
#     print(code_table[i])

for i in range(height_code):
    decode = decode + ''.join(code_table[i])
print('\nРасшифровка:', decode, '\n')
'''
# ---------------терминал--------------------

def vertical_crypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    text = input('Введите текст: ')
    print()
    key_word = input('Введите ключ-слово: ')
    width = len(key_word)
    # print()
    while len(text) % width != 0:
        text = text + ' '
    # если не добалять заполнение пустых клеток 'ф'ками, то приписать в эту строку (+ 1)
    height = len(text) // width
    print('\nРазмер таблицы: {}x{}'.format(width, height))
    # print()
    table = []
    for i in range(height):
        table.append([' ']*width)
    counter = 0
    for i in range(height):
        for j in range(width):
            try:
                table[i][j] = (text[counter])
                counter = counter + 1
            except IndexError:
                pass
    for i in range(height):
        print(table[i])
    num = 1  # временно поставил ноль, изначально была единица
    index_symb_in_key = []
    index_symb_in_key2 = []
    for i in range(width):
        index_symb_in_key2.append([''])
    for symb in key_word:
        index_symb_in_key.append(alphabet.index(symb))
    # print()
    for i in range(width):
        for j in range(width):
            if min(index_symb_in_key) == index_symb_in_key[j]:
                if num > width:
                    break
                index_symb_in_key2[j] = num
                num += 1
                index_symb_in_key[j] = 33
            else:
                pass
    bufer_list = []
    for element in index_symb_in_key2:
        bufer_list.append(element - 1)
    index_symb_in_key2 = bufer_list
    print(index_symb_in_key2)
    code = ''
    for j in index_symb_in_key2:
        # print()
        for i in range(height):
            code = code + table[i][j]
    print('\nШифртекст:', code.replace(' ', ''))

def vertical_decrypt():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print()
    code = input('Введите шифртекст: ')
    print()
    key_word = input('Введите ключ-слово: ')
    width_code = len(key_word)
    height_code = len(code) // len(key_word)


###
    num = 1 
    index_symb_in_key = []
    index_symb_in_key2 = []
    for i in range(width_code):
        index_symb_in_key2.append([''])
    for symb in key_word:
        index_symb_in_key.append(alphabet.index(symb))
    # print()
    for i in range(width_code):
        for j in range(width_code):
            if min(index_symb_in_key) == index_symb_in_key[j]:
                if num > width_code:
                    break
                index_symb_in_key2[j] = num
                num += 1
                index_symb_in_key[j] = 33
            else:
                pass
    bufer_list = []
    for element in index_symb_in_key2:
        bufer_list.append(element - 1)
    index_symb_in_key2 = bufer_list
###

    decode = ''
    code_table = []

    for i in range(height_code):
        code_table.append([' ']*width_code)

    counter = 0
    for i in range(width_code):
        for j in range(height_code):
            try:
                code_table[j][index_symb_in_key2[i]] = (code[counter])
                counter = counter + 1
            except IndexError:
                pass

    for i in range(height_code):
        decode = decode + ''.join(code_table[i])
    print('\nРасшифровка:', decode, '\n')
