from script.const import ABC, POLYBIUS_SQUARE as square
from  script.method import is_int, alph_to_sq

matrixHeight = len(square);
matrixWidth = len(square[0]);

def enc(text: str, alph: str = ABC, **kwargs) -> str:

    answer = []
    sq = alph_to_sq(alph)

    for sym in text:
        sym = sym.lower()

        for row in sq:
            if sym not in row:
                continue
            num = str(sq.index(row) + 1) + str(row.index(sym) + 1)
            answer.append(num)

    return " ".join(answer)


def dec(text: str, alph: str = ABC, **kwargs) -> str:
    text = text.split()
    assert all(is_int(i) for i in text), "Шифр должен состоять из чисел"
    sq = alph_to_sq(alph)
    return "".join([sq[int(sym[0]) - 1][int(sym[1]) - 1] for sym in text])



proverb = input('Введите пословицу: ')
question = input("Выполнить действие (шифровать/дешифоровать): ")

if question == "шифровать":
    print("Зашифрованное сообщение: " + enc(proverb));

elif question == "дешифоровать":
    print("Дешеврованное сообщение: " + dec(proverb));


