from sympy import *
from script.method import solve_linear_congruence

def rsa():
    action = str(input("Выполнить действие (шифровать/дешифоровать): "))
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#,.!?:;{ }[]\'\"-'
    message = input("Введите пословицу: ").upper()
    p = int(input("Введите параметр p - большое простое число: ")) #Вводим ключ p
    if not isprime(p):
        p = int(input("p просто число. Повторите ввод: "))  # Вводим ключ p
    q = int(input("Введите параметр q - большое простое число: ")) #Вводим ключ q
    if not isprime(q):
        q = int(input("q просто число. Повторите ввод: "))  # Вводим ключ p
    N = p*q
    F = (p-1)*(q-1) #Функция Эйлера от числа N
    print("N =", N)
    E = int(input("Введите параметр E - число, взаимно простое с N: ")) #Вводим ключ E
    D = solve_linear_congruence(E, 1, F) #Решение модульного сравнения
    print("Вычисленный ключ D: ", D)
    result = ""
    if action == "шифровать": #Действия для зашифрования
        for i in range(len(message)):
            Z = ((alphabet.index(message[i])+1)**E) % N #Зашифровка
            if len(str(Z)) != 2: #Если результат - цифра, то добавляем ноль вперёд
                Z = "0"+str(Z)
            result += str(Z)
        new_result = ""
        L = len(result) // 5 #Далее идут действия для представления результата в виде пятёрок
        H = len(result)
        for i in range(L):
            five_symb = result[0:H // L]
            new_result += five_symb + " "
            result = result[5:]
        print("Результат шифрования: ", new_result)
    if action == "дешифоровать": #Действия для расшифрования
        message = message.replace(" ", "") #В вводимой строке из пятёрок и пробелов убираю пробелы
        array = []
        L = len(message) // 2 #Далее делю строку на массив из двоичных чисел
        for i in range(L):
            array.append(message[0:2])
            message = message[2::]
        for i in array: #Расшифровываю
            result += alphabet[(int(i)**D % N)-1]
        print("Результат расшифровки: ", result)


rsa()