from script.method import solve_linear_congruence
from sympy import *


def GOST_R_34_10_2012():
    message = str(input("Введите ссобщение: ")).upper()
    a = int(input("Введите коэффициент a эллиптической кривой: "))
    b = int(input("Введите коэффициент b эллиптической кривой: "))
    while (4 * (a ** 3) + 27 * (b ** 2)) == 0:
        print("Параметры не прошли условие (4*(a**3) + 27*(b**2)) != 0. Повторите ввод...")
        a = int(input("Введите коэффициент a эллиптической кривой: "))
        b = int(input("Введите коэффициент b эллиптической кривой: "))
    p = int(input("Введите модуль p эллиптической кривой: "))
    dictionary_x = {}  # Словарь значений x [0;p-1] и значений x^2 % p
    for i in range(p):  # Заполнение словаря
        k = i
        dictionary_x[k] = i ** 2 % p
    values = dictionary_x.values()  # Значения словаря
    K = 0  # Счётчик порядка эллиптической кривой
    for x in range(p):  # Цикл рассчёта порядка эллиптической кривой
        Y = (x ** 3 + a * x + b) % p
        if Y in values and Y != 0:
            K = K + 2
        elif Y in values and Y == 0:
            K = K + 1
    K = K + 1  # Добавление точки Омикрон к порядку
    print("Рассчитанный порядок эллиптической кривой: ", K)
    q = find_q(K)
    print("Получаемое q: ", q)
    Xu = int(input("Введите число 0<Xu<q: "))
    while not (Xu < q and Xu > 0):  # Проверка параметра
        Xu = int(input("Введите число 0<Xu<q: "))
    koef_a = a
    x1 = int(input("Введите координату x точки G: "))
    y1 = int(input("Введите координату y точки G: "))
    array = choice(x1, y1, Xu, p, koef_a)
    x6 = array[0]
    y6 = array[1]
    print("Открытый ключ-точка Y: ", x6, y6)
    h = hash(message)
    print("1)Вычисленный хеш: ", h)
    K = int(input("2)Введите случайное число 0<k<q: "))
    while not (K < q and K > 0):  # Проверка параметра
        K = int(input("2)Введите случайное число 0<k<q: "))
    array = choice(x1, y1, K, p, koef_a)
    x2 = array[0]
    y2 = array[1]
    print("3)Точка P эллиптической кривой с координатами: ", x2, y2)
    r = x2 % q
    print("4)Вычисленный r: ", r)
    s = (K*h+r*Xu) % q
    print("5)Вычисленный s: ", s)
    while (s==0 or r==0):
        K = int(input("Параметр s или r равен 0. Введите другое случаное число 0<K<q: "))
        while not (K < q and K > 0):  # Проверка параметра
            K = int(input("2)Введите случайное число 0<k<q: "))
        array = choice(x1, y1, K, p, koef_a)
        x2 = array[0]
        y2 = array[1]
        print("3)Точка P эллиптической кривой с координатами: ", x2, y2)
        r = x2 % q
        print("4)Вычисленный r: ", r)
        s = (K * h + r * Xu) % q
        print("5)Вычисленный s: ", s)
    print("Цифровая подпись: ", r, s)
    print("-------------------------")
    print("Проверка подписи...")
    print("1)Хеш: ", h)
    if r<q and s<q and r>0 and s>0:
        print("2)r и s проходят условия неравенств относительно q (0<r,s<q)")
    else:
        return print("2)Подпись неверна")
    u1 = solve_linear_congruence(h,s,q)
    u2 = solve_linear_congruence(h,-r,q)
    print("3)u1 и u2: ", u1, u2)
    array = choice(x1, y1, u1, p, koef_a)
    x3 = array[0]
    y3 = array[1]
    array = choice(x6, y6, u2, p, koef_a)
    x4 = array[0]
    y4 = array[1]
    param1 = x4 - x3
    param2 = y4 - y3
    if param1 == 0 and param2 == 0:
        array_p = double(x3, y3, p, koef_a)
    else:
        array_p = sum(x3, y3, x4, y4, p)
    x5 = array_p[0]
    y5 = array_p[1]
    if  x5==0 and y5==0:
        return print("4)Подпись неверна. Точка P - Омикрон")
    else:
        print("4)Точка P: ", x5, y5)
    if x5 % q == r:
        print("5)xp mod q =r. Подпись верна")
    else:
        print("5)Подпись неверна. xp mod q != r")


