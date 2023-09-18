from math import pi

with open("pi.txt",'w') as file:
    file.write(f"{pi}")

with open('pi.txt', 'r') as file:
    PI = file.read()
    print(PI)

faylnomi = 'ustozlar.txt'# ochilayotgan (yaratilayotgan) fayl nomi
with open(faylnomi,'w') as fayl:
    fayl.write('anvar narzullaev') # faylga yozilayotgan ma'lumot


faylnomi = 'new_file.txt'
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')

with open(faylnomi,'a') as fayl:
    fayl.write('Alijon Valiyev\n')
    fayl.write('2000')

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)

print(talaba2)

#Amaliyot

import pickle

with open('pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = pi.replace(' ','')

# Tug'ilgan kunim pi da bormi?
bdate = '31122000'
print(bdate in pi)

pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz

with open('pi_float.dat','wb') as file:
    pickle.dump(pi,file)

while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('books.txt','a') as file:
        file.write(book+'\n')