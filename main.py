import math
print(math.e**10)
print(pow(math.log((5+(pow(math.sin(8), 2))), 10), (1/6)))
print('3,55')
print('4,80')
# zadanie 2
a = 'WOJCIECH'
b = 'WIDŹGOWSKI'
a = a.capitalize()
b = b.capitalize()
print(a + ' ' + b)
# zadanie 3
tekstkrasnoludki = 'My jesteśmy krasnoludki, hopsa sa, hopsa sa, pod grzybkami nasze budki, hopsa sa, hopsa sa.'
c = tekstkrasnoludki.count('hopsa sa')
print(c)
# zadanie 4
d = 'łobuziarnia'
print(d[0], d[d.__len__()-1])
# zadanie 6
e = 0x1b6
f = 0.464323
g = 'string to jedyna słuszna zmienna'
print(hex(e), f, g)
h = hex(e), f, g
print(g.split())
listy = ['siatkówka', 'piłka nożna', 'koszykówka', 'rugby', 'hokej', 'jazda konna', 'strzelectwo', 'tenis stołowy']
print(listy)
listy.reverse()
print(listy)
listy.pop(listy.index('piłka nożna'))
listy.pop(listy.index('siatkówka'))
listy.append('siatkówka')
listy.append('piłka nożna')
print(listy)
# zadanie 8
dekalog = {'PZPN': 'Polski Związek Piłki Nożnej', 'PiS': 'Prawo i Sprawiedliwość', 'ZUS': 'Zakład Ubezpieczeń Społecznych'}
i = 'Przedstawiciele PZPN i PiS połączyli siły w starciu z ZUS'
print(dekalog.values())
# zadanie 9
slownik={'Witcher 3': 'RPG', 'Minecraft': 'Sandbox', 'WorldBox': 'Sandbox'}
print(len(slownik)*2)
#zadanie 10
beg=input('wpisz cos plis')
print(beg.count('a'))
# zadanie 11
a=input('podaj a: ')
b=input('podaj b: ')
c=input('podaj c: ')
if(a>b)&(a>c):
    wynik=a
elif(b>a)&(b>c):
    wynik=b
elif(c>a)&(c>b):
    wynik=c
elif(a==b):
    wynik='a i b sa równe i największe'
elif(b==c):
    wynik ='b i c są równe i największe'
elif(a==c):
    wynik='a i c są równe i największe'
elif(a==b)&(b==c):
    wynik='wszystkie są równe'
print(wynik)
#zadanie 12
listy=[1,12,14,15.1241,24,156.214]
x=0
for x in range(0,len(listy)):
    listy[x]=pow(listy[x],2)
    print(listy[x])

#zadanie 13
x=0
listy=[]
for x in range(0,9):
    a=input()
    if((int(a))%2==0):
        listy.append(a)
print(listy)