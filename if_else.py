avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ...
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ...
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.


ism = 'Ali'
ism.lower() == 'ali'
ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")

javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')


login = input("Yangi login tanlang:")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart!")

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")


yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")

# Amaliyot

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car!='gm':
    print(car.title())
  else:
    print(car.upper())

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz {login.title()}!")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")


#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')