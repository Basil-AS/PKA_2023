import re
import copy


class LFSR:

    def __init__(self, i, length, clockingBit,
                 tappedBits): self.i, self.length, self.register, self.clockingBit, self.tappedBits = i, length, [
        0] * length, clockingBit, tappedBits

    def _getID(self):                        return self.i

    def _getRegister(self):                return self.register

    def _getBit(self, i):                    return self.register[i]

    def _getLength(self):                    return self.length

    def _getClockingBit(self):                return self.register[self.clockingBit]

    def _getTappedBits(self):                return self.tappedBits

    def _setID(self, i):                        self.i = i

    def _setLength(self, length):            self.length = length

    def _setRegister(self, register):        self.register = register

    def _setClockingBit(self, clockingBit):    self.clockingBit = clockingBit

    def _setTappedBits(self, tappedBits):    self.tappedBits = tappedBits


# Постоянные переменные
alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
r1_length = 19
r2_length = 22
r3_length = 23
key_one = ""
r1 = []
r2 = []
r3 = []


def xor(x, y): return 0 if x == y else 1


def bin_enc(pr):  # преобразуем строку в биты
    result = bin(int.from_bytes(pr.encode(encoding='utf-8'), 'big'))[2:]
    return result


def bin_dec(pr):  # преобразуем биты в строку
    pr = int(pr, 2)
    result = pr.to_bytes((pr.bit_length() + 7) // 8, 'big').decode(encoding='utf-8')
    return result


def set_key(key):  # записываем ключ в постоянные переменные
    key_one = key
    loading_registers(key)  # вызываем функцию для заполнения регистров


def loading_registers(key):  
    i = 0
    while (i < r1_length):
        r1.insert(i, int(key[i]))
        i = i + 1
    j = 0
    p = r1_length
    while (j < r2_length):
        r2.insert(j, int(key[p]))
        p = p + 1
        j = j + 1
    k = r2_length + r1_length
    r = 0
    while (r < r3_length):
        r3.insert(r, int(key[k]))
        k = k + 1
        r = r + 1


def get_majority(x, y, z):  # функция F из методички, иначе говоря определяем число для сравнения с битом синхронизации
    if (x + y + z > 1):
        return 1
    else:
        return 0


def get_keystream(length):  # функция изменения регистров
    r1_temp = copy.deepcopy(r1)
    r2_temp = copy.deepcopy(r2)
    r3_temp = copy.deepcopy(r3)
    keystream = []
    i = 0
    while i < length:
        # print(i)
        # print(r1_temp)
        # print(r2_temp)
        # print(r3_temp)
        majority = get_majority(r1_temp[8], r2_temp[10], r3_temp[10])  # вычисляем мажор
        if r1_temp[8] == majority:  # если бит синхронизации совпадает с мажором, то меняем регистр
            new = r1_temp[13] ^ r1_temp[16] ^ r1_temp[17] ^ r1_temp[18]
            r1_temp_two = copy.deepcopy(r1_temp)
            j = 1
            while (j < len(r1_temp)):
                r1_temp[j] = r1_temp_two[j - 1]
                j = j + 1
            r1_temp[0] = new

        if r2_temp[10] == majority:  # если бит синхронизации совпадает с мажором, то меняем регистр
            new_one = r2_temp[20] ^ r2_temp[21]
            r2_temp_two = copy.deepcopy(r2_temp)
            k = 1
            while (k < len(r2_temp)):
                r2_temp[k] = r2_temp_two[k - 1]
                k = k + 1
            r2_temp[0] = new_one

        if r3_temp[10] == majority:  # если бит синхронизации совпадает с мажором, то меняем регистр
            new_two = r3_temp[7] ^ r3_temp[20] ^ r3_temp[21] ^ r3_temp[22]
            r3_temp_two = copy.deepcopy(r3_temp)
            m = 1
            while (m < len(r3_temp)):
                r3_temp[m] = r3_temp_two[m - 1]
                m = m + 1
            r3_temp[0] = new_two

        keystream.insert(i, r1_temp[18] ^ r2_temp[21] ^ r3_temp[22])
        i = i + 1
    return keystream


def encode(pr):
    cryp_text = ""
    binary = bin_enc(pr)
    keystream = get_keystream(len(binary))
    i = 0
    while (i < len(binary)):
        cryp_text = cryp_text + str(int(binary[i]) ^ keystream[i])
        i = i + 1
    return cryp_text


def decode(pr):
    decryp_text = ""
    binary = []
    keystream = get_keystream(len(pr))
    i = 0
    while (i < len(pr)):
        binary.insert(i, int(pr[i]))
        decryp_text = decryp_text + str(binary[i] ^ keystream[i])
        i = i + 1
    return bin_dec(decryp_text)


sessionKey = '111101010101010100101010100110100001011110100100101010011010101010100101010101110'


def stepOne(): return (LFSR(1, 19, 8, [13, 16, 17, 18]), LFSR(2, 22, 10, [20, 21]), LFSR(3, 23, 10, [7, 20, 21, 22]))


def stepTwo(lfsrOne, lfsrTwo, lfsrThree, sessionKey):
    for bit in sessionKey:
        bit = int(bit)
        # LFSRONE #
        nMsb = xor(xor(xor(xor(lfsrOne._getBit(13), lfsrOne._getBit(16)), lfsrOne._getBit(17)), lfsrOne._getBit(18)),
                   bit)
        lfsrOne._setRegister([nMsb] + lfsrOne._getRegister()[0:lfsrOne._getLength() - 1])
        # LFSRTWO #
        nMsb = xor(xor(lfsrTwo._getBit(20), lfsrTwo._getBit(21)), bit)
        lfsrTwo._setRegister([nMsb] + lfsrTwo._getRegister()[0:lfsrTwo._getLength() - 1])
        # LFSRTHREE #
        nMsb = xor(
            xor(xor(xor(lfsrThree._getBit(7), lfsrThree._getBit(20)), lfsrThree._getBit(21)), lfsrThree._getBit(22)),
            bit)
        lfsrThree._setRegister([nMsb] + lfsrThree._getRegister()[0:lfsrThree._getLength() - 1])


def stepFour(lfsrOne, lfsrTwo, lfsrThree):
    for i in range(100):
        clockingBits = [lfsrOne._getClockingBit(), lfsrTwo._getClockingBit(), lfsrThree._getClockingBit()]
        oneCount, zeroCount = clockingBits.count(1), clockingBits.count(0)
        majorityBit = 1 if max(oneCount, zeroCount) == oneCount else 0
        # LFSRONE #
        if lfsrOne._getClockingBit() == majorityBit:
            nMsb = xor(xor(xor(lfsrOne._getBit(13), lfsrOne._getBit(16)), lfsrOne._getBit(17)), lfsrOne._getBit(18))
            lfsrOne._setRegister([nMsb] + lfsrOne._getRegister()[0:lfsrOne._getLength() - 1])
            print(lfsrOne._getRegister())
        # LFSRTWO #
        if lfsrTwo._getClockingBit() == majorityBit:
            nMsb = xor(lfsrTwo._getBit(20), lfsrTwo._getBit(21))
            lfsrTwo._setRegister([nMsb] + lfsrTwo._getRegister()[0:lfsrTwo._getLength() - 1])
        # LFSRTHREE #
        if lfsrThree._getClockingBit() == majorityBit:
            nMsb = xor(xor(xor(lfsrThree._getBit(7), lfsrThree._getBit(20)), lfsrThree._getBit(21)),
                       lfsrThree._getBit(22))
            lfsrThree._setRegister([nMsb] + lfsrThree._getRegister()[0:lfsrThree._getLength() - 1])


# key = '1110111011101110111011101110111111001111110011101110111011101110'
#эцп на рса + хэш и 94 гост

key = input('Введите ключ-бит: ')

set_key(key)
# print ("Инициалруем LFSR")
lfsrs = stepOne()
lfsrOne, lfsrTwo, lfsrThree = lfsrs[0], lfsrs[1], lfsrs[2]
proverb = input('Введите пословицу: ')
question = input("Выполнить действие (1. шифровать/2. дешифоровать): ")

print(f'Введен текст {proverb}')
if question == "1":
    print("Зашифрованный текст: ", encode(proverb))
elif question == "2":
    print("Разшифрованный текст: ", decode(proverb))


