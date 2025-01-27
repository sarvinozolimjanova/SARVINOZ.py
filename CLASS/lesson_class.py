""" Class """
""" OOP - Object oriented programming """

class Car():
    """ docstring """

    def __init__(self, company:str, model:str, color:str, price:int, max_speed:int, year:int): # parametr
        self.company = company     # hususiyat
        self.model = model
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.year = year

    def get_info(self):
        """ The function which is about cars """

        info = f"Information about the car: \nCompany: {self.company} \nModel: {self.model} \nColor: {self.color} \
        \nPrice: {self.price} $  \nMaximum speed: {self.max_speed} \nYear: {self.year} \n"

        return info

car1 = Car("BMW", "m8", "black", 300_000, 450, 2012)
car2 = Car("Mercedes-Benz", 'cls63', 'black', 300_000, 300, 2020)
car3 = Car('Bentley', "i don't know", 'white', 500_000, 300, 2009)

# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())




# git config --global user.name "Your Name"
# git config --global user.email "youremail@domain.com"


""" 1 - mashq """
class Student():
    """ The class for students """
    
    def __init__(self, name:str, surname:str, year:int, kurs:int, marks:list, friends:list):
        self.name = name
        self.surname = surname
        self.kurs = kurs
        self.marks = marks
        self.year = year
        self.friends = friends

    def get_info(self):
        """  about student """
        return f"Student {self.name} {self.surname} {self.kurs}-kurs studenti."
    
    def get_middle_ball(self):
        """ Student's ball """
        return sum(self.marks)/len(self.marks)
    
    def get_full_name(self):
        """ Student's full name """
        return f"{self.name} {self.surname}"
    
    def get_age(self, now=2025):
        """ Student's age"""
        return now-self.year
    
    def get_friends(self):
        """ Student's friends """
        info = f"{self.name}ning do'stlari: "
        for ism in self.friends:
            info += f"{ism} "

        return info

    def set_kurs(self):
        """ a function that increases the student's rate (1-6)"""

        if self.kurs < 6:
            self.kurs += 1
        else:
            return "Siz hozirda eng so'nggi kursda siz."

        return self.kurs
    

durbek = Student("Durbek", "Muhiddinov", 2009, 2, [4, 3, 4, 5], ["Ibrohim", "Said", "Otabek"])

# print(durbek.get_info())
# print(durbek.get_middle_ball())
# print(durbek.get_full_name())
# print(durbek.get_age())
# print(durbek.get_friends())
# print(durbek.set_kurs())



""" library class """
class Library():
    """ Kutubxona classi """
    def __init__(self, name:str, adress:str):
        self.name = name
        self.adress = adress
        self.books = []
        self.books_count = 0

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return self.name

    def get_info(self):
        """ Kutubhona haqidagi ma'lumotlarni qaytaradi (nomi, manzili, kutubxonadagi kitoblar soni)"""
        return f" Bu kutubhona haqida ma'lumot {self.name}, manzili {self.adress}, {self.books_count} ta kitob bor."

    def add_book(self, book):
        """ Kutubhonaga kitob qo'shuvchi funksiya """
        self.books.append(book)
        self.books_count += 1
        return f"{book} kitobi qo'shildi." 

    def get_books(self):
        """ Kutubxonadagi kitoblar nomini qaytaradigan funksiya """
        info = f"{self.name}ning kitoblari nomlari: "
        for book in self.books:
            info += f"{book} "

        return info

    def delete_book(self, book):
        """ Kutubxonadan kitobni o'chiruvchi funksiya """
        if book in self.books:
            self.books.remove(book)
            self.books_count -= 1
            return f"{book} kitobi kutubxonadan o'chirildi. "
        else:
            return f" {book} kitobi kutubxonada topilmadi. "

kutubxona1 = Library("Nodira", "4 yoki 3- mkr")


# print(book1.add_book("AAA"))
# print(book1.add_book("SSS"))
# print(book1.get_info())
# print(book1.get_books())

# print(kutubxona1)


""" BOOK mashq """
class Book():
    """ Kitob haqida class """
    def __init__(self, name:str, author:str, year:int, publisher:str, price:int):
        """ """
        self.name = name
        self.author = author
        self.year = year 
        self.publisher = publisher
        self.price = price

    def __str__(self):
        """ Kitob haqida """
        return f"{self.name} kitob"

    def get_info(self):
        """ Kitob haqida ma'lumotlar """
        return f"{self.name} kitobi {self.author} tomonidan {self.year}-yilda yozilgan. Hozirda uning narhi {self.price} so'm."

    def get_name(self):
        """ Kitobni nomini chiqarib beruvchi funksiya """
        return self.name

    def get_price(self):
        """ Kitobning narhini ko'rsatib beradigan funksiya """
        return self.price

    def get_year(self):
        """ Kitobning nechanchi yilda yozlganini ko'rsatib beradigan funksiya """
        return self.year

    def get_author(self):
        """ Kitobning muallifini ko'rsatib beradigan funksiya """
        return self.year

book1 = Book("Rome & Julietta", "Uilyam Shekspeare", 1591, "bilmadim", 65_000)


""" Obyekting hususiyat va metodlarini ko'rish """
""" dir() funksiyasi """
from pprint import pprint  # prety print 
print(dir(kutubxona1))
print(dir(book1))


""" __dict__ metodi """
""" __dict__ metodi obyektning hususiyatlarini lug'at ko'rinishida qaytaradi """
pprint(kutubxona1.__dict__)
pprint(book1.__dict__)

