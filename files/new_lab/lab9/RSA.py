alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
            'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# Функция, которая преобразует числа в буквы
def numberToLetter(text):
    strInLetter = ''
    for i in text:
        if i == 0:
            strInLetter += ' '
        else:
            strInLetter += alphabet[i-1]
    return strInLetter

# Функция, которая заменяет символы в тексте
def replacer(text):
    text = text.replace('ё', 'е')
    text = text.replace(',', 'зпт').replace('.', 'тчк').replace('-', 'тире')
    text = text.lower()
    return text

# Функция, которая преобразует буквы в числа
def letterToNumber(text):
    strInNumber = []
    if type(text) is str:
        text = replacer(text)
    for letter in text:
        if letter == ' ':
            strInNumber.append(0)
        else:
            strInNumber.append((alphabet.index(letter) + 1))
    return strInNumber

# Функция, которая проверяет число на простоту
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция, которая находит НОД двух чисел
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Функция, которая находит мультипликативно обратный элемент по модулю
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

# Функция, которая генерирует открытый и закрытый ключи
def generate_keypair(p: int, q: int):
    while not (is_prime(p) and is_prime(q) and p != q):
        print('p и/или q не простое число или p = q')
        p = int(input('Введите p: '))
        q = int(input('Введите q: '))

    n = p * q
    phi = (p-1) * (q-1)
    print('Функция Эйлера равна: ', phi)

    e = int(input('Введите e: '))
    while gcd(e, phi) != 1 or e < 1 or e > phi:
        print('Не выполняются условия: 1 < e < phi и e с phi взаимно просты')
        e = int(input('Введите e: '))

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

# Функция шифрования RSA
def encrypt_rsa(pk, plaintext):
    cipher = []
    key, n = pk
    for char in plaintext:
        cipher.append(pow(char, key, n))
    return cipher

# Функция расшифрования RSA
def decrypt_rsa(pk, ciphertext):
    plain = []
    key, n = pk
    for char in ciphertext:
        plain.append((pow(char, key, n)))
    return plain

# Функция, которая применяет RSA к тексту
def crypt_rsa(pk, beforetext):
    aftertext = []
    key, n = pk
    for char in beforetext:
        aftertext.append((pow(char, key, n)))
    return aftertext

# Функция хеширования
def hash(phr, mod):
    h=[0]
    for ind, i in enumerate(phr, 1):
        t = ((h[ind-1]+alphabet.index(i)+1)**2) % mod
        h.append(t)
    if h[-1] == 0:
        h.append(1)
    return(h)

def rsa():
    p = 11
    q = 3
    public_key, private_key = generate_keypair(p, q)
    print('e, n =', public_key, 'd, n =', private_key)

    message = "времязптприливыиотливынеждутчеловекатчк"
    num_message = letterToNumber(message)
    print('num message: ', num_message)
    encrypted_message = encrypt_rsa(public_key, num_message)
    print("Зашифрованный текст:", encrypted_message)
    print("Зашифрованный текст:", numberToLetter(encrypted_message))

    decrypted_message = decrypt_rsa(private_key, encrypted_message)
    print("\nРасшифрованный текст:", decrypted_message)
    print("\nРасшифрованный текст:", numberToLetter(decrypted_message))

def rsa_sign():
    message = input("Введите текст: ")

    p = int(input("Введите p: "))
    q = int(input("Введите q: "))
    public_key, private_key = generate_keypair(p, q)
    print('e, n =', public_key, 'd, n =', private_key)

    hash_message = []
    hash_message.append(hash(message, 47)[-1])
    print('hash message: ', *hash_message)
    signed_message = crypt_rsa(private_key, hash_message)
    print("Подпись: ", *signed_message, public_key[-1])

    checked_message = crypt_rsa(public_key, signed_message)
    print("\nПроверка подписи: ", *checked_message)
    if hash_message == checked_message:
        print("Подпись верна")
    else: print("Подпись неверна")

#47 13 13 

if __name__ == "__main__":
    rsa_sign()
