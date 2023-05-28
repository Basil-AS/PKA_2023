from script.const import ABC as alf


def atbash(s):
    proverb_text = s.translate(str.maketrans(
        alf + alf.upper(), alf[::-1] + alf.upper()[::-1]))
    return proverb_text

print(atbash(input('Введите пословицу: ')))