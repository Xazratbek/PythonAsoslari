import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

product = lambda x, y : x ** y
print(product(3, 2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

sonlar = list(range(11))
from math import sqrt
ildizlar = list(map(sqrt,sonlar))

# Sonlar ro'yxatidagi har bir sonni ikkilik sanoq sistema (binar) shaklida ifodalash

numbers = [10, 20, 30, 40, 50]
binary_representations = list(map(lambda x: bin(x), numbers))
print(binary_representations)

# Matn ro'yxatidagi har bir matnning uzunligini topish

words = ["Salom", "Python", "Dunyo"]
lengths = list(map(lambda x: len(x), words))
print(lengths)

# Sonlar ro'yxatidagi juft sonlarni aniqlash
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz

kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda matn:matn.upper(),ismlar)))

import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)

import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)


filtr = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar)) # Ushbu mevalar ro'yxatidagi bosh harfi a bilan boshlanadigan va r harfi bilan tugaydigan mevalar nomini listga yig'ib oladi

print(filtr)