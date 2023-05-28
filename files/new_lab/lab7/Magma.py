from pygost.gost3412 import GOST3412Magma
from pygost.utils import hexdec, hexenc


def encrypt(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)
    return hexenc(crypter.encrypt(text))


def decrypt(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)
    return hexenc(crypter.decrypt(text))


def print_header(text):
    print(header(text))


def print_kv(k, v):
    print(kv(k, v))


def header(text):
    return f"[bold black on bright_white] { text } [/bold black on bright_white]"


def kv(k, v):
    return f"{ k }: { v } "


def main():


    m = input('Введите текст-хекс: ')  #fedcba9876543210
    question = input("Выполнить действие (1.шифровать/2.дешифоровать): ")
    key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

    enc = encrypt(m, key)
    dec = decrypt(m, key)

    print_kv("Сообщение", m)
    print_kv("Ключ", key)

    if question == "1":
        print_kv("Шифровка", enc)

    elif question == "2":
        print_kv("Расшифровка", dec)


if __name__ == "__main__":
    main()
