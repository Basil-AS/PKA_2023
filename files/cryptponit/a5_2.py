alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# text = input("Введите исходный текст: ")
text = 'цепьнекрепчесвоегосамогослабогозвенатчк'

text_to_num = []
text_to_num_binary = []
for i in range(len(text)):
    text_to_num.append(alphabet.index(text[i]) + 1)
    text_to_num_binary.append(bin(alphabet.index(text[i]) + 1)[2:])
# print(text_to_num)
# print(text_to_num_binary)

for i in range (len(text_to_num_binary)):
    if len(text_to_num_binary[i]) != 6:
        text_to_num_binary[i] = '0'*(6 - len(text_to_num_binary[i])) + text_to_num_binary[i]
# print(text_to_num_binary)

session_key = ['1100', '1001', '1011', '0100', '0101', '1111', '1010', '1001', '1010', '1010', '0101', '1010', '1111', '0101', '1011', '0101']

R1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
R2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
R3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
R4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(len(R4))
gamma = []

counter = 0
for i in range(len(session_key)):
    for j in range(len(session_key[i])):
        key = session_key[i][j]
        
        # counter += 1
        # print(counter, key)
        
        R1_xor_result = int(key) ^ (R1[13] ^ R1[16] ^ R1[17] ^ R1[18])
        R1.insert(0, R1_xor_result)
        R1.pop(-1)
        
        R2_xor_result = int(key) ^ (R2[20] ^ R2[21])
        R2.insert(0, R2_xor_result)
        R2.pop(-1)
        
        R3_xor_result = int(key) ^ (R3[7] ^ R3[20] ^ R3[21] ^ R3[22])
        R3.insert(0, R3_xor_result)
        R3.pop(-1)
        
        # F = (R1[8] and R2[10]) or (R1[8] and R3[10]) or (R2[10] and R3[10])
        # print(F)
        # gamma.append(R1[18] ^ R2[21] ^ R3[22])
print('R1:', R1)
print('R2:', R2)
print('R3:', R3)
# print('gamma:', gamma)

result = ''
result_xor = ''
xor_gamma = []
for i in range (len(text_to_num_binary)):
    for j in range (len(text_to_num_binary[i])):
        F = (R1[8] and R2[10]) or (R1[8] and R3[10]) or (R2[10] and R3[10])
        xor_gamma.append(R1[-1] ^ R2[-1] ^ R3[-1])

        if R1[8] == F:
            R1.insert(0, R1[-1])
            R1.pop(-1)

        if R2[10] == F:
            R2.insert(0, R2[-1])
            R2.pop(-1)

        if R3[10] == F:
            R3.insert(0, R3[-1])
            R3.pop(-1)
            
    xor_gamma = ''.join(str(xor_gamma).replace(', ', '').strip('[]'))
    
    for k in range (len(text_to_num_binary[i])):
        result_xor = result_xor + str((int(text_to_num_binary[i][k])) ^ int(xor_gamma[k]))
    print('Исходный текст в 2-ичной:', text_to_num_binary[i], 'Гамма:', xor_gamma, 'Результат XOR:', result_xor, '\n')
    
    result = result + alphabet[int(result_xor, 2) % 32]
    result_xor = ''
    xor_gamma = []
print('Результат шифрования:', result)

