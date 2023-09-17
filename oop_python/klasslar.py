# class Talaba:
#     """ Talaba nomli klass yaratamiz """
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

# talaba1 = Talaba("Xazratbek","Turdaliyev",2003)

# print(talaba1.ism)

# talaba2 = Talaba("Olim","Olimov",1995)
# talaba3 = Talaba("Husan","Akbarov",2004)
# talaba4 = Talaba("Hasan","Akbarov",2004)

# print(talaba2.ism)

# print(talaba4.familiya)

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

# talaba4 = Talaba("Hasan","Akbarov",2004)
# talaba4.tanishtir()

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism

#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya

#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"

#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_fullname())

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism

#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya

#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"

#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil

#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")


# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_age(2023))

class User:
    def __init__(self,first_name,last_name,uname,email,t_number,adress,born_year):
        self.first_name = first_name
        self.last_name = last_name
        self.uname = uname
        self.mail = email
        self.t_number = t_number
        self.adress = adress
        self.born_year = born_year

    def get_info(self):
        return f"User: {self.first_name.title()} {self.last_name.title()}\nWas born in: {self.born_year}\nAge: {2023-int(self.born_year)}"

    def get_email(self):
        return f"{self.uname.title()}s email is: {self.mail}"

    def get_age(self,year):
        return f"User's age is: {year - int(self.born_year)}"

    def get_phone_number(self):
        return f"{self.uname.title()}'s telephone number is: {self.t_number}"

user_1 = User("Xazratbek","Turdaliyev","xazratbek","xazratbek@gmail.com","+9939999999","Uzbekistan","2003")
print(user_1.get_info())
print(user_1.get_age(2023))
print(user_1.get_email())
print(user_1.get_phone_number())
