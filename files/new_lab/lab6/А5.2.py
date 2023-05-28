# Импорт функций для обработки текста, работы ввода/вывода, проверки ввода/вывода.
from script.method import strToBin, binToStr, encodingFormat, normalText, isBinary, inputText, saveOutput


# Функция поиска мажоритарного бита
def matchMajor(b1, b2, b3):
    b1 = int(b1)
    b2 = int(b2)
    b3 = int(b3)
    return int((b1 and b2) or (b1 and b3) or (b2 and b3))

# Функция, которая принимает на вход введенные пользователем ключ и длину гаммы
# и возвращает получившуюся гамму
def createGamma(sKey, gammaLen):
    R1 = sKey[:19]
    R2 = sKey[19:41]
    R3 = sKey[41:64]
    R4 = sKey[64:81]
    gamma = ''
    for i in range(gammaLen):
        # print(i, "гамма: ", str(int(R1[-1]) ^ int(R2[-1]) ^ int(R3[-1]) ^ matchMajor(R1[15], R1[14], R1[12]) ^ matchMajor(R2[16], R2[13], R2[9]) ^ matchMajor(R3[18], R3[16], R3[13])))
        S1 = int(R4[3])
        S2 = int(R4[7])
        S3 = int(R4[10])
        gamma += str(int(R1[-1]) ^ int(R2[-1]) ^ int(R3[-1]) ^ matchMajor(R1[15], R1[14], R1[12]) ^ matchMajor(R2[16], R2[13], R2[9]) ^ matchMajor(R3[18], R3[16], R3[13]))
        F = matchMajor(S1, S2, S3)
        if S1 == F:
            # получение нового бита происходит путем применения операции XOR к соответствующим битам регистра
            nBit = int(R2[21]) ^ int(R2[20])
            R2 = str(nBit) + R2[:21]
        if S2 == F:
            # получение нового бита происходит путем применения операции XOR к соответствующим битам регистра
            nBit = int(R3[22]) ^ int(R3[21]) ^ int(R3[20]) ^ int(R3[7])
            R3 = str(nBit) + R3[:22]
        if S3 == F:
            # получение нового бита происходит путем применения операции XOR к соответствующим битам регистра
            nBit = int(R1[18]) ^ int(R1[17]) ^ int(R1[16]) ^ int(R1[13])
            R1 = str(nBit) + R1[:18]
        R4 = str(int(R4[16]) ^ int(R4[11])) + R4[:16]
    return gamma

# Функция рас/шифрования.
def encode(gamma, text):
    result = ""
    for i in range(len(text)):
        result += str(int(text[i]) ^ int(gamma[i]))
    return result


def main():
    print("Шифр А5/2")
    question = input("Выполнить действие (шифровать/дешифоровать): ")
    # Ввод ключа в формате bin с размером 81.
    while True:
        sKey = input("Введите ключ в формате Binary длиной 81 символов: ").upper()
        if isBinary(sKey):
            if len(sKey) == 81:
                break
            elif (sKey == ""):
                sKey = '111010110100001001111011100011101000110001010101111111011010100110011001101110101'
                break
            else:
                print("Длина ключа не 81 символов")
    # Шифрование.
    if (question == "шифровать"):
        text = inputText()
        if not (isBinary(text)):
            text = strToBin(encodingFormat(text))
        gamma = createGamma(sKey, len(text))
        result = encode(gamma, text)
        print('Шифрование:', result)
        saveOutput(result)
        print("Результат работы программы в output.txt")
    # Расшифрование.
    elif (question == "дешифоровать"):
        text = inputText()
        if (isBinary(text)):
            gamma = createGamma(sKey, len(text))
            while True:
                toBin = input("Вывести в формате Binary? (Y/N)\n")
                if (toBin == "Y") or (toBin == "N"):
                    break
            if (toBin == "Y"):
                result = encode(gamma, text)
            elif (toBin == "N"):
                result = normalText(binToStr(encode(gamma, text)))
            print('Текст:', result)
            saveOutput(result)
            print("Результат работы программы в output.txt")
    # Ошибочный ввод.
    else:
        print("Некорректный ввод.")
