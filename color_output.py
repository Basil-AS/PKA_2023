class Color:
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7


def color_print(text, color=Color.WHITE, bold=False, underline=False, end='\n'):
    """
    Выводит текст с указанным цветом, жирностью и подчеркиванием.

    :param text: Текст для вывода
    :param color: Цвет текста (используйте константы из класса Color)
    :param bold: Жирный текст (True/False)
    :param underline: Подчеркнутый текст (True/False)
    :param end: символ конца строки
    """
    style_code = 0
    if bold:
        style_code |= 1
    if underline:
        style_code |= 4

    print(f'\033[{style_code};3{color}m{text}\033[0m', end=end)


if __name__ == '__main__':
    color_print('Hello, World!', color=Color.GREEN, bold=True, underline=True)


"""
\033[<style_code>;<foreground_color_code>;<background_color_code>m
Коды цветов для заднего плана (background) аналогичны кодам переднего плана, но начинаются с 40.
\033[0m сбрасывает стили и цвета в конце строки
"""