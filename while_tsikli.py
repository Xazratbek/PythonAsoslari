son = 1 # son ga 1 qiymatini beramiz
while son<=5: # toki son 5 dan kichik yoki teng ekan...
    print(son, end=' ') # son ni konsolga chiqaramiz,
    son = son+1 # songa 1 qo'shamiz.

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)


print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsiklni to'xtatish
    else:
        print(float(qiymat)**2)


sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")

son = 0
while son<10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)

# infinite loop
son = 0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son)

son = 1
while son>0:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)

# Amaliyot
stop = True
kitoblar = []
while stop:
    kitob = input("Yaxshi ko'rgan kitobingiz nomini kiriting( dasturni to'xtatish uchun stop so'zini kiriting ): ")
    if kitob.lower() == 'stop':
        break
    else:
        kitoblar.append(kitob)
print(f"Siz yoqtirgan kitoblar: {kitoblar}")

stop = True
while stop:
    yosh = input("Chipta narxini bilish uchun yoshingizni kiriting: ")
    if (yosh.lower() == 'exit' or yosh.lower() == 'quit'):
        stop = False
        break

    if not yosh.isdigit():
        print("Iltimos yoshingizni raqamlar orqali kiriting: ")
        continue

    elif int(yosh) < 7:
        print("Siz uchun bilet narxi 2000-so'm")

    elif int(yosh) < 18 and int(yosh) >= 7:
        print("Siz uchun bilet narxi 3000-so'm")

    elif int(yosh) >= 18 and int(yosh) < 65:
        print("Siz uchun bilet narxi 10000-so'm")

    elif int(yosh) >= 65:
        print("Siz uchun bilet bepul")

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")