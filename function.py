""" Funksiyalar """
# print("Hello world!")

def salom_ber():
    print("Assalomu alekum !")

# salom_ber()


def yosh_top():
    ism = input("Ismingizni kiriting: ")
    t_yil = int(input(f"{ism.title()} tug'ilgan yilingizni kiriting: "))

    print(f"{ism.title()} sizning yoshingiz {2024-t_yil} da.")

# yosh_top()


""" Parametr """
# def yosh_top(t_yil):
#     """ Tug'ilgan yilni qabul qilib olib yoshni hisblaydigan funksiya
    
#     t_yil  --->  int
#     """
#     print(f"Sizning yoshingiz {2024-t_yil} da")

# yosh_top(2012)
# yosh_top(2005)

# x = int(input("T yil kiriting: "))
# yosh_top(x)


"""
"""
# print(print.__doc__) # duble under score --> du nder methdods
# print(max.__doc__)
# print(len.__doc__)
# print(yosh_top.__doc__)

# """ Parametrni key_word bilan birga berish """
# def yosh_top(ism, t_yil):
#     print(f" Salom {ism.title()}, Siz {t_yil}-yilda tug'ilgan siz va yoshingiz {2024-t_yil} da.")

# yosh_top("Ali", t_yil=2012)

# """ Standart qiymat """
# def yosh_top(ism, t_yil):
#     print(f"Salom {ism.title()}, Siz {t_yil}-yilda tug'ilgansiz va yoshingiz {2024-t_yil} da.")

# yosh_top("Ali", t_yil=2009)


""" 1 - mashq """
# print((len.__doc__))
# print((max.__doc__))
# print((sum.__doc__))
# print((range.__doc__))
# print((list.__doc__))


# """ 2 - mashq """
# def bal_top():
#     """ Foydalanuvchidan imtihon balini so'rab, uni yahshi yoki yomonligini aniqlovchi funksiya """
#     savol = int(input("Imtihon balingizni kiriting: "))
#     if 0 < savol <= 50:
#         print(f"Siz {savol} bal to'pladingiz va bu qoniqarsz!")
#     elif 51 < savol <= 70:
#         print(f"Siz {savol} bal to'pladingiz va bu qoniqarli!")
#     elif 71 < savol <= 90:
#         print(f"Siz {savol} bal to'pladingiz va bu yahshi!")
#     elif 91 < savol <= 100:
#         print(f"Siz {savol} bal to'pladingiz va bu a'lo!!!")

# bal_top()


# """ 3 = mashq """
# def perimetr(a, b):
#     """ To'g'ri to'rtburchakning perimetrini topuvchi funksiya """
#     print(f"Tomonlari {a} va {b} ga teng bo'lgan to'g'ri burchakning perimetri {2*(a+b)} ga teng.")
# perimetr(7, 5)

# def yuza(a, b):
#     """ To'g'ri to'rtburchakning yuzini topuvchi funksiya """
#     print(f"Tomonlari {a} va {b} ga teng bo'lgan to'g'ri burchakning perimetri {a*b} ga teng.")
# yuza(77, 3)


# """ 4 - mashq """
sonlar = [23, -6, 9, 244, 0, -4, 43]
def tartibla(qiymat):
    qiymat.sort()
    print(qiymat)
tartibla(sonlar)


""" Funksiya qiymat qaytarish """
# def yosh_top(t_yil: int, ism: str, oila: list) -> int: #t_yil - parametr
def yosh_top(t_yil: int) -> int: #t_yil - parametr
    """ Tug'ilgan yilni qabul qilib olib, yoshni qaytaradigan funksiya """
    yosh = 2024-t_yil
    return yosh
    # return f"Salom {ism}"

# sarvinozning_yoshi = yosh_top(2009)
# print(f"Sarvinozning yoshi {sarvinozning_yoshi} da.")


""" mashq """
def new_person(name: str, surname: str, age: int, email: str, phone: int) -> dict:
    person = {
        'name': name,
        'surname':surname,
        'age':age,
        'email':email,
        'phone':phone
    }
    return person

# person1 = new_person("Sarvinoz", "Olimjonova", 15, "sarvinoz@gmail.com", 123456789)
# print(person1)


