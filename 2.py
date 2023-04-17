import numpy as np

ALPH = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


# str = input("\033[36m\033[1mВведите строку: \033[0m")
str = "забава"
n = len(str)
# Создание ключ-матрицы
key = [[1, 4, 8],
       [3, 7, 2],
       [6, 9, 5],
       [6, 9, 5]]
key = np.array(key)
i_key = key.shape[0]
j_key = key.shape[1]
# print(i_key, j_key)

# перевод строки в числовой эквивалент
str_int = []
for j in range(n):
    i = ALPH.find(str[j]) + 1
    str_int.append(i)

# Разбиваем строку эквивалентов на вектор столбцы
n_list = n // j_key  #количество вектор столцов
if n % j_key!= 0:
    n_list += 1

list_str_int = [[]*n_list for i in range(j_key)]
for i in range(n_list):
    for j in range(j_key):
        list_str_int[i].append(str_int[i * j_key + j])
print(list_str_int)


# умножение матрицы числового эквивалента на ключ-матрицу
# res = np.dot(key, np.array(str_int))


# print(
#     f"\033[35m\033[1mРезультат шифровки матричный {key}: \033[4m{res}\033[0m")
print(str_int)
# print(
#     f"\033[35m\033[1mРезультат матричной шифровки с ключом \n{key}: \n{res}\033[4m\033[0m")
# print(type(res))
