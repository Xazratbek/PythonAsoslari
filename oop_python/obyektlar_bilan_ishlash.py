class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

talaba1 = Talaba("Xazratbek","Turdaliyev",2003)
print(talaba1.get_info())

talaba1.bosqich= 2
print(talaba1.bosqich)

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

talaba1 = Talaba("Xazratbek","Turdaliyev",2003)
talaba1.set_bosqich(3)
print(talaba1.get_info())

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Xazratbek","Turdaliyev",2003)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talabalar_soni)

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]

matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Xazratbek","Turdaliyev",2003)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

mat_talabalar = matematika.get_students()
print(mat_talabalar)


class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil


class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [x.get_info() for x in self.talabalar]

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni

print(dir(Talaba))

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))

print(see_methods(talaba1))

print(talaba1.__dict__)

print(talaba1.__dict__.keys())

# Amaliyot

class Avtosalon:
    def __init__(self,salon_nomi,salon_manzili):
        self.salon_nomi = salon_nomi
        self.salondagi_mashinalar_soni = 0
        self.salon_manzili = salon_manzili
        self.salondagi_mashinalar = []
        self.sotilgan_mashinalar = []
        self.sotilgan_mashinalar_soni = 0

    def get_salon_nomi(self):
        return self.salon_nomi

    def get_salondagi_mashinalar(self):
        return [mashina.get_info() for mashina in self.salondagi_mashinalar]

    def get_info(self):
        return f"Salon nomi: {self.salon_nomi}\nMavjud mashinalar soni: {self.salondagi_mashinalar_soni}\n"

    def add_to_sotilgan_mashinalar(self,sotilgan_mashina):
        self.sotilgan_mashinalar.append(sotilgan_mashina)
        self.sotilgan_mashinalar_soni += 1

    def add_mashina(self,mashina):
        self.salondagi_mashinalar.append(mashina)
        self.salondagi_mashinalar_soni += 1

    def remove_sotuvdagi_mashinalar(self,mashina):
        self.sotuvdagi_mashinalar.remove(mashina)

    def get_sotilgan_mashinalar(self):
        return [mashina.get_info() for mashina in self.sotilgan_mashinalar]

    def get_sotilgan_mashinalar_soni(self):
        return self.sotilgan_mashinalar_soni

    def get_salon_manzil(self):
        return self.salon_manzili

    def remove_salondagi_mashinalar(self,mashina):
        self.salondagi_mashinalar.remove(mashina)

class Avto:
    def __init__(self,model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.km = 0


    def get_car_model(self):
        return self.model

    def get_car_rang(self):
        return self.rang

    def get_info(self):
        return f"Car model: {self.model}\nColor: {self.rang}\nCar price: {self.narh}"

    def update_km(self,km):
        self.km += km

    def get_km(self):
        return self.km

avto_1 = Avto("Malibu","Qora","Avtomat",45000)
avto_2 = Avto("Gentra","Oq","Mehanika",12000)
avto_3 = Avto("Matiz","Oq","Mehanika",3400)
avto_4 = Avto("Nexia 3","Oq","Avtomat",9000)
avto_1.update_km(1500)
avto_4.update_km(1500)
avto_1.get_km()
print(avto_1.get_car_model())
print(avto_1.get_info())

avtosalon = Avtosalon("One way","Tashkent uzbekistan")
avtosalon.add_mashina(avto_1)
avtosalon.add_mashina(avto_2)
avtosalon.add_mashina(avto_3)
avtosalon.add_mashina(avto_4)
avtosalon.add_to_sotilgan_mashinalar(avto_1)
print(avtosalon.get_sotilgan_mashinalar())
print(avtosalon.get_sotilgan_mashinalar_soni())
print(avtosalon.get_salondagi_mashinalar())

print(dir(Avto))
print(dir(Avtosalon))
