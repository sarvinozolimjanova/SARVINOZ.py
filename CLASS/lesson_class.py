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
    

durbek = Student("Durbek", "Muhiddinov", 2009, 2, [4, 3, 4, 5], ["Ibrohim", "Said", "Otabek"])

print(durbek.get_info())
print(durbek.get_middle_ball())
print(durbek.get_full_name())
print(durbek.get_age())
print(durbek.get_friends())
