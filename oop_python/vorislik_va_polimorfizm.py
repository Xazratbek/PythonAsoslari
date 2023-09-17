class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

inson = Shaxs("Hasan","Alimov","FB001122",1995)
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def remove_fan(self,fan_nomi):
        if fan_nomi not in self.fanlar:
            return "Siz ushbu fanga yozilmagansiz"

        else:
            self.fanlar.remove(fan_nomi)

    def fanga_yozil(self,fan_nomi):
        if fan_nomi not in self.fanlar:
            self.fanlar.append(fan_nomi)

        else:
            return "Siz allaqachon usbu fanga yozilgansiz"

    def get_fanlar(self):
        return [fan_nomi.get_fan_nomi() for fan_nomi in self.fanlar]

class Fan:
    def __init__(self,fan_nomi):
        self.fan_nomi = fan_nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def get_fan_nomi(self):
        return self.fan_nomi

    def add_talaba(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_talabalar(self):
        return [talaba.get_info() for talaba in self.talabalar]

talaba_1 = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
fan = Fan("Fizika")
fan_2 = Fan("Matematika")
fan_3 = Fan("Adabiyot")
fan.add_talaba(talaba_1)
fan.add_talaba(inson)
fan_3.add_talaba(inson)
talaba_1.fanga_yozil(fan_2)
print(talaba_1.get_fanlar())

# print(fan.get_talabalar())
# print(fan_3.get_talabalar())
# print(talaba.get_info())

# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")

# print(f"{talaba.get_bosqich()}-bosqich talabasi")
