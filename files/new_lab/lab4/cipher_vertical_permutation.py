import math
from random import randint
from script.const import ABC as alphabet

def vertical_swap_cipher():
    question = str(input("Выполнить действие (шифровать/дефишровать): "))
    proverb = input("Введите пословицу: ").lower()
    key = input("Введите ключ-текст: ").lower()
    result = ''
    if question == "шифровать":
        row_num = math.ceil(len(proverb) / len(key))
        print('Число строк: ', row_num, ', число стобцов: ', len(key))
        if len(proverb) != len(key)*row_num:
            while len(proverb) % len(key) != 0:
                proverb += alphabet[randint(0, len(alphabet) - 1)]
        else:
            print('Добавление букв не требуется')
        print('Сообщение: ', proverb)
        array = []
        count = 1
        substr = ""
        for i in proverb:
            substr += i
            if count % len(key) == 0:
                array.append(substr)
                substr = ""
            count = count+1
        for i in range(len(array)):
            if i % 2 == 1:
                array[i] = array[i][::-1]
        pass_copy = key
        count = 0
        for i in alphabet:
            if i in pass_copy:
                count += 1
                pass_copy = pass_copy.replace(i, str(count) + '.')
        pass_copy = pass_copy.split('.')
        pass_copy.remove('')
        print('Числовое значение ключа: ', pass_copy)
        message_list_res = []
        for i in range(math.ceil(len(proverb)/row_num)):
            message_list_res.append(" ")
        count_pass_copy = 0
        for i in range(len(key)):
            temp = ''
            index_pass = pass_copy[count_pass_copy]
            for item in array:
                temp += item[int(i)]
            message_list_res[int(index_pass)-1] = temp
            count_pass_copy = count_pass_copy + 1
        print('Строки таблицы перестановки: ', array)
        result = ''.join(message_list_res)
        return print('Результат шифрования: ', result)
    if question == "дешифровать":
        row_num = math.ceil(len(proverb) / len(key))
        print('Число строк: ', row_num, ', число стобцов: ', len(key))
        array = []
        count = 1
        substr = ""
        for i in proverb:
            substr += i
            if count % row_num == 0:
                array.append(substr)
                substr = ""
            count = count + 1
        print(array)
        pass_copy = key
        count = 0
        for i in alphabet:
            if i in pass_copy:
                count += 1
                pass_copy = pass_copy.replace(i, str(count) + '.')
        pass_copy = pass_copy.split('.')
        pass_copy.remove('')
        print('Числовое значение ключа: ', pass_copy)

        message_list_res = []
        for i in range(math.ceil(len(proverb) / row_num)):
            message_list_res.append(" ")
        count_pass_copy = 0
        for i in range(len(key)):
            index_pass = pass_copy[count_pass_copy]
            substr_pass = array[int(index_pass)-1]
            message_list_res[ count_pass_copy] = substr_pass
            count_pass_copy = count_pass_copy + 1
        print('Нормальные столбцы: ', message_list_res)
        result_array = []
        for i in range(math.ceil(len(proverb) / len(key))):
            result_array.append("")
        for item in message_list_res:
            count = 0
            for i in item:
                result_array[count] += i
                count += 1
        for i in range(len(result_array)):
            if i % 2 == 1:
                result_array[i] = result_array[i][::-1]
        result = ''.join(result_array)
        return print('Результат шифрования: ', result)


vertical_swap_cipher()