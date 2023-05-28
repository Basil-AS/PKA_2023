
alphabet = 'абвгдежзиклмнопрстуфхцчшщъыэюя'
text = input("Введите исходный текст: ")
key_word = 'стенка'
key_word = input('Введите ключ-слово без повторяющихся букв: ')

seen = set()
for i in key_word:
    if i in seen:
        print('В ключе-слове есть повторяющиеся буквы\n')
        exit()
    else:
        seen.add(i)


text = text.replace('й','и').replace('ё', 'е').replace('ь','ъ')
if len(text) % 2 != 0:
    text = text + 'ф1' 
else:
    text = text + '1'
new_text = ''
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        new_text += text[i] + 'ф'
    else:
        new_text += text[i]
table = []
for i in range(5):
    table.append(['']*6)

for i in range(len(key_word)):
    alphabet = alphabet.replace(key_word[i], '')


key_with_alph = key_word + alphabet

counter = 0
for i in range(5):
    for j in range(6):
        table[i][j] = (key_with_alph[counter])
        counter = counter + 1

code = ''
bufer = ''
for k in range(0, len(new_text)-1, 2):
    letter1, letter2 = new_text[k], new_text[k+1]
    str1 = 0
    str2 = 0
    column1 = 0 
    column2 = 0
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter1)
            except ValueError: 
                pass
            else: 
                str1 = i
                column1 = table[i].index(letter1)
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter2)
            except ValueError: 
                pass
            else: 
                str2 = i
                column2 = table[i].index(letter2)

    if str1 == str2:
        column1 = (column1 + 1) % 6
        column2 = (column2 + 1) % 6
        code = code + table[str1][column1] + table[str2][column2]

    elif column1 == column2:
        str1 = (str1 + 1) % 5
        str2 = (str2 + 1) % 5
        code = code + table[str1][column1] + table[str2][column2]
    
    else:
        bufer = str1
        str1 = str2
        str2 = bufer
        code = code + table[str2][column2] + table[str1][column1]
print()
for i in table:
    print(*i)
print()
print('Шифртекст: ' + code)
print()
decode = ''

for k in range(0, len(code)-1, 2):
    letter1, letter2 = code[k], code[k+1]
    str1 = 0
    str2 = 0
    column1 = 0 
    column2 = 0
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter1)
            except ValueError: 
                pass
            else: 
                str1 = i
                column1 = table[i].index(letter1)
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter2)
            except ValueError: 
                pass
            else: 
                str2 = i
                column2 = table[i].index(letter2)

    if str1 == str2:
        column1 = (column1 - 1) % 6
        column2 = (column2 - 1) % 6
        decode = decode + table[str1][column1] + table[str2][column2]

    elif column1 == column2:
        str1 = (str1 - 1) % 5
        str2 = (str2 - 1) % 5
        decode = decode + table[str1][column1] + table[str2][column2]
    
    else:
        bufer = str1
        str1 = str2
        str2 = bufer
        decode = decode + table[str2][column2] + table[str1][column1]

# print()
print('Расшифрованный текст: ' + decode)
print()