""" mashq """
def family(dad: str, mum: str, sister: str, brother: str) -> list:
    new_family = [dad, mum, sister, brother]
    return new_family

# family1 = family("ddddd", "sssss", "zzzzz", "mmmmmm")
# print(family1)


""" mashq """
def baholash(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()} imtihon balini kiriting: ")
        baholar[ism] = baho
    return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = baholash(talabalar)
# print(baholar)


""" info mashq """
def info(name: str, age: int, sinf='9green') -> str:
    """ Ismni, yoshni va sinfni chiqarb beradgan funksiya """
    return f"{name.title()} your age {age}, your class {sinf}"

student = info(sinf= "10a", age=15, name="Sarvinoz")
# print(student)


""" MASHQ """
def juft(son):
    """ 0 dan parametr sifatida uzatilgan songacha bo'lgan ro'yhat yaratuvchi funksiya """
    x = list(range(0, son, 2))
    return x  

# son1 = juft(100)
# print(son1)


""" *args usuli """
def my_sum(*sonlar): # *arg
    """ sum funksiyasi """
    summa = 0
    for son in sonlar:
        summa = summa + son
    return summa

# print(my_sum(4, 77, -9, 0, 15, -2, 4))
# print(my_sum(2, 5))
# print(my_sum())


""" ENG KATTA SONNI TOPISH """
def my_max(*numbers):
    """ Eng katta sonni topuvchi funksiya """
    x = sorted(numbers)
    return x[-1]

# numbers1 = my_max(12, -9, 77, 7, 1000, 4, 76, 923345, -22234567, -2, 1111)
# print(numbers1)


""" ENG KATTA SONNI TOPISH """
def my_max2(*numbers):
    """ Eng katta sonni topuvchi funksiya """
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    
    return maximum

# numbers2 = my_max2(12, -9, 77, 7, 1000, 4, 76, 923345, -22234567, -2, 1111)
# print(numbers2)


""" ENG KICHIK SONNI TOPISH """
def my_min(*numbers):
    """ Eng katta sonni topuvchi funksiya """
    x = sorted(numbers)
    return x[0]

# print(my_min(12, -9, 77, 7, 1000, 4, 76, 923345, -22234567, -2, 1111))


""" len() ni yasash """
def yasama_len(*numbers):
    qoshlma = 0
    for number in numbers:
        qoshlma += 1

    return qoshlma

# print(yasama_len(12, 44, 77, 99, -3, 77))
# print(yasama_len("Assalomu",  "alekum",  "Sarvinoz"))


""" Yasama range 1-usul """
def yasama_range(a:int, b:int) -> list:
    """ Yasama range() funksiyasi"""
    sonlar = [a]
    for son in sonlar:
        if son < b-1:
            sonlar.append(son+1)
    return sonlar

# print(yasama_range(7, 17))


""" Yasama range 2-usul """
def yasama_range2(a:int, b:int, c=1) -> list:
    """ Yasama range() funksiyasi"""
    sonlar1 = [a]
    for son in sonlar1:
        if son < b-1:
            sonlar1.append(son+c)
    return sonlar1

# print(yasama_range2(7, 28))


""" Yasama sqrt """
def my_sqrt(son:int):
    x = son**0.5
    return x

# print(my_sqrt(81))


""" Unli undosh funksiyasi """
# undosh = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
def harflar(harf:str) -> str:
    unli = ["a", 'e', 'i', 'o', 'u']
    if harf in unli:
        return f"{harf.title()} unli harf."
    else:
        return f"{harf.title()} undosh harf."

# print(harflar("s"))
# print(harflar('o'))


""" o'rta arifmetik """
def arifmetik(*sonlar:int):
    arif = sum(sonlar)/len(sonlar)
    return arif

# print(arifmetik(12, 66, 77, -3, 5, 22, -111))


""" o'rta arifmetik 2 """
def arifmetik2(*sonlar):
    """ o'rta arifmetik 2-usuli """
    summa = 0
    qoshlma = 0
    for son in sonlar:
        summa = summa + son
        qoshlma += 1
        
    return summa/qoshlma

# print(arifmetik2(22, 44, 88, -99, -1, 24))
# print(arifmetik2(22, 44))

