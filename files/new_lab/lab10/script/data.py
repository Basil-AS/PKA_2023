from types import FunctionType
from script.method import get_default_args

cardan_data = [
    "тКПзнатрсо",
    "_еотсдпрое",
    "влавеитсшт",
    "откар_яоевл",
    "мпю_щтояор",
    "еуотс_одюб",
    "пиоосртйсо",
    "гмяянсетор",
    "у_кт_гтчзо",
    "купрркута "
]


grid_kardano = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
]


def test_crypt(enc: FunctionType, dec: FunctionType) -> None:
    from script.method import clear_text

    text_1000 = """
    Современные технологии достигли такого уровня, что выбранный нами инновационный путь предполагает независимые способы реализации соответствующих условий активизации. Принимая во внимание показатели успешности, новая модель организационной деятельности, а также свежий взгляд на привычные вещи - безусловно открывает новые горизонты для укрепления моральных ценностей. Лишь сделанные на базе интернет-аналитики выводы неоднозначны и будут обнародованы. Ясность нашей позиции очевидна: высокотехнологичная концепция общественного уклада предполагает независимые способы реализации укрепления моральных ценностей.
    Прежде всего, курс на социально-ориентированный национальный проект, а также свежий взгляд на привычные вещи - безусловно открывает новые горизонты для экспериментов, поражающих по своей масштабности и грандиозности. С другой стороны, реализация намеченных плановых заданий создаёт предпосылки для вывода текущих активов. Мы вынуждены отталкиваться от того, что понимание сути ресурсосберегающих технологий однозначно определяет каждого участника как способного принимать собственные решения касаемо как самодостаточных, так и внешне зависимых концептуальных решений. Ясность нашей позиции очевидна: глубокий уровень погружения способствует повышению качества приоритизации разума над эмоциями. В частности, семантический разбор внешних противодействий влечет за собой процесс внедрения и модернизации поставленных обществом задач
    """

    text_test = "Кто слишком торопится зпт застревает по дороге тчк"

    text_test = clear_text(text_test)
    text_1000 = clear_text(text_1000)

    print("Тест на пословице и тексте: ")

    _enc = enc(text_test)
    print("Шифровка пословицы: ", _enc)

    _dec = dec(_enc)
    print("Расшифровка пословицы: ", _dec)

    _enc = enc(text_1000)
    print("Шифровка 1000: ", _enc)

    _dec = dec(_enc)
    print("Расшифровка 1000: ", _dec)


