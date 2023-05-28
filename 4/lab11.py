"""Лабораторная работа 11.Обмен ключами по алгоритму Diffie–Hellman

1.Обменяться ключами с виртуальным пользователем - Блок K: Обмен ключами*

28. Diffie-Hellman

2. Подготовить отчет в соответствие с требованиями  Методических указаний*."""

from modulo import modulo
from random import randint

# Функция проверки числа на простоту
def simple_number(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        print('Число "{}"— простое.'.format(number))
        return number
    else:
        number = int(input("Число не является простым, попробуйте еще раз: "))
        return simple_number(number)

# Функция проверки условия (1 < a < n)
def check_A(a, n):
    if 1 < a and a < n:
        print('Число "{}" — подходит.\n'.format(a))
        return a
    else:
        a = int(input('Число не подходит. Введите a (1 < a < n): '))
        return check_A(a, n)

# Проверка секретных ключей kA и kB
def check_kA_kB(k, n):
    if 2 < k and k < n-1:
        print('K. Число "{}" — подходит.'.format(k))
        return k
    else:
        # k = int(input('Число не подходит. Введите a (2 < k < n-1): '))
        k = randint(3, n-2)
        return check_kA_kB(k, n)

# Y=a^K mod n
def search_Y(a, k, n):
    y = int(modulo(a ** k, n))
    # print('y = {}'.format(y))
    return y
'''
# Ввод переменных
print()
n = int(input('Введите большое простое число "n": '))
n = simple_number(n)

a = int(input('Введите число "a" (1 < a < n): '))
a = check_A(a, n)
'''
# 1. Определить секретные ключи пользователей kА и kВ
# 2. Для этого каждый пользователь независимо выбирает случайные числа из 
# интервала (2,..., n-1)

# Функция алгоритма
def algorithm(a, n):
    kA = randint(3, n-2)
    # kA = int(input('Введите "kA"из интервала (2, ..., n-1): '))
    kA = check_kA_kB(kA, n)
    
    kB = randint(3, n-2)
    # kB = int(input('Введите "kB"из интервала (2, ..., n-1): '))
    kB = check_kA_kB(kB, n)
    
    # 3. Вычислить открытые ключи пользователей YA и YB:
    # Y=a^K mod n
    
    yA = search_Y(a, kA, n)
    yB = search_Y(a, kB, n)
    print('\nyA = {}, yB = {}'.format(yA, yB))
    return yA, yB, kA, kB

# 4. Обменяться ключами YA и YB по открытому каналу связи.
# 5. Независимо определить общий секретный ключ К:
# kA=yB^kA mod n
# kB=yA^kB mod n

# Проверка на единицу
def check_1(yA, yB, kA, kB, a, n):
    kA = int(modulo(yB**kA, n))
    kB = int(modulo(yA**kB, n))
    if kA == 1 or kB == 1:
        yA, yB, kA, kB = algorithm(a, n)
        return check_1(yA, yB, kA, kB, a, n)
    else:
        return kA, kB
'''
yA, yB, kA, kB = algorithm(a, n)
kA, kB = check_1(yA, yB, kA, kB, a, n)
print('kA = {}, kB = {}'.format(kA, kB))
'''
# ----------- для терминала ----------

def Diffie_Hellman_exchange():
    n = int(input('\nВведите большое простое число "n": '))
    n = simple_number(n)
    a = int(input('\nВведите число "a" (1 < a < n): '))
    a = check_A(a, n)
    yA, yB, kA, kB = algorithm(a, n)
    kA, kB = check_1(yA, yB, kA, kB, a, n)
    print('kA = {}, kB = {}'.format(kA, kB))