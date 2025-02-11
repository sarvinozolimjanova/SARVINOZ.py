""" Vorislik """

class Shahs(): # Ota class
    """ """

    def __init__(self, ism:str, familiya:str, otchestvo:str, t_yil:int, passport:str, millat:str):
        self.ism = ism
        self.familiya = familiya
        self.otchestvo = otchestvo
        self.t_yil = t_yil
        self.passport = passport
        self.millat = millat
        
    def __str__(self):
        """"""
        return f"{self.ism} {self.familiya} {self.otchestvo}"

    def get_info(self):
        """ Shahs haqida to'liq ma'lumot beruvchi funksiya """
        return f"{self.familiya} {self.ism} {self.otchestvo} {self.t_yil}-yilda tug'ilgan. Millati: {self.millat}. Passport raqami: {self.passport}"

    def get_age(self, h_yil):
        """ Shahsning yoshini qaytaruvchi funksiya """
        return h_yil-self.t_yil

    def get_passport(self):
        """ shahsning passport ma'lumotini qaytaruvchi funksiya """
        return self.passport

    def get_millat(self):
        """ Shahsning millatini qaytaruvchi funksiya """
        return self.millat

shahs1 = Shahs("Sarvinoz", "Olimjonova", "Shuhratovna", 2009, "AC1234555", "O'zbek")
# print(shahs1)
# print(shahs1.get_info())
# print(shahs1.get_age(2025))


class Student(Shahs): # Voris class
    """ O'quvchi haqidagi klass """

    def __init__(self, ism:str, familiya:str, otchestvo:str, t_yil:int, passport:str, millat:str, maktab:str, sinf:int, baholar:list):
        super().__init__(ism, familiya, otchestvo, t_yil, passport, millat)
        self.maktab = maktab
        self.sinf = sinf
        self.baholar = baholar

    def get_maktab(self):
        """ O'quvchining maktabini qaytaruvchi funksiya """
        return self.maktab

    def change_school(self, new_school):
        """ Maktabni o'zgartiradigan funksiya """
        self.maktab = new_school
        return new_school


    def get_sinf(self):
        """ O'quvchining sinfini qaytaradigan funksiya """
        return self.sinf

    def set_sinf(self):
        """ Sinfni o'zgartiradigan funksiya  """
        if self.sinf <= 11:
            self.sinf += 1
            return self.sinf
        else: 
            return f"Siz bitiruvchi sinfsiz !!!"

    def get_baholar(self):
        """ Umumiy ballini qaytaruvchi """
        return self.baholar

    def get_age(self, h_yil):
        """ O'quvchining yoshini chiqarib beruvchi funksiya """
        return f"{self.ism} {h_yil-self.t_yil} yoshda"

    def get_millat(self):
        """ P'quvchining millatini chiqarb beruvchi funksiya """
        return f"{self.ism}ning millati: {self.millat}"


student1 = Student("Naima", "Malikova", "Murodovna", 2009, "AD1234555", "O'zbek", "Boborahim mashrab", 9, [3, 4, 5, 4])

# print(student1.get_age(2025))
# print(student1.get_info())
# print(student1.get_passport())
# print(student1.get_millat())
# print(student1.get_maktab())
# print(student1.get_sinf())
# print(student1.get_baholar())
# print(student1.set_sinf())
# print(student1.change_school("34-maktab"))


""" mashq """
class Texnika():
    """ Umumiy texnika haqida klass """
    def __init__(self, brend:str, model:str, yil:int, narh:int, rang:str):
        self.brend = brend
        self.model = model
        self.yil = yil
        self.narh = narh
        self.rang = rang

    def get_brend(self):
        """ """
        return f"Texnika brendi: {self.brend}"

    def get_model(self):
        """ """
        return f"Texnika modeli: {self.model}"

    def get_yil(self):
        """ """
        return f"Texnika ishlab chiqarlgan sana: {self.yil}"

    def get_narh(self):
        """ """
        return f"Texnika narhi: {self.narh} $"

    def get_rang(self):
        """ """
        return f"Texnika rangi: {self.rang}"


texnika1 = Texnika("Apple", "13", "idk", 1500, "dark blue")
print(texnika1.get_brend())

class Telefon(Texnika):
    """ Telefon haqida """
    def __init__(self, brend:str, model:str, yil:int, narh:int, rang:str, kamera:str, xotira:str):
        super().__init__(brend, model, yil, narh, rang)
        self.kamera = kamera
        self.xotira = xotira

    def get_kamera(self):
        """ """
        return f"Telefon xotirasi: {self.kamera}"

    def get_xotira(self):
        """ """
        return f"Telefon hotirasi: {self.xotira}"

    def get_brend(self):
        """ """
        return f"Telefon brendi: {self.brend}"

    def get_model(self):
        """ """
        return f"Telefon modeli: {self.model}"

    def get_yil(self):
        """ """
        return f"Telefon ishlab chiqarlgan sana: {self.yil}"

    def get_narh(self):
        """ """
        return f"Telefon narhi: {self.narh} $"

    def get_rang(self):
        """ """
        return f"Telefon rangi: {self.rang}"

phone1 = Telefon("Apple", "13", 2000, 111111, 'drak blue', '11pxl', '256gb')
print(phone1.get_brend())


class Noutbuk(Texnika):
    """ Noutbuk haqida """
    def __init__(self, brend:str, model:str, yil:int, narh:int, rang:str, xotira:str, kamera:str):
        super().__init__(brend, model, yil, narh, rang)
        self.kamera = kamera
        self.xotira = xotira

    def get_kamera(self):
        """ """
        return f"Noutbuk xotirasi: {self.kamera}"

    def get_xotira(self):
        """ """
        return f"Noutbuk hotirasi: {self.xotira}"

    def get_brend(self):
        """ """
        return f"Noutbuk brendi: {self.brend}"

    def get_model(self):
        """ """
        return f"Noutbuk modeli: {self.model}"

    def get_yil(self):
        """ """
        return f"Noutbuk ishlab chiqarlgan sana: {self.yil}"

    def get_narh(self):
        """ """
        return f"Noutbuk narhi: {self.narh} $"

    def get_rang(self):
        """ """
        return f"Noutbuk rangi: {self.rang}"

noutbuk1 = Noutbuk("hp", "windows", 2000, 1200, 'grey', 'nechdur terrabayt', '10px')
print(noutbuk1.get_brend())