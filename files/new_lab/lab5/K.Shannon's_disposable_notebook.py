import alphabet


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def encode(text, a, c, t_i):
    if c % 2 == 0:
        return "Ошибка, С должно быть четным"

    if gcd(c, 32) != 1:
        return "Ошибка, С должно быть взаимнопростым с 32"

    if c > 32:
        return "Ошибка, С не должно больше модуля(32)"

    if t_i > 32:
        return "Ошибка, t_i не должно больше модуля(32)"

    if a > 32:
        return "Ошибка, a не должно больше модуля(32)"
    if a % 4 != 1:
        return "Ошика, остаток от деления A на 4 должен быть равет 1"

    # if a < 32:
    #     return "ошибка, меньше 32"
    # if 0 >= c < 32:
    #     return "ошибка, меньше 32"
    # if 0 >= t_i < 32:
    #     return "ошибка, меньше 32"

    result = ''
    for char in text:
        number = alphabet.get_pos(char)
        t_i = (a * t_i + c) % 32
        result += alphabet.get_char((number + t_i) % 32)
    return result


def decode(text, a, c, t_i):
    result = ''
    for char in text:
        number = alphabet.get_pos(char)
        t_i = (a * t_i + c) % 32
        if number > t_i:
            result += alphabet.get_char(number - t_i)
        elif number == t_i:
            result += alphabet.get_char(number)
        else:
            result += alphabet.get_char(number + 32 - t_i)
    return result


# print(encode("отодногопорченогояблокацелыйвоззагниваеттчк", 5, 7, 6))
# print(decode("утхожтюььцяйжщсщгпшечюлфвгълукънегфтыдааяящ", 5, 7, 6))
question = input("Выполнить действие (шифровать/дешифоровать): ").lower()
proverb = input("Введите пословицу: ").lower().replace(" ", "")
a = int(input("Введите a -> "))
c = int(input("Введите c -> "))
t_i = int(input("Введите t_i -> "))

if question not in ["шифровать", "дешифоровать"]:
    print("Неизвестное действие")
else:
    if question == "шифровать":

        print("Получаем: ", encode(proverb, a, c, t_i))
    else:
        # result = decode(text)
        print("Получаем: ", decode(proverb, a, c, t_i))
