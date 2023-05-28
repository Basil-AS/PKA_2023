'''
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
text = ('цепьнекрепчесвоегосамогослабогозвенатчк')

while len(text) != 60:
    text = text + 'ф'
# print('\n', text, '\n')

height = 6
width = 10

trafaretka1 = [['  ', ' 1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
               [' 2', '  ', '  ', '  ', ' 3', '  ', ' 4', ' 5', '  ', '  '],
               ['  ', ' 6', '  ', '  ', '  ', ' 7', '  ', '  ', '  ', ' 8'],
               ['  ', '  ', '  ', ' 9', '  ', '  ', '  ', '10', '  ', '  '],
               ['  ', '11', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
               ['  ', '  ', '12', '  ', '  ', '13', '14', '  ', '  ', '15']]

trafaretka2 = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '16', '  '],
               ['  ', '  ', '17', '18', '  ', '19', '  ', '  ', '  ', '20'],
               ['21', '  ', '  ', '  ', '22', '  ', '  ', '  ', '23', '  '],
               ['  ', '  ', '24', '  ', '  ', '  ', '25', '  ', '  ', '  '],
               ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '26', '  '],
               ['27', '  ', '  ', '28', '29', '  ', '  ', '30', '  ', '  ']]

trafaretka3 = [['31', '  ', '  ', '32', '33', '  ', '  ', '34', '  ', '  '],
               ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '35', '  '],
               ['  ', '  ', '36', '  ', '  ', '  ', '37', '  ', '  ', '  '],
               ['38', '  ', '  ', '  ', '39', '  ', '  ', '  ', '40', '  '],
               ['  ', '  ', '41', '42', '  ', '43', '  ', '  ', '  ', '44'],
               ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '45', '  ']]

trafaretka4 = [['  ', '  ', '46', '  ', '  ', '47', '48', '  ', '  ', '49'],
               ['  ', '50', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
               ['  ', '  ', '  ', '51', '  ', '  ', '  ', '52', '  ', '  '],
               ['  ', '53', '  ', '  ', '  ', '54', '  ', '  ', '  ', '55'],
               ['56', '  ', '  ', '  ', '57', '  ', '58', '59', '  ', '  '],
               ['  ', '60', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]

# for i in range(height):
#     print(trafaretka1[i])

table = []
for i in range(height):
    table.append(['']*width)

# print()
# for i in range(height):
#     print(table[i])

counter_symb = 1
for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka1[i][j]) == counter_symb:
                table[i][j] = text[counter_symb-1]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka2[i][j]) == counter_symb:
                table[i][j] = text[counter_symb-1]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka3[i][j]) == counter_symb:
                table[i][j] = text[counter_symb-1]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka4[i][j]) == counter_symb:
                table[i][j] = text[counter_symb-1]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

print()
for i in range(height):
    print(table[i])
print()
code = ''
for element in table:
    code = code + ''.join(element)
print('Шифртекст:', code, '\n')

# Расшифровка
decode = ''
decode_table = []
for i in range(height):
    decode_table.append(['']*width)

counter = 0
for i in range(height):
    for j in range(width):
        try:
            decode_table[i][j] = (code[counter])
            counter = counter + 1
        except IndexError:
            pass

for i in range(height):
    print(decode_table[i])
print()

counter_symb = 1
for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka1[i][j]) == counter_symb:
                decode += decode_table[i][j]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka2[i][j]) == counter_symb:
                decode += decode_table[i][j]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka3[i][j]) == counter_symb:
                decode += decode_table[i][j]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

for i in range(height):
    for j in range(width):
        try:
            if int(trafaretka4[i][j]) == counter_symb:
                decode += decode_table[i][j]
                counter_symb = counter_symb + 1
        except ValueError:
            pass

print('Расшифровка:', decode)
'''
# -------------- для терминала ------------------

