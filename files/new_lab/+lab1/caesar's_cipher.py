from script.const import ABC as alf



def caesar_encrypt(text, alf, shift ):
    def get_new_lower_let(x):
        return alf[ ( alf.index(x)+shift ) % len(alf) ]

    def get_new_let(x):
        if x.isupper():
            return get_new_lower_let( x.lower() ).upper()
        return get_new_lower_let(x)

    text = [ x for x in text if x.isalpha() ]
    return ''.join( list( map( get_new_let, text ) ) )


def caesar_decrypt(text, alf, shift ):
    def get_new_lower_let(x):
        return alf[ ( alf.index(x)-shift ) % len(alf) ]

    def get_new_let(x):
        if x.isupper():
            return get_new_lower_let( x.lower() ).upper()
        return get_new_lower_let(x)

    text = [ x for x in text if x.isalpha() ]
    return ''.join( list( map( get_new_let, text ) ) )


def main():
    shift_text = int(input('Введите сдвиг: '))
    proverb = input('Введите пословицу: ')
    question = input("Выполнить действие (шифровать/дешифровать): ")
    c_code = caesar_encrypt( proverb, alf, shift_text)
    code = caesar_decrypt( proverb, alf, shift_text )
    print(f'Исходное сообщение: {proverb}')
    print(f'Сдвиг: {shift_text}')
    if question == "шифровать":
        print(f'Зашифрованное сообщение: { c_code }')
    elif question == "дешифровать":
        print(f'Дешиврованное сообщение: { code }' )

main()