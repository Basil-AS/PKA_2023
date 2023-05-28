def format_text():
    with open('thousandtext.txt', 'r', encoding="utf-8") as file:
        text_1000 = file.read()

    text_1000 = text_1000.lower().replace(' ', 'прбл').replace('\n', 'нстрк').replace('.', 'тчк').replace(',', 'зпт').replace('!', 'вскл').replace('?', 'впрст').replace('--', 'тире').replace('-', 'дефис').replace(':', 'двт').replace('<<', 'открквч').replace('>>', 'зкрквч').replace(';', 'тчсзп')
    print('\n' + text_1000 + '\n')
    print('\tОтформатированный фрагмент содержит', len(text_1000), 'символа.')
    # return text_1000

def format_text_rev():
    text_1000 = input('\nВведите текст для форматирования: ')
    text_1000 = text_1000.lower().replace('прбл', ' ').replace('нстрк', '\n').replace('тчк', '.').replace('зпт', ',').replace('вскл', '!').replace('впрст', '?').replace('тире', '--').replace('дефис', '-').replace('двт', ':').replace('открквч', '<<').replace('зкрквч', '>>').replace('тчсзп', ';')
    print('\n' + text_1000 + '\n')
    print('\tОтформатированный фрагмент содержит', len(text_1000), 'символа.')
    # return text_1000

# format_text()
# format_text_rev()