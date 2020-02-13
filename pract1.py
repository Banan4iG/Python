#задание 1
print("Hello, World!")
#задание 2
a = None
b = 5
c = 5.5
d = "str"
e = [1,2,3,4]
f = (1,2,3,5)
g = {2:4,3:6}
j = {'1','2', 'str', 2}
print(a, ' - type: ', type(a))
print(b, ' - type: ', type(b), ' float: ', float(b), ' int: ', int(b))
print(c, ' - type: ', type(c), ' str: ', str(c), ' float: ', float(c))
print(d, ' - type: ', type(d), ' size: ', len(d), ' first elem: ', d[1], ' last elem: ', d[len(d)-1], ' mid: ', d[1:len(d)-1])
print(e, ' - type: ', type(e), ' size: ', len(e), ' first elem: ', e[1], ' last elem: ', e[len(e)-1], ' mid: ', d[1:len(e)-1])
print(f, ' - type: ', type(f), ' size: ', len(f), ' first elem: ', f[1], ' last elem: ', f[len(f)-1], ' mid: ', f[1:len(f)-1])
print(g, ' - type: ', type(g), ' size: ', len(g), ' key: ', g[2])
print(j, ' - type: ', type(j), ' size: ', len(j))
#задание 3
t = True
f = False
print(t, ' - type: ', type(t))
print(f, ' - type: ', type(f))
print('and: ', t and f)
print('or: ', t or f)
print('not t: ', not t, ' not f: ', not f)
first = 5
second = 3
print ('ravny?: ',first == second)
print ('not ravny?: ',first != second)
print ('1 > 2?: ', first > second)
print ('1 < 2?: ', first < second)
print ('2 >= 1?: ', second >= first)
print ('2 <= 1?: ', second <= second)
print('+: ', first + second)
print('-: ', first - second)
print('*: ', first * second)
print('/: ', first / second)
print('^: ', first ** second)
print('%: ', first % second)
print('//: ', first // second)
#задание 4
print('Введите число от -100 до 100')
h = int(input())
if h < -100 and h > 100:
    print('Число не входит в диапазон [-100; 100]')
elif h < -50:
    print('Число меньше -50')
elif h == -50:
    print('Число равно -50')
elif h < 0 and h > -50:
    print('Число меньше 0, но больше -50')
elif h > 0 and h < 50:
    print('Число больше 0, но меньше 50')
elif h == 50:
    print('Число равно 50')
elif h > 50:
    print('Число больше 50')
#задание 5
for i in range(0,11):
    print(i, end='\t')
print()
i = 0
while i < 11:
    print(i, end='\t')
    i = i+1
print()
MyFIO = "Кашин Никита Павлович"
for i in MyFIO:
    print(i)
MyFriends = ["Елизавета", "Артем", "Ксения", "Даниил"]
for i in MyFriends:
    print(i)
MyFriendsDict = {'Елизавета':'10.12.2000', 'Артем':'08.12.2000', 'Ксения':'16.11.2000', 'Даниил':'22.12.2000'}
for k in MyFriendsDict:
    if MyFriendsDict[k][3:5]== '06' or MyFriendsDict[k][3:5]== '07' or MyFriendsDict[k][3:5]== '08' or MyFriendsDict[k][3:5]== '12' or MyFriendsDict[k][3:5]== '01' or MyFriendsDict[k][3:5]== '02':
        print(k, MyFriendsDict[k])
#задание 6
def Func():
    print("Hello, World!")
Func()
def FuncName(name):
    print(name)
FuncName("Nikita")
def FuncYr(a, b, c):
    d = b**2 - 4*a*c
    return d
a = 1
b = 5
c = 10
print(FuncYr(a, b, c))
def FuncAsk():
    print("Введите ваше имя:")
    name = input()
    print("Введите ваш возраст: ")
    old = int(input())
FuncAsk()
def FuncAlf(b):
    if b>=1 and b<=33:
        print(chr(b+1071))
    elif b>33:
        print("Указано неправильное число")
FuncAlf(int(input()))
#задание 7
name = "Кашин Никита Павлович"
print('Len: ', len(name))
print(name + name)
print('Name: ', name[6:12])
print(name.upper())
print(name.split())
#задание 8
l = [None, 5, 5.5, 'Nikita', [1,2,3], (1,3,5), {2:4, 4:6}, {2,4,6}]
for n, i in enumerate(l):
    print(n, type(i), end = '\t')
l.pop()
name=list(l[3])
print(name)
st=''
print(st.join(name))
for n, i in enumerate(st.join(name)):
    print(n, ' - ', i)
count = 0
for i in name:
    if i=='a':
        count += 1
        print(count)
#задание 9
l1 = []
for i in range(1,100):
    if i % 2 != 0:
        l1.append(i)
print(l1)
#задание 10
def delen(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(r)
delen(int(input()),int(input()))






























