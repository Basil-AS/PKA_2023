from script.const import ABC as alphabet


def vigenere_encrypt(text):
    key = input('Введите ключ-текст: ')
    result = []
    space = 0

    for index, symbol in enumerate(text):
        if symbol != " ":
            index_1 = alphabet.index(symbol)
            index_2 = alphabet.index(key[(index - space) % len(key)])
            index_result = (index_1 + index_2) % len(alphabet)
            result.append(alphabet[index_result])
        else:
            space += 1
            result.append(" ")

    return "".join(result)


def vigenere_decrypt(text):
    key = input("Введите ключ-текст: ")
    result = []
    space = 0

    for index, symbol in enumerate(text):
        if symbol != " ":
            index_1 = alphabet.index(symbol)
            index_2 = alphabet.index(key[(index - space) % len(key)])
            index_result = (index_1 - index_2) % len(alphabet)
            result.append(alphabet[index_result])
        else:
            space += 1
            result.append(" ")

    return "".join(result)



question = input("Выполнить действие (шифровать/дешифоровать): ")
proverb = input('Введите пословицу: ').lower().replace(" ", "")

if question == "шифровать":
    print("Cообщение: " + proverb)
    print("Шифрируется: " + vigenere_encrypt(proverb))
elif question == "дешифоровать":
    print("Cообщение: " + proverb)
    print("Декодируется: "+ vigenere_decrypt(proverb))
