import inspect
import math
from typing import List
from script.const import ABC, REPLACES


def alphabet_enumeration(proverb, ABC):
    cycle, list_abc = 0, []
    for symbol in ABC:
        for text in proverb:
            list_abc.append(ABC.index(proverb[cycle]))
            cycle += 1
        return list_abc


def lover_text(text):
    text = (text.lower().replace(" ", ""))
    return text


def input_matrix():
    matrix = []
    print("Если хотите закончить введите end!")
    while True:
        line = [index for index in input("Введите номера в строку: ").split()]
        if 'end' in line:
            break
        number = [int(i) for i in line]
        matrix.append(number)
    return matrix


def addind_symbl(text):
    list = []
    for sumbl in text:
        list.append(sumbl)
    return list


def clear_text(text, alph=ABC):
    import re
    text = replace_special(text)
    text = text.lower()
    text = re.sub(f"[^{alph}]", "", text)
    return text


def replace_special(text, replaces=REPLACES):
    for key, value in replaces.items():
        text = text.replace(key, value)
    return text


def random_char(alph=ABC):
    from random import choice
    return choice(alph)


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def alph_to_sq(alph: str) -> List[List[str]]:
    from math import ceil, sqrt

    n = ceil((sqrt(len(alph))))
    sq = [[char for char in alph[i * n : (i + 1) * n]] for i in range(n)]
    return sq


def is_int(s):
    if s[0] in ("-", "+"):
        return s[1:].isdigit()
    return s.isdigit()


def is_hex(s):
    import string
    try:
        return all(c in string.hexdigits for c in s)
    except:
        return False


def kv_hash(msg: str, p: int = 11) -> int:
    h = 0
    h_list = []
    for symbol_code in to_indexes(msg):
        symbol_code += 1
        h = ((h + symbol_code) ** 2) % p
        h_list.append(h)
    return h


def get_hash(
    message: str,
    q: int,
    h: int = None,
):
    hashed_m = h if h else kv_hash(message)
    hashed_m = 1 if hashed_m % q == 0 else hashed_m

    return hashed_m


def is_symbols_in(text, symbols):
    from re import search

    pattern = f"[\d]"
    return False if search(pattern, text) else True


def check_key(key, alph):
    assert is_symbols_in(key, alph), "Ключ должен содержать только символы из алфавита"


def create_row(sym: str, alph: str) -> str:
    row = alph[alph.index(sym) :] + alph[: alph.index(sym)]
    return row


def check_key(key, alph):
    assert is_symbols_in(key, alph), "Ключ должен содержать только символы из алфавита"


def to_indexes(text, alph=ABC):
    return [alph.index(symbol) for symbol in text]


def to_symbols(nums, alph=ABC):
    return "".join([alph[num] for num in nums])


def change_array(array, message, grid_zeros):
    for item in range(len(grid_zeros)):
        if grid_zeros[item] == '1':
            array[item] = message[0]
            message = message[1:]
    return array, message


def change_array_2(array, message, grid_zeros, count_change):
    for item in range(len(grid_zeros)):
        if grid_zeros[item] == '1':
            array[count_change] = message[item]
            count_change += 1
    return array, count_change


def flip_horizontal(grid_zeros, grid_length, grid_width):
    temp = grid_zeros[:grid_width]
    temp = temp[::-1]
    grid_zeros = temp + grid_zeros[grid_width:]

    for i in range(1, grid_length - 1):
        temp = grid_zeros[i * grid_width:i * grid_width + grid_width]
        temp = temp[::-1]
        grid_zeros = grid_zeros[:i * grid_width] + temp + grid_zeros[i * grid_width + grid_width:]

    temp = grid_zeros[len(grid_zeros) - grid_width:]
    temp = temp[::-1]
    grid_zeros = grid_zeros[:len(grid_zeros) - grid_width] + temp

    return grid_zeros


def flip_vertical(grid_zeros, grid_length, grid_width):
    for i in range(grid_width):
        for j in range(grid_length // 2):
            temp1 = grid_zeros[j * grid_width + i]
            temp2 = grid_zeros[grid_width * grid_length - 1 - j * grid_width - (grid_width - i - 1)]
            grid_zeros = grid_zeros[:j * grid_width + i] + temp2 + grid_zeros[j * grid_width + i + 1:grid_width * grid_length - 1 - j * grid_width - (grid_width - i - 1)] + temp1 + grid_zeros[grid_width * grid_length - 1 - j * grid_width - (grid_width - i - 2):]
        # print_matrix(grid_zeros, grid_width)
        # print()
    return grid_zeros


def get_decimal_alphabet(b):
    string_s = []
    for i in range(len(b)):
        string_s.append(ABC.index(b[i]))
    return string_s


def get_alphabet():
    return ABC


def get_pos(c):
    return ABC.index(c) + 1


def get_char(n):
    return ABC[n-1]


def solve_linear_congruence(a, b, m): #Функция для решения модульных сравненений
    g = math.gcd(a, m) #НОД a и m
    if b % g:
        raise ValueError("No solutions")
    a, b, m = a//g, b//g, m//g
    return (a, (-1), m) * b % m #вычисление


def hash(message):
    alphabet = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#,.!?:;{ }[]\'\"-'
    h = 0  # Начальное значение хэша
    p = 37  # Модуль в хэшировании
    for i in range(len(message)):
        h = (h + (alphabet.index(message[i]) + 1)) ** 2 % p  # Вычисление
        if hash == 0:
            hash == 1
    return h
