import datetime as dt

hozir = dt.datetime.now()
print(hozir)

# sanani ajratib olish
print(hozir.date())

# vaqtni ajratib olish
print(hozir.time())

# soatni ajratib olish
print(hozir.hour)

# minutni ajratib olish
print(hozir.minute)

# sekundni ajratib olish
print(hozir.second)

bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")

ertaga = dt.date(2023, 6, 21)
print(f"Ertangi sana: {ertaga}")

hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")

vaqtKeyin = dt.time(23,45,00)

bugun = dt.date.today()
qurbonHayit = dt.date(2023, 7, 19)
farq = qurbonHayit-bugun
print(farq)
print(f"Qurbon Hayitiga {farq.days} kun qoldi")

hozir = dt.datetime.now()
futbol = dt.datetime(2023, 6, 22, 23, 45, 00)
farq= futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")

# vaqtni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")

# sanani kun-oy-yil koʻrinishida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")

# sanani kun/oy/yil koʻrinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)

import math
PI = math.pi
print(f"PI ning qiymati: {PI}")

E = math.e
print(f"e ning qiymati: {E}")

math.sin(math.pi/2)

math.cos(0)

math.tan(PI)

math.degrees(math.pi/2)

math.radians(90)

# natural logarifm
math.log(5)

# 10 asosli logarifm
math.log10(100)

x = 4.6
print(math.ceil(x))

print(math.floor(x))

x = 81

# Kvadrat ildiz
math.sqrt(x)

x = 81

# Kvadrat ildiz
math.sqrt(x)

math.pow(x,5) # x ning 5-darajasi

math.pow(x,1/3) # x dan kub ildiz

from pprint import pprint
import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)

print(bemor)

{'ism': 'Alijon Valiyev', 'yosh': 30, 'oila': True, 'farzandlar': ['Ahmad', 'Bonu'], 'allergiya': None, 'dorilar': [{'nomi': 'Analgin', 'miqdori': 0.5}, {'nomi': 'Panadol', 'miqdori': 1.2}]}

pprint(bemor)

{'allergiya': None,
 'dorilar': [{'miqdori': 0.5, 'nomi': 'Analgin'},
             {'miqdori': 1.2, 'nomi': 'Panadol'}],
 'farzandlar': ['Ahmad', 'Bonu'],
 'ism': 'Alijon Valiyev',
 'oila': True,
 'yosh': 30}

import re

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р"

print(re.match(andoza, word1))

print(re.match(andoza, word2))

print(re.match(andoza, word3))

from uzwords import words
andoza = "^т...р$"

matches = []
for word in words:
    if re.match(andoza,word):
        matches.append(word)
print(matches) # ['табар', 'табор', 'тавир', 'тайёр', 'татар', 'татир', 'тахир', 'тақир', 'театр', 'тембр', 'темир', 'темур', 'тенор', 'тикер', 'тихир', 'товар', 'товор', 'тожир', 'томир', 'тонер', 'тоҳир', 'триер', 'тумор', 'тўпар', 'тўпир']