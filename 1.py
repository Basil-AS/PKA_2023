import numpy as np

# ALPH = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# str = input('Введите строку: ')
# str = str.lower()


# Создаем первую матрицу
key = np.array([[1, 4, 8], [3, 7, 2], [6, 9, 5]])

# Создаем вторую матрицу
m2 = np.array([8, 1, 2])

# Перемножаем их
result = np.dot(key, m2)

# Выводим результат
print(result)
