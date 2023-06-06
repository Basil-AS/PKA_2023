from typing import Union
from script.const import REPLACES, ABC  # Импортируем константы REPLACES и ABC из модуля script.const
from script.method import to_indexes, get_hash, clear_text, replace_special  # Импортируем функции из модуля script.method


def primes(n):
    """
    Факторизация числа n
    """
    primfac = []  # Создаем пустой список для хранения простых множителей
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # Добавляем простой множитель в список
            n //= d  # Делим число на простой множитель
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac  # Возвращаем список простых множителей


def enc(text: str, P: str, Q: str, A: str, X: str, K: str, h: int = None):
    P, Q, A, X, K = map(int, (P, Q, A, X, K))  # Преобразуем входные аргументы в целочисленные значения
    assert Q in primes(P - 1), "Q должно быть множителем для P-1"  # Проверяем, что Q является множителем для P-1
    assert (A ** Q) % P == 1, "Условие (a**q)%p==1 не соблюдено"  # Проверяем выполнение условия (a**q)%p==1
    assert 1 < A < (P - 1), "A должно ∈ (1, P-1)"  # Проверяем, что A находится в интервале (1, P-1)
    assert X < Q, "X должно быть < Q" 
    assert K < Q, "K должно быть < Q" 

    text = clear_text(text)  # Очищаем текст от специальных символов и приводим к нижнему регистру

    text_hash = get_hash(text, Q, h)  # Вычисляем хэш текста

    r = ((A ** K) % P) % Q  # Вычисляем значение r
    assert r != 0, "R не должен = 0. Попробуйте ввести другие параметры"  # Проверяем, что r не равно 0

    s = (X * r + K * text_hash) % Q  # Вычисляем значение s
    return f"{r},{s}"


# y = (pub_key.a ** x) % pub_key.p
def dec(text: str, P: str, Q: str, A: str, Y: str, ecp: str, h: int = None):
    r, s = map(int, ecp.split(","))  # Разделяем ecp на значения r и s
    P, Q, Y, A = map(int, (P, Q, Y, A))  # Преобразуем входные аргументы в целочисленные значения
    text = clear_text(text)  # Очищаем текст от специальных символов и приводим к нижнему регистру

    hashed_m = get_hash(text, Q, h)  # Вычисляем хэш текста

    v = (hashed_m ** (Q - 2)) % Q 
    z1 = (s * v) % Q  
    z2 = ((Q - r) * v) % Q
    u = ((A ** z1 * Y ** z2) % P) % Q

    return u == r  # Возвращаем результат сравнения u и r


def main():
    text_test = input("Введите пословицу: ")  # Вводим текст пословицы

    def print_kv(k, v):
        print(kv(k, v))

    def kv(k, v):
        return f"[bold cyan] {k} :[/bold cyan] {v} "

    p = int(input("Введите число для переменной p: "))
    q = int(input("Введите число для переменной q: "))
    a = int(input("Введите число для переменной a: "))
    k = int(input("Введите число для переменной k: "))
    x = int(input("Введите число для переменной x: "))
    y = (a ** x) % p  # Вычисляем значение y

    ecp = enc(text_test, p, q, a, x, k)  # Шифруем текст пословицы
    chk = dec(text_test, p, q, a, y, ecp)  # Расшифровываем текст пословицы и проверяем подпись
    print("\nПодпись пословицы", ecp)
    
    if chk:
        print("Подпись верна")
    else: print("Подпись неверна")


#47 23 3 3 7
if __name__ == "__main__":
    main()