def kardano_crypt():
    print()
    text = input("Введите исходный текст: ")
    print()
    while len(text) != 60:
        text = text + 'ф'
    height = 6
    width = 10
    trafaretka1 = [['  ', ' 1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                [' 2', '  ', '  ', '  ', ' 3', '  ', ' 4', ' 5', '  ', '  '],
                ['  ', ' 6', '  ', '  ', '  ', ' 7', '  ', '  ', '  ', ' 8'],
                ['  ', '  ', '  ', ' 9', '  ', '  ', '  ', '10', '  ', '  '],
                ['  ', '11', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '12', '  ', '  ', '13', '14', '  ', '  ', '15']]
    trafaretka2 = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '16', '  '],
                ['  ', '  ', '17', '18', '  ', '19', '  ', '  ', '  ', '20'],
                ['21', '  ', '  ', '  ', '22', '  ', '  ', '  ', '23', '  '],
                ['  ', '  ', '24', '  ', '  ', '  ', '25', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '26', '  '],
                ['27', '  ', '  ', '28', '29', '  ', '  ', '30', '  ', '  ']]
    trafaretka3 = [['31', '  ', '  ', '32', '33', '  ', '  ', '34', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '35', '  '],
                ['  ', '  ', '36', '  ', '  ', '  ', '37', '  ', '  ', '  '],
                ['38', '  ', '  ', '  ', '39', '  ', '  ', '  ', '40', '  '],
                ['  ', '  ', '41', '42', '  ', '43', '  ', '  ', '  ', '44'],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '45', '  ']]
    trafaretka4 = [['  ', '  ', '46', '  ', '  ', '47', '48', '  ', '  ', '49'],
                ['  ', '50', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '51', '  ', '  ', '  ', '52', '  ', '  '],
                ['  ', '53', '  ', '  ', '  ', '54', '  ', '  ', '  ', '55'],
                ['56', '  ', '  ', '  ', '57', '  ', '58', '59', '  ', '  '],
                ['  ', '60', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    table = []
    for i in range(height):
        table.append(['']*width)
    counter_symb = 1
    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka1[i][j]) == counter_symb:
                    table[i][j] = text[counter_symb-1]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass
    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka2[i][j]) == counter_symb:
                    table[i][j] = text[counter_symb-1]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass
    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka3[i][j]) == counter_symb:
                    table[i][j] = text[counter_symb-1]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass
    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka4[i][j]) == counter_symb:
                    table[i][j] = text[counter_symb-1]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass
    # print()
    for i in range(height):
        print(table[i])
    print()
    code = ''
    for element in table:
        code = code + ''.join(element)
    print('Шифртекст:', code)


def kardano_decrypt():
    print()
    code = input("Введите шифртекст: ")
    print()
    height = 6
    width = 10
    trafaretka1 = [['  ', ' 1', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                [' 2', '  ', '  ', '  ', ' 3', '  ', ' 4', ' 5', '  ', '  '],
                ['  ', ' 6', '  ', '  ', '  ', ' 7', '  ', '  ', '  ', ' 8'],
                ['  ', '  ', '  ', ' 9', '  ', '  ', '  ', '10', '  ', '  '],
                ['  ', '11', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '12', '  ', '  ', '13', '14', '  ', '  ', '15']]
    trafaretka2 = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '16', '  '],
                ['  ', '  ', '17', '18', '  ', '19', '  ', '  ', '  ', '20'],
                ['21', '  ', '  ', '  ', '22', '  ', '  ', '  ', '23', '  '],
                ['  ', '  ', '24', '  ', '  ', '  ', '25', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '26', '  '],
                ['27', '  ', '  ', '28', '29', '  ', '  ', '30', '  ', '  ']]
    trafaretka3 = [['31', '  ', '  ', '32', '33', '  ', '  ', '34', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '35', '  '],
                ['  ', '  ', '36', '  ', '  ', '  ', '37', '  ', '  ', '  '],
                ['38', '  ', '  ', '  ', '39', '  ', '  ', '  ', '40', '  '],
                ['  ', '  ', '41', '42', '  ', '43', '  ', '  ', '  ', '44'],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '45', '  ']]
    trafaretka4 = [['  ', '  ', '46', '  ', '  ', '47', '48', '  ', '  ', '49'],
                ['  ', '50', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '51', '  ', '  ', '  ', '52', '  ', '  '],
                ['  ', '53', '  ', '  ', '  ', '54', '  ', '  ', '  ', '55'],
                ['56', '  ', '  ', '  ', '57', '  ', '58', '59', '  ', '  '],
                ['  ', '60', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    decode = ''
    decode_table = []
    for i in range(height):
        decode_table.append(['']*width)

    counter = 0
    for i in range(height):
        for j in range(width):
            try:
                decode_table[i][j] = (code[counter])
                counter = counter + 1
            except IndexError:
                pass

    for i in range(height):
        print(decode_table[i])
    print()

    counter_symb = 1
    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka1[i][j]) == counter_symb:
                    decode += decode_table[i][j]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass

    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka2[i][j]) == counter_symb:
                    decode += decode_table[i][j]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass

    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka3[i][j]) == counter_symb:
                    decode += decode_table[i][j]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass

    for i in range(height):
        for j in range(width):
            try:
                if int(trafaretka4[i][j]) == counter_symb:
                    decode += decode_table[i][j]
                    counter_symb = counter_symb + 1
            except ValueError:
                pass
    print('Расшифровка:', decode)