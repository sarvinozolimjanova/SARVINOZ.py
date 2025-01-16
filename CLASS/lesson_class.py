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
    """ """
    
    def __init__(self, name:str, surname:str, kurs:int, marks:list):
        self.name = name
        self.surname = surname
        self.kurs = kurs
        self.marks = marks

    def get_info(self):
        return sum(self.marks)/len(self.marks)


durbek = Student("Durbek", "Muhiddinov", 2, [3,4,4,3])
ali = Student("Ali", "Bahodirov", 4, [5, 4, 4, 3])

print(durbek.get_info())
print(ali.get_info())
