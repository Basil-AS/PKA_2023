import math
from modulo import modulo

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Функция для проверки простоты числа
def simple_number(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):   
            k = k + 1
    if (k <= 0):
        print("Число", number, "— простое.")
        return number
    else:
        number = int(input("Число не является простым, попробуйте еще раз: "))
        return simple_number(number)
    
# Функция для вычисления функции Эйлера
def euler_function(number):
    value = 0
    for k in range(1, number + 1):
        if math.gcd(number, k) == 1:
            value += 1
    return value

# Функция для проверки, что числа взаимно простые (НОД = 1)
def relatively_prime(num1, num2):
    if math.gcd(num1, num2) != 1:
        num2 = int(input(
            'НОД чисел {} и {} не равен 1. Введите другое число "E": '.format(num1, num2)))
        return relatively_prime(num1, num2)
    else:
        print('НОД чисел {} и {} равен 1, все верно.'.format(num1, num2), '\n')
        return num1, num2
    
# Функция для преобразования текста в список чисел, соответствующих индексам символов в алфавите
def text_to_numbers(text):
    numbers = []
    for i in range(len(text)):
        numbers.append(alphabet.index(text[i]) + 1)
    return numbers

# Функция для преобразования списка чисел обратно в текст, используя алфавит
def numbers_to_text(numbers):
    text = ''
    for number in numbers:
        text += alphabet[number - 1]
    return text

# Функция для шифрования текста с использованием алгоритма RSA
# Возведение каждого числа из списка чисел (представления текста) в степень E и вычисление остатка от деления на N
def rsa_encrypt(text, e, n):
    numbers = text_to_numbers(text)
    encrypted_numbers = [int(modulo(number ** e, n)) for number in numbers]
    return numbers_to_text(encrypted_numbers)

# Функция для дешифрования текста с использованием алгоритма RSA
# Возведение каждого числа из списка чисел (представления зашифрованного текста) в степень D и вычисление остатка от деления на N
def rsa_decrypt(encrypted_text, d, n):
    encrypted_numbers = text_to_numbers(encrypted_text)
    decrypted_numbers = [int(modulo(number ** d, n)) for number in encrypted_numbers]
    return numbers_to_text(decrypted_numbers)

def main():
    text = 'цепьнекрепчесвоегосамогослабогозвенатчк'

    p = simple_number(int(input('Введите простое число "p": ')))
    q = simple_number(int(input('Введите простое число "q": ')))

    n = p * q
    print('N = ', n)

    # Вычисление функции Эйлера от N
    euler_n = euler_function(n)
    print('Функция Эйлера от N =', euler_n)

    # Ввод числа E, взаимно простого с функцией Эйлера от N
    e = int(input('Введите целое число E, взаимно простое с функцией Эйлера от N: '))
    euler_n, e = relatively_prime(euler_n, e)

    # Вычисление числа D (обратное к E по модулю функции Эйлера от N)
    d = modulo(1, euler_n) // e
    d = int(d)  # Преобразуем d обратно в int
    print('D равно:', d, '\n')

    encrypted_text = rsa_encrypt(text, e, n)
    print("Шифрованный текст:", encrypted_text, '\n')

    decrypted_text = rsa_decrypt(encrypted_text, d, n)
    print("Расшифрованный текст:", decrypted_text)

if __name__ == "__main__":
    main()

