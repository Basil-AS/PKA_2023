#n простое, а любое

#101, 7
#8, 10


#211, 10
#23, 7

def input1():
    N1 = int(input('Введите параметр N для первого пользователя: '))
    A1 = int(input('Введите параметр A для первого пользователя: '))
    K1 = int(input('Введите параметр K для первого пользователя: '))
    N2 = int(input('Введите параметр N для второго пользователя: '))
    A2 = int(input('Введите параметр A для второго пользователя: '))
    K2 = int(input('Введите параметр K для второго пользователя: '))
    if (not A1 > N1 or A2 > N2  ):
        if N1 == N2:
            if A1 == A2:
                Y1 = (A1**K1)%N1

                Y2 = A2**K2%N2
            else: 
                print ('Парематр А не совпадает! Введите одинаковые параметры')
                A1 = int(input('Введите параметр A: '))
                A2 = int(input('Введите параметр A: '))
        else:   
            print ('Парематр N не совпадает! Введите одинаковые параметры')
            N1 = int(input('Введите параметр N: '))
            N2 = int(input('Введите параметр N: '))   
            if A1 == A2:
                Y1 = (A1**K1)%N1
                Y2 = A2**K2%N2

            else: 
                print ('Парематр А не совпадает! Введите одинаковые параметры')
                A1 = int(input('Введите параметр A: '))
                A2 = int(input('Введите параметр A: '))  
        return N1,A1,K1,K2,Y1,Y2
    else: 
        print('введите верные N и A')
    
def dfplayer2(N,A,Y1,K):
    Y2 = A**K%N
    K = Y1**K%N
    return Y2,K
    
def dfplayer1key(Y2,KU2,N,K1):
    KU1 = Y2**K1%N
    print("Секретный ключ первого пользователя",KU1)
    print("Секретный ключ второго пользователя",KU2)
    if KU2 == 1 or K1 == 1:
        print('Секретный ключ равен 1. Введите данные повторно')
        input1()
    else:
        if KU1 == KU2:
            print("Ключи одинаковые")
        else:
            print("Ключи не совпали")

params = input1() 
print('Общий парамет N = ', params[0])
print('Общий парамет A = ', params[1]) 
print("Открытый ключ первого пользователя:",params[4])
print("Открытый ключ второго пользователя:",params[5])
prog = dfplayer2(params[0],params[1],params[4],params[3])
result = dfplayer1key(prog[0],prog[1],params[0], params[2])

input()