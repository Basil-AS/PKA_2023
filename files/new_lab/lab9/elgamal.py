import math


message = input("Сообщение: ").upper() #Кто слишком торопится зпт застревает по дороге тчк


def elgamal():
    P = int(input("Введите параметр P - большое простое число: "))  # Вводим ключ P
    G = int(input("Введите параметр G - большое целое число меньшее P: "))  # Вводим ключ G
    if not G < P:
        G = int(input("Ошибка! Введите параметр G - большое целое число меньшее P: "))
    X = int(input("Введите параметр X - целое число в пределах 1 < X <= (P-1): "))  # Вводим ключ X
    if not (X > 1 and X < (P - 1)):
        X = int(input("Ошибка! Введите параметр X - целое число в пределах 1 < X <= (P-1): "))
    Y = G ** X % P  # Y - открытый ключ, X - секретный ключ
    m = hash(message)  # Хэширование сообщения
    print("Вычисленный хеш m: ", m)
    K = int(input(
        "Введите параметр K - целое число в пределах 1 < K <= (P-1) и взаимно простое с (P-1): "))  # Вводим ключ K
    if not (K > 1 and K < (P - 1) and math.gcd(K, (P - 1)) == 1):
        K = int(input("Ошибка! Введите параметр K - целое число в пределах 1 < K <= (P-1) и взаимно простое с (P-1): "))

        # Действия отправителя

    a = G ** K % P
    # m = Х*а + К*b (mod (Р-1))
    # -K*b = X*a - m (mod (P-1)).
    Z = X * a - m
    str_int = 36
    b = solve_linear_congruence(-K, Z, str_int)
    print("Цифровая подпись S: ", a, b)


    A1 = (Y ** a * a ** b) % P
    A2 = G ** m % P
    print("A1: ", A1)
    print("A2: ", A2)
    if A1 == A2:
        print("Подпись верна!")
    else:
        print("Подпись не верна!")


def solve_linear_congruence(a, b, m): #Функция для решения модульных сравненений
    g = math.gcd(a, m) #НОД a и m
    if b % g:
        raise ValueError("No solutions")
    a, b, m = a//g, b//g, m//g
    return pow(a,m-1) * b % m #вычисление


def hash(message):
    alphabet = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#,.!?:;{ }[]\'\"-'
    h = 0  # Начальное значение хэша
    p = 37  # Модуль в хэшировании
    for i in range(len(message)):
        h = (h + (alphabet.index(message[i]) + 1)) ** 2 % p  # Вычисление
        if hash == 0:
            hash == 1
    return h


elgamal()