shahar = "Қўқон"
viloyat = 'Фарғона'

matn = "Men yangi 📱 oldim"
print(matn)

ism = 'Ahmad'
print("Mening ismim " + ism)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')


ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())

ism_sharif = 'james bond'
print(ism_sharif.title())

ism_sharif = 'james bond'
print(ism_sharif.capitalize())

print('james bond'.upper())


meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")

ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, " + ism.title())


"""
AMALIYOT
Quyidagi mashqlarni bajaring:
Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
"""

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"

print(f"{kocha} ko'chasi,\n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati")


kocha = input("Ko'cha nomini kiriting kiriting: ")
mahalla = input("Mahalla nomini kiriting: ")
tuman = input("Tuman nomini kiriting: ")
viloyat = input("Viloyat nomini kiriting: ")

print(f"Siz kiritgan to'liq matn: {kocha} ko'chasi,\n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati")


adress = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(adress)

print(adress.upper())
print(adress.lower())
print(adress.title())
print(adress.capitalize())