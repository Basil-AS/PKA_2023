from script.const import ABC
from script.method import is_symbols_in, create_row, check_key


question = input("Выполнить действие (шифровать/дешифоровать): ")
proverb = input('Введите пословицу: ')
str = ""
key = input('Введите ключ-текст: ')
key *= len(proverb) // len(key) + 1


def decode(text: str, alph: str = ABC, key: str = key, **kwargs) -> str:
    result = []
    # table = create_table(alph, key)
    check_key(key, alph)
    for i, sym in enumerate(text):
        sym = sym.lower()

        if sym not in alph:
            result.append(sym)
            continue

        key_row_index = i % len(key)
        row = create_row(key[key_row_index], alph)

        col_index = row.index(sym)
        enc_sym = alph[col_index]

        result.append(enc_sym)

    return "".join(result)


def encode(text: str, alph: str = ABC, key: str = key, **kwargs) -> str:
    result = []
    check_key(key, alph)
    for i, sym in enumerate(text):
        sym = sym.lower()
        if sym not in alph:
            result.append(sym)
            continue

        key_row_index = i % len(key)
        col_index = alph.index(sym)

        row = create_row(key[key_row_index], alph)
        enc_sym = row[col_index]

        result.append(enc_sym)

    return "".join(result)



if question == "шифровать":
    print("Cообщение: " + proverb)
    print("Шифрируется: " + encode(proverb))
elif question == "дешифоровать":
    print("Cообщение: " + proverb)
    print("Декодируется: "+ decode(proverb))



