alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
text = ('цепьнекрепчесвоегосамогослабогозвенатчк')
# text = ('когданеумеютписатьзптговорятзптчтопероплохоетчк')
print(len(text))

if len(text) % 2 != 0:
    text = text + 'ф'
print(text)
print(len(text))

text1 = ''
text2 = ''
for element in range(len(text)//2):
    text1 = text1 + text[element]
    text2 = text2 + text[element+len(text)//2]

print(text1)
print(text2)

text1_to_index = ''
text2_to_index = ''

for i in range(len(text)//2):
    symb1 = text1[i]
    symb2 = text2[i]
    index_symb1 = alphabet.index(symb1)
    index_symb2 = alphabet.index(symb2)
    text1_to_index = text1_to_index + str(index_symb1 + 1) + ','
    text2_to_index = text2_to_index + str(index_symb2 + 1) + ','

text1_to_index = text1_to_index[:-1].split(',')
text2_to_index = text2_to_index[:-1].split(',')

for i in range(len(text1_to_index)):
    text1_to_index[i] = int(text1_to_index[i])
for i in range(len(text2_to_index)):
    text2_to_index[i] = int(text2_to_index[i])

# print(text1_to_index)
# print(text2_to_index)
print()

def func(l, k):
    # Функция сложения по модулю 2^32
    f = (l + k) % 32
    print(f)
    # f = bin((l + k) % 32)[2:]
    # print("0"*(32-len(f)) + f)
    return f

n = 1
for i in range((len(text)//2) - 1):
    print(n)
    text2_to_index[i+1] = text1_to_index[i]
    text1_to_index[i+1] = (int(text2_to_index[i]
                              ) ^ func(int(text1_to_index[i]), n)) % 32
    n = (n + 1) % 9
    if n == 0:
        n = 1

print(text1_to_index, '\n', text2_to_index, '\n', n)

result = text1_to_index + text2_to_index
print(result)

code = ''
for j in range(len(result)):
    code = code + str(alphabet[result[j]])

print(code)

#Расшифровка
# decode = ''
# code1 = ''
# code2 = ''
# for element in range(len(code)//2):
#     code1 = code1 + code[element]
#     code2 = code2 + code[element+len(code)//2]

# print(code1)
# print(code2)

# code1_to_index = ''
# code2_to_index = ''

# for i in range(len(code)//2):
#     symb1 = code1[i]
#     symb2 = code2[i]
#     index_symb1 = alphabet.index(symb1)
#     index_symb2 = alphabet.index(symb2)
#     code1_to_index = code1_to_index + str(index_symb1) + ','
#     code2_to_index = code2_to_index + str(index_symb2) + ','

# code1_to_index = code1_to_index[:-1].split(',')
# code2_to_index = code2_to_index[:-1].split(',')

# for i in range(len(code1_to_index)):
#     code1_to_index[i] = int(code1_to_index[i])
# for i in range(len(code2_to_index)):
#     code2_to_index[i] = int(code2_to_index[i])

# n = 8
# for i in range((len(text)//2) - 1):
#     print(n)
#     code2_to_index[i+1] = code1_to_index[i]
#     code1_to_index[i+1] = int(code2_to_index[i]
#                               ) ^ func(int(code1_to_index[i]), n) % 32
#     n = (n - 1) % 9
#     if n == 0:
#         n = 8

# result = code1_to_index + code2_to_index
# print(result)

# for j in range(len(result)):
#     decode = decode + str(alphabet[result[j]])

# print(decode)