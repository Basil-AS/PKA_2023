
from typing import Union


from script.const import REPLACES, ABC
from script.method import to_indexes, get_hash, clear_text, replace_special


def primes(n):
    """
    Факторизация числа n
    """
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def enc(text: str, P: str, Q: str, A: str, X: str, K: str, h: int = None):
    P, Q, A, X, K = map(int, (P, Q, A, X, K))
    assert Q in primes(P - 1), "Q должно быть множителем для P-1"
    assert (A ** Q) % P == 1, "Условие (a**q)%p==1 не соблюдено"
    assert 1 < A < (P - 1), "A должно ∈ (1, P-1)"
    assert X < Q, "X должно быть < Q"
    assert K < Q, "K должно быть < Q"

    text = clear_text(text)

    text_hash = get_hash(text, Q, h)

    r = ((A ** K) % P) % Q
    assert r != 0, "R не должен = 0. Попробуйте ввести другие параметры"

    s = (X * r + K * text_hash) % Q
    return f"{r},{s}"


# y = (pub_key.a ** x) % pub_key.p
def dec(text: str, P: str, Q: str, A: str, Y: str, ecp: str, h: int = None):
    r, s = map(int, ecp.split(","))
    P, Q, Y, A = map(int, (P, Q, Y, A))
    text = clear_text(text)

    hashed_m = get_hash(text, Q, h)

    v = (hashed_m ** (Q - 2)) % Q
    z1 = (s * v) % Q
    z2 = ((Q - r) * v) % Q
    u = ((A ** z1 * Y ** z2) % P) % Q

    return u == r


def main():
    text_test = input("Введите пословицу: ")


    def print_kv(k, v):
        print(kv(k, v))

    def kv(k, v):
        return f"[bold cyan] {k} :[/bold cyan] {v} "

    #p, q, a = 23, 11, 6
    #k = 5
    #x = 8

    p = int(input("Введите число для переменной p: "))
    q = int(input("Введите число для переменной q: "))
    a = int(input("Введите число для переменной a: "))
    k = int(input("Введите число для переменной k: "))
    x = int(input("Введите число для переменной x: "))
    y = (a ** x) % p

    ecp = enc(text_test, p, q, a, x, k)
    chk = dec(text_test, p, q, a, y, ecp)
    print("Подпись пословицы", ecp)
    print("Проверка подписи", chk)


    print("Проверка подписи", chk)


if __name__ == "__main__":
    main()