def find_q(K):
    array_deliteli = []
    for i in range(2, K):
        if (K % i) == 0:
            array_deliteli.append(i)
    q = 0
    while q == 0:
        param = array_deliteli[-1]
        if isprime(param):
            q = param
        else:
            array_deliteli.pop(-1)
    return q


def choice(x1, y1, Z, p, koef_a): #Функция для определения действий в зависимости от свойств числа-композиции точки
    if Z == 1:
        return [x1, y1]
    if Z % 2 == 1: #Если число нечётно
        array = func1(x1, y1, Z, p, koef_a)
        x1 = array[0]
        y1 = array[1]
        return [x1, y1]
    if (Z // 2) % 2 == 1 and Z != 2: #Если число чётно, но не является степенью двойки
        array = func2(x1, y1, Z, p, koef_a)
        x1 = array[0]
        y1 = array[1]
        return [x1, y1]
    if ((Z // 2) % 2 == 0 or Z == 2) and Z % 2 == 0: #Если число - степень двойки
        array = func3(x1, y1, Z, p, koef_a)
        x1 = array[0]
        y1 = array[1]
        return [x1, y1]


def func1(x1,y1, Cb, p, koef_a): #Если число нечётно. Пример: Cb=5. 5-1=4. 4//2=2. Вывод: нужно удвоить точку 2 раза и сложить с изначальной
    Cb = Cb - 1
    K = Cb // 2
    a = x1
    b = y1
    for i in range(K):
        array_double = double(x1, y1, p, koef_a)
        x1 = array_double[0]
        y1 = array_double[1]
    array_sum = sum(x1, y1, a, b, p)
    x1 = array_sum[0]
    y1 = array_sum[1]
    return [x1, y1]


def func2(x1, y1, Cb, p, koef_a): #Если число чётно, но не является степенью двойки. Пример: Cb=6. 6//2=3. 3-1=2. 2//2=1. Вывод: нужно удвоить точку 1 раз, сложить с изначальной и ещё раз удвоить
    Cb = Cb // 2
    Cb = Cb - 1
    K = Cb // 2
    a = x1
    b = y1
    for i in range(K):
        array_double = double(x1, y1, p, koef_a)
        x1 = array_double[0]
        y1 = array_double[1]
    array_sum = sum(x1, y1, a, b, p)
    x1 = array_sum[0]
    y1 = array_sum[1]
    array_double = double(x1, y1, p, koef_a)
    x1 = array_double[0]
    y1 = array_double[1]
    return [x1, y1]


def func3(x1, y1, Cb, p, koef_a): #Если число - степень двойки. Пример: Cb=4. 4//2=2. Вывод: нуэно удвоить точку 2 раза.
    K = 0
    while Cb != 1:
        Cb = Cb // 2
        K = K + 1
    for i in range(K):
        array_double = double(x1, y1, p, koef_a)
        x1 = array_double[0]
        y1 = array_double[1]
    return [x1, y1]


def double(x1, y1, p, koef_a): #Функция для удвоения точки
    param1 = 2*y1
    param2 = 3*(x1**2)+koef_a
    lambd = solve_linear_congruence(param1, param2, p)
    x3 = (lambd**2 - 2*x1) % p
    y3 = (lambd*(x1-x3) - y1) % p
    return [x3, y3]

GOST_R_34_10_2012()