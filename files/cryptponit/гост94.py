# Функция хеширования
def hash(phr):
    h=[0]
    index=1
    p=33
    for i in phr:
        t=((h[index-1]+alphabet.index(i)+1)**2) % p
        h.append(t)
        index+=1
    print('h=', h, '\n')
    return(h)

# Проверка подписи
def check(phr, r, s, q):
    v=(hash(phr)[-1]**(q-2)) % q
    print('v:',v)
    z1=(s*v) % q
    print('z:',z1)
    z2=((q-r)*v) % q
    print('z2:',z2)
    u=((a**z1 * y**z2) % p) % q
    print('u:',u)
    return u==r

# Проверка на число
def isInt(string):
    try:
        int(string)
        return True
    except:
        return False

# Проверка параметра, является он числом или нет, если нет, то просит повторить ввод
def user_input(param):
    someIn = input(f'Введите {param}: ')
    while (not isInt(someIn)):
        someIn = input(f'Введите число {param}: ')
    return int(someIn)

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
# phr = list('ЦЕПЬНЕКРЕПЧЕСВОЕГОСАМОГОСЛАБОГОЗВЕНАТЧК')
phr = list('КОГДАНЕУМЕЮТПИСАТЬЗПТГОВОРЯТЗПТЧТОПЕРОПЛОХОЕТЧК')

p=user_input('p')
q=user_input('q') #(p-1)%q=0
while (p-1)%q!=0:
    q=user_input(f'q, что {p-1}%q=0')
a=user_input('a') #a>1; <(p-1); a**q%p==1
while a<=1 or a>=(p-1) or a**q%p!=1:
    a=user_input(f'a, что 1< a <({p-1}); a**{q}%{p}==1')

#if not (a**q % p==1):
#    print("a**q % p!=1")
#    while not (a**q % p==1):
#        a+=1
#    print(a)
#    exit(0)
x=user_input('x')
y=a**x % p
print('y:',y)

k=user_input('k')  #k<q
while k>=q:
    k=user_input(f'k меньше {q}')
r=(a**k % p) % q
print('r:',r)
if r==0:
    print("r=0")
    exit(0)
h = hash(phr)[-1]
if h % q==0:
    h=1
s=(x*r+k*h) % q
print('s:',s)
print('Подпись:',(r%(2**256), s%(2**256)))
if check(phr, r%(2**256), s%(2**256), q):
    print('Подпись прошла')

'''
р - большое простое число длиной от 509 до 512 бит либо от 1020 до 1024 бит;
q - простой сомножитель числа (р-1), имеющий длину 254...256 бит; 
а - любое число, большее 1 и меньшее (р-1), причем такое, что а^q mod p = 1;
--------------------------------  р, q и а являются открытыми
х - некоторое число, меньшее q;
у = а^x mod р ---> тоже открытый ключ
-------
p = 47
q = 23
a = 3
х = 15
y = 42
'''