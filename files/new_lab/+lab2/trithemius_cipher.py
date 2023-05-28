from script.const import ABC
from script.method import is_symbols_in


def check_text(text, alph):
    assert is_symbols_in(
        text, alph
    ), "Текст должен содержать только символы из алфавита"


def enc(text: str, alph: str = ABC, **kwargs) -> str:
    result = []
    check_text(text, alph)
    for i, sym in enumerate(text):
        if sym not in alph:
            result.append(sym)
            continue

        n = len(alph)
        index_alph = alph.index(sym)

        shift = (index_alph + i) % n

        result.append(alph[shift])

    return "".join(result)


def dec(text: str, alph: str = ABC, **kwargs) -> str:
    result = []

    check_text(text, alph)
    for i, sym in enumerate(text):
        if sym not in alph:
            result.append(sym)
            continue

        n = len(alph)
        index_alph = alph.index(sym)

        shift = (index_alph - i) % n

        result.append(alph[shift])

    return "".join(result)


def main():
    proverb = input('Введите пословицу: ')
    question = input("Выполнить действие (шифровать/дешифровать): ")
    c_code = enc(proverb)
    code = dec(proverb)
    print(f'Исходное сообщение: {proverb}')

    if question == "шифровать":
        print(f'Зашифрованное сообщение: {c_code}')
    elif question == "дешифровать":
        print(f'Дешиврованное сообщение: {code}')
    (enc, dec)


main()