import unittest

class Car:
    """(self,make,model,year,km=0,price=None)"""
    def __init__(self,make,model,year,km=0,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km

    def set_price(self,price):
        self.price = price

    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")

    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}, "
        info += f"{self.year}-yil, {self.__km}km yurgan."
        if self.price:
            info += f" Narhi: {self.price}"
        return info

    def get_km(self):
        return self.__km


class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""

    def setUp(self):
        make = "GM"
        self.model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make, self.model, year)
        self.avto2 = Car(make, self.model, year, price=self.price)

    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model, self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEqual(0, self.avto1.get_km())
        # avto2 narhini tekshiramiz
        self.assertEqual(self.price, self.avto2.price)

    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)

    def test_add_km(self):
        # 1 Musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(15000, self.avto1.get_km())
        # 2 Manfiy qiymat berib ko'ramiz
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

    def test_get_info(self):
        avto1_info = "GM Malibu, 2020-yil, 0km yurgan."
        self.assertEqual(avto1_info, self.avto1.get_info())
        # avto1 narhi va km o'zgartiramiz
        self.avto1.set_price(50000)
        self.avto1.add_km(20000)
        avto1_info = "GM Malibu, 2020-yil, 20000km yurgan. Narhi: 50000"
        self.assertEqual(avto1_info, self.avto1.get_info())


# Amaliyot

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
    def __init__(self, ism, familiya, passport, tyil, idraqam):
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

    def remove_fan(self, fan_nomi):
        if fan_nomi not in self.fanlar:
            return None  # Return None when the fan is not found
        else:
            self.fanlar.remove(fan_nomi)

    def fanga_yozil(self, fan_nomi):
        if fan_nomi not in self.fanlar:
            fan = Fan(fan_nomi)  # Create a Fan instance
            self.fanlar.append(fan)
        else:
            return "Siz allaqachon usbu fanga yozilgansiz"

    def get_fanlar(self):
        return [fan.get_fan_nomi() for fan in self.fanlar]

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

class TestShaxs(unittest.TestCase):
    def setUp(self):
        self.inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)

    def test_get_info(self):
        self.assertEqual(self.inson.get_info(), "Hasan Alimov. Passport:FB001122, 1995-yilda tug`ilgan")

    def test_get_age(self):
        self.assertEqual(self.inson.get_age(2021), 26)

class TestTalaba(unittest.TestCase):
    def setUp(self):
        self.talaba = Talaba("John", "Doe", "AB123456", 2000, "12345")

    def test_get_id(self):
        self.assertEqual(self.talaba.get_id(), "12345")

    def test_get_bosqich(self):
        self.assertEqual(self.talaba.get_bosqich(), 1)

    def test_remove_fan(self):
        self.talaba.fanga_yozil("Math")
        self.assertEqual(self.talaba.remove_fan("Math"), None)

    def test_fanga_yozil(self):
        self.assertEqual(self.talaba.fanga_yozil("Math"), None)

    def test_get_fanlar(self):
        self.talaba.fanga_yozil("Math")
        self.assertEqual(self.talaba.get_fanlar(), ["Math"])

class TestFan(unittest.TestCase):
    def setUp(self):
        self.fan = Fan("Math")

    def test_get_fan_nomi(self):
        self.assertEqual(self.fan.get_fan_nomi(), "Math")

    def test_add_talaba(self):
        talaba = Shaxs("Alice", "Johnson", "CD789012", 2002)
        self.fan.add_talaba(talaba)
        self.assertEqual(self.fan.get_talabalar(), ["Alice Johnson. Passport:CD789012, 2002-yilda tug`ilgan"])


if __name__ == '__main__':
    unittest.main()