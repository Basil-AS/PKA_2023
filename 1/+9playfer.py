alphabet = 'абвгдежзиклмнопрстуфхцчшщъыэюя'
# алфавит для таблицы, в которором убраны ё, й и ь

# text = 'сынсапожникавсегдаходитбосикомтчк'
# print()
text = input("Введите исходный текст: ")
# key_word = 'стенка'
# print()
key_word = input('Введите ключ-слово без повторяющихся букв: ')

# Создаем множество для проверки ключа на повторяемость символов
seen = set()
for i in key_word:
    if i in seen:
        print('В ключе-слове есть повторяющиеся буквы\n')
        exit()
    else:
        seen.add(i)


# Замена символов исходного текста (замена (ё, й, ь) на (е, и, ъ))
text = text.replace('й','и').replace('ё', 'е').replace('ь','ъ')
# Если колличество символов нечетное, то в конец строки добавляется буква "а"
if len(text) % 2 != 0:
    text = text + 'ф1' 
    # Добавляем строку "а1" в конец text, т.к единичка в последствии пропадает в др. операции
else:
    text = text + '1'
    # Добавляем строку "1" в конец text, т.к единичка в последствии пропадает в др. операции

# print()
# print(text)
# print()

# В случае, если в тексте есть повторяющиеся буквы, происходит внедрение символа "ф" между ними
new_text = ''
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        new_text += text[i] + 'ф'
    else:
        new_text += text[i]

# print()
# print(new_text)
# print()

# Создание многомерного массива (создается пустая таблица 5x6)
table = []
for i in range(5):
    table.append(['']*6)

# Удаляем из алфавита буквы из слова-ключа
for i in range(len(key_word)):
    alphabet = alphabet.replace(key_word[i], '')


# Строка, содержащая слово-ключ и отредактированный алфавит
key_with_alph = key_word + alphabet

# Заполнение таблицы строкой, содержащей слово-ключ и отредактированный алфавит (с исключенными буквами)
counter = 0
for i in range(5):
    for j in range(6):
        table[i][j] = (key_with_alph[counter])
        counter = counter + 1

# print()
# print(table)
# print()

# print()
code = ''
bufer = ''
for k in range(0, len(new_text)-1, 2):
    letter1, letter2 = new_text[k], new_text[k+1]
    # print(letter1,letter2)
    str1 = 0
    str2 = 0
    column1 = 0 
    column2 = 0
    # Ищем в таблице первую букву пары и получаем её индекс
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter1)
            except ValueError: 
                pass
            else: 
                str1 = i
                column1 = table[i].index(letter1)
    # Ищем в таблице вторую букву пары и получаем её индекс
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter2)
            except ValueError: 
                pass
            else: 
                str2 = i
                column2 = table[i].index(letter2)
    
    # print ('Строка и столбец 1 символа: ', str1, column1)
    # print ('Строка и столбец 2 символа: ', str2, column2)
    # print()
    
    # Если буквы находятся в одной строке, то идет смещение на один символ вправо
    if str1 == str2:
        column1 = (column1 + 1) % 6
        column2 = (column2 + 1) % 6
        code = code + table[str1][column1] + table[str2][column2]

    # Если буквы не находятся в одном столбце, то идет смещение на один символ вниз
    elif column1 == column2:
        str1 = (str1 + 1) % 5
        str2 = (str2 + 1) % 5
        code = code + table[str1][column1] + table[str2][column2]
    
    # Если буквы находятся в разных строках и столбцах, то символы меняются местами по строкам (идет отзеркаливание)
    else:
        bufer = str1
        str1 = str2
        str2 = bufer
        code = code + table[str2][column2] + table[str1][column1]
print()
# print(table)
for i in table:
    print(*i)
print()
print('Шифртекст: ' + code)
print()
decode = ''

for k in range(0, len(code)-1, 2):
    letter1, letter2 = code[k], code[k+1]
    # print(letter1,letter2)
    str1 = 0
    str2 = 0
    column1 = 0 
    column2 = 0
    # Ищем в таблице первую букву пары и получаем её индекс
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter1)
            except ValueError: 
                pass
            else: 
                str1 = i
                column1 = table[i].index(letter1)
    # Ищем в таблице вторую букву пары и получаем её индекс
    for i in range(5):
        for j in range(6):
            try: 
                table[i].index(letter2)
            except ValueError: 
                pass
            else: 
                str2 = i
                column2 = table[i].index(letter2)
    
    # print ('Строка и столбец 1 символа: ', str1, column1)
    # print ('Строка и столбец 2 символа: ', str2, column2)
    # print()
    
    # Если буквы находятся в одной строке, то идет смещение на один символ вправо
    if str1 == str2:
        column1 = (column1 - 1) % 6
        column2 = (column2 - 1) % 6
        decode = decode + table[str1][column1] + table[str2][column2]

    # Если буквы не находятся в одном столбце, то идет смещение на один символ вниз
    elif column1 == column2:
        str1 = (str1 - 1) % 5
        str2 = (str2 - 1) % 5
        decode = decode + table[str1][column1] + table[str2][column2]
    
    # Если буквы находятся в разных строках и столбцах, то символы меняются местами по строкам (идет отзеркаливание)
    else:
        bufer = str1
        str1 = str2
        str2 = bufer
        decode = decode + table[str2][column2] + table[str1][column1]

# print()
print('Расшифрованный текст: ' + decode)
print()