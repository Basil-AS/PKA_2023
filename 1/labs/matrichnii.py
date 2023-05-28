import numpy as np
from sympy import Matrix
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

print()
# text = input('Введите текст для шифрования: ')
text = 'сынсапожникавсегдаходитбосикомтчк'
print()
# size = int(input('Введите размер квадратной матрицы (число от 3 и далее): '))
size = int(3)
print()
# print('Введите элементы для заполения ключ-матрицы ({}x{}): '.format(size, size))
# print('Введите ключ-матрицу: ')

# print(len(text) % size)
# print((size - (len(text) % size)))

if len(text) % size != 0:
    text = text + ((size - (len(text) % size)) * 'ф')
# Матрица как пример
# matr = [['4', '2', '1'], ['7', '5', '3'], ['9', '8', '6']]
matr = [['1', '5', '7'], ['8', '9', '4'], ['3', '2', '2']]

key = []

# Создается массив размером, который был задан в size.
# Если в матрице оказывается пустой символ - программа выдает сообщение и станавливается
for i in range(size):
    key.append([0]*size)

# Заполняем ключ-матрицу
count = 1
# for i in range(size):
#     for j in range(size):
#         key[i][j] = input('Введите {}-ый элемент матрицы: '.format(count))
#         count += 1
#         if key[i][j] == '':
#             print('Матрица заполнена пустыми элементами')
#             exit()

matr1 = Matrix(key)
# key = matr

# Преобразовываем лист key в массив NumPy с элементами из чисел
keynp = np.array(key, dtype=np.int32)

# Проверяем, есть ли у keynp обратная матирица
if np.linalg.det(keynp) == 0:
    print('Детерминант матрицы равен нулю, попробуйте ввести другую')
    exit()

# Создаем матрицу обратную keynp
key_inv = np.linalg.inv(keynp)
print()

print('Обратная матрица существует:')
print(key_inv)
print()

print('Матрица:')
print(keynp)
print()

# print(text)

result = []
counter = 0
for k in range(int(len(text)/(size))):
    text_to_matr = []
    for i in range(size):
        text_to_matr.append(alphabet.index(''.join([text[counter]]))+1)
        counter = counter + 1
        # print(text_to_matr)
    result.append(list(np.dot(keynp, text_to_matr)))

# print()
# print(result)
# print(type(text_to_matr))

# print()

# print(result[0][0])

# print()
code = ''
for i in range(len(result)):
    for j in range(size):
        code = code + str(result[i][j]) + ' '
print('Зашифрованное сообщение:', code)
print()

det = int(np.linalg.det(keynp))
print('Определитель равен:', det)
print()
# keynp_transpose = keynp.transpose()
# print('Транспонированная матрица:\n', keynp_transpose)
# print()

matr1 = matr1.adjugate()
# print(matr1)
# matr1 = matr1.transpose()
# print(matr1)
# print()
# for item in matr1:
#     matr1[item] = matr1[item] / det
matr1 = matr1 / det
# print(matr1)
# print()

code = code.split()
# print(code)
result = []
counter = 0
for k in range(int(len(code)/size)):
    text_to_matr = []
    for i in range(size):
        text_to_matr.append(''.join([code[counter]]))
        counter = counter + 1
        # print(text_to_matr)
    text_to_matr = Matrix(text_to_matr)
    result.append(list(matr1 * text_to_matr))
# print()
decode = ''
for i in range(len(result)):
    for j in range(size):
        decode = decode + str(alphabet[result[i][j]-1])
print('Расшифровка:', decode)
print()