from pygost.gost3412 import GOST3412Kuznechik as Kuz
from pygost.utils import hexdec, hexenc
from rich import print

REPLACES = {
    ",": "ЗПТ",
    ".": "ТЧК",
    "-": "ТИРЕ",
    ";": "ТЧКИЗПТ",
}

def print_header(text):
    print(header(text))


def print_kv(k, v):
    print(kv(k, v))


def header(text):
    return f"[bold black on bright_white] { text } [/bold black on bright_white]"


def kv(k, v):
    return f"[bold cyan] { k } :[/bold cyan] { v } "


default_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

def to_indexes(text, alph=default_alph):
    return [alph.index(symbol) for symbol in text]

def to_symbols(nums, alph=default_alph):
    return "".join([alph[num] for num in nums])


def clear_text(text, alph=default_alph):
    import re

    text = replace_special(text)
    text = text.lower()
    text = re.sub(f"[^{alph}]", "", text)
    return text


def replace_special(text, replaces=REPLACES):

    for key, value in replaces.items():
        text = text.replace(key, value)
    return text




def is_hex(s):
    import string

    try:
        return all(c in string.hexdigits for c in s)
    except:
        return False


def get_key(key: str) -> bytes:
    if is_hex(key):
        key = hexdec(key)
    else:
        key = bytes(key, "utf-8")
    return key


def get_text(text: str) -> bytes:
    if type(text) == str:
        if is_hex(text):
            text = hexdec(text)
        else:
            text = bytes(text, "utf-8")
    return text


def get_chipher(key: str) -> Kuz:
    key = get_key(key)
    return Kuz(key)


def enc(text: str, key: str = key):

    chipher = get_chipher(key)

    byte_text = get_text(text)
    enc_bytes = chipher.encrypt(byte_text)

    enc_text = hexenc(enc_bytes)

    return enc_text


def dec(text: str, key: str = key, t: str = "str"):

    chipher = get_chipher(key)
    byte_text = get_text(text)
    dec_bytes = chipher.decrypt(byte_text)
    dec_text = ""

    if t == "hex":
        dec_text = hexenc(dec_bytes)

    else:
        dec_text = dec_bytes.decode("utf-8")

    return dec_text


def main():
    print_header("Пример из GOST_R_34_12-2015")
    text = input("Введите текст-бит: ") #"1122334455667700ffeeddccbbaa9988" , деш_кл = 7f679d90bebc24305a468d42b9d4edcd
    key = input("Введите ключ-бит: ") #8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef
    question = input("Выполнить действие (шифровать/дешифоровать): ")

    if question == "шифровать":
        print_kv("Открытый текст", text)
        enc_text = enc(text, key)
        print_kv("Результат", enc_text)
    elif question == "дешифоровать":
        print_kv("Шифр", text)
        dec_text = dec(text, key, t="hex")
        print_kv("Расшифр.", dec_text)


if __name__ == "__main__":
    main()
