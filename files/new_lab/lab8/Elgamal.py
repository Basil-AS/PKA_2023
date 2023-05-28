import math
import random
from script.method import solve_linear_congruence

def elgamal():
    question = input("Выполнить действие (шифровать/дешифоровать): ")
    message = input("Введите пословицу: ").upper()
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#,.!?:;{ }[]\'\"-'
    P = int(input("Введите параметр P - большое простое число: ")) #Вводим ключ P
    G = int(input("Введите параметр G - большое целое число меньшее P: ")) #Вводим ключ G
    if not G < P: #Проверка параметра
        G = int(input("Введите параметр G - большое целое число меньшее P: "))
    X = int(input("Введите параметр X - целое число в пределах 1 < X <= (P-1): "))  # Вводим ключ X
    if not (X > 1 and X < (P-1)): #Проверка параметра
        X = int(input("Введите параметр X - целое число в пределах 1 < X <= (P-1): "))
    Y = G**X % P #P,G,Y - открытые ключи, X - секретный ключ
    print("Открытый ключ Y: ", Y)
    F = P - 1 #Функция Эйлера от числа P
    array = [] #Массив чисел, взаимно простых с F
    for i in range(2,F): #Заполнение массива
        Z = math.gcd(i, F)
        if Z == 1:
            array.append(i)
    print("Числа, взаимно простые с функцией Эйлера от числа P: ", array)

    #array_k = [5, 11, 13, 11, 5, 13, 13, 5, 5, 11, 11, 5, 13, 13, 11, 11, 5, 11, 13, 5, 5, 5, 11, 11, 13, 13, 5, 11, 5, 5, 13, 13, 11, 11, 5, 5, 13, 13, 11, 5] #Мой массив рандомных k для пословицы
    #print("Массив рандомных k для пословицы: ", array_k)

    array_k = []
    for i in range(10):
        Z = random.choice(array)
        if random.choice(array) not in array_k:
            array_k.append(Z)
        else:
            i = i - 1


    if question == "шифровать": #Действия для зашифрования
        print("Случайные секретные числа k: ", array_k)
        result=""
        for i in message: #Зашифровка
            Z = random.choice(array_k) #Берём случайный k из массива случайных k
            a = (G ** Z) % P #Вычисляем a
            b = ((Y ** Z) * (alphabet.index(i)+1)) % P #Вычисляем b
            if len(str(a)) != 2: #Если а - цифра, добавляем 0 вперёд
                a = '0'+str(a)
            if len(str(b)) != 2: #Если b - цифра, добавляем 0 вперёд
                b = '0'+str(b)
            result += str(a)+str(b) #Конкатенируем a и b в результат
        new_result = "" #Далее идут действия для представления результата в виде пятёрок
        L = math.ceil(len(result) // 5)
        H = len(result)
        for i in range(L+1):
            five_symb = result[0:H // L]
            new_result += five_symb + " "
            result = result[5:]
        print("Результат зашифровки: ", new_result)
    if question == "дешифоровать": #Действия для расшифрования
        result=""
        message = message.replace(" ", "") #В вводимой строке из пятёрок и пробелов убираю пробелы
        array = []
        L = len(message) // 2
        for i in range(L): #Делю строку на массив двоичных чисел
            array.append(message[0:2])
            message = message[2::]
        for i in range(0, len(array), 2): #Расшифровываю
            M = solve_linear_congruence(int(array[i])**X, int(array[i+1]), P) #Решаю модульное сравнение относительно M
            result += alphabet[M-1] #Добавляю в результат
        print("Результат расшифровки: ", result)


elgamal()