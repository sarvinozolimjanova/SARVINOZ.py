# """ 1 - Mashq"""
# ism = "Sarvinoz"
# familiya = "Olimjonova"
# yosh = 15
# kitoblar = ["garri potter"]
# kasb = "Advokat"
# print(type(ism))
# print(type(familiya))
# print(type(yosh))
# print(type(kitoblar))
# print(type(kasb))


# """ 2 - Mashq """
# from math import sqrt
# print(round(sqrt(4364+1233),2))


# """ 3 - mashq """
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))

# print((son1**2)+(son2**2)/23)


# """ 4 - mashq """
# x  = input("son kirit: ")
# x = int(x)
# print(type(x))

# x = float(x)
# print(type(x))


# """ 5 - mashq """
# books = []

# books.append(input("Kitob nomini kirit: "))
# books.append(input("Kitob nomini kirit: "))
# books.append(input("Kitob nomini kirit: "))
# books.append(input("Kitob nomini kirit: "))
# books.append(input("Kitob nomini kirit: "))


# """ 6 - mashq """
# students = ["Ali", "Ma'ruf", "Bahrom"]
# print(students)

# students.insert(0, "Hadicha")
# students.insert(5, "Hadicha")
# students.insert(3, "Hadicha")

# students[4] = "Oydina"
# students[2] = "Oydina" 
# print(students)


"""""""""""""""""""""""""""""""""""""""""""""""""""""
4-list
"""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 1 - MASHQ """
# sonlar = [45, -96, 0, 63.2, 1257, -6752.2, 42, 3, 542]
# print(sonlar)

# sonlar.sort()
# print(sonlar)

# sonlar.sort(reverse=True)
# print(sonlar)

# sonlar.reverse()
# print(sonlar)


# """ 2 - mashq """
# mevalar = ["olma", "shaftoli", "o'rik", 'apelsin', 'malina', 'xurmo']
# for meva in mevalar:
#     if meva == "olma" or meva == "malina":
#         print(meva.upper())
#     else:
#         print(meva.title())


# """ 3 - mashq """
# books = {
#     'key1':'kitob',
#     'key2':'kitob2',
# }
# print(books)

# books['key3'] = "kitob3"
# books.update({'key4':'kitob4'})
# print(books)

# books['key3'] = "kitob5"
# books.update({'key4':'kitob7'})
# print(books)

# del books['key1']
# books.popitem()
# books.pop()
# print(books)

# books.clear()
# print(books)


# """ 4 - mashq """
# from math import sqrt
# sonlar = list(range(102, 2020))
# for son in sonlar:
#     if 102 < son < 1000:
#         print(son**3)
#     elif son > 1500:
#         print(son-4)
#     if son%7==0:
#         print(sqrt(son))


# """ 5 - mashq """
# ball = int(input("Imtixondan necha ball oldingiz: "))
# if 64 < ball <= 100:
#     savol = int(input("Nechanchi o'rinni oldingiz: "))
#     if savol == 1:
#         print("Tabriklaymiz, siz 100% lik grantni qo'lga kiritdingiz !!!")
#     elif savol == 2:
#         print("Tabriklaymiz, siz 75% lik grantni qo'lga kiritdingiz !!!")
#     elif savol == 3:
#         print("Tabriklaymiz, siz 50% lik grantni qo'lga kiritdingiz !!!")
#     elif savol == 4:
#         print("Tabriklaymiz, siz 25% lik grantni qo'lga kiritdingiz !!!")
#     elif savol > 4:
#         print("Tabriklaymiz, siz imtihondan o'tdingiz :)")
# elif 0 < ball <= 64:
#     print("Siz imtihondan o'ta olmadingiz :(")
# else:
#     print("Iltimos, to'g'ri son kiriting !")


""""""""""""""""""""""""""""""" 6 - imtihon """""""""""""""""""""""""""""""""""""""""""""
# """ 1 - mashq """
# eng_uzb = {
#     'flower':'gul',
#     'book':'kitob',
#     'food':'taom',
#     'pen':'ruchka',
# }

# savol = input("So'z kiriting: ")
# for key, value in eng_uzb.items():
#     if savol == key:
#         print(f"{key} - {value}")
#     elif savol == value:
#         print(f"{value} - {key}")
# if savol not in eng_uzb.keys() and savol not in eng_uzb.values():
#     print("Kechirasz, bizda bunday so'z haqida ma'lumot yo'q !")



# """ 2 - MASHQ """
# restoran = {
#     'pitsa':75_000,
#     'lavash':24_000,
#     'shashlik':12_000,
#     'sushi':65_000,
#     'kfc':50_000,
#     'chechevitsa':22_000,
#     'borsh':21_000,
#     'gamburger':35_000,
#     'pide':45_000,
#     'mastava':22_000,
# }

# savol = input("Qanday taom hohlaysiz: ").lower()

# for taom, narh in ismlar.items():
#     if savol == taom:
#         print(f"{taom} - {narh}")

# if savol not in restoran.keys() and savol not in restoran.values():
#     print("Kechirasz, bizda bunday taom yo'q !")


# """ 3 - mashq """
# ism = input("Ismingizni kiriting: ").lower()
# yosh = int(input(f"{ism.title()} yoshingizni kiriting: "))
# if 1 <= yosh <= 6:
#     print(f"{ism.title()} siz bog'cha yoshidasiz :)")
# elif 7 <= yosh <= 17:
#     print(f"{ism.title()} siz maktab o'quvchisisiz :)")
# elif 18 <= yosh <= 30:
#     print(f"{ism.title()} siz universitet talabasisiz :)")
# elif 31 <= yosh <= 100:
#     print(f"{ism.title()} siz maktab o'quvchisi emassiz !")
# else:
#     print("Noto'g'ri son kiritildi!!!")


# """ 4 - MASHQ"""
# ismlar = {
#     'olimjonova':'sarvinoz',
#     'botirova':'hadicha',
#     'malikova':'naima',
#     'tohirova':'rahima',
# }
# savol = input("Ism kiriting: ").lower()

# for familiya, ism in ismlar.items():
#     if savol == ism:
#         print(f"{familiya.title()} - {ism.title()}")
#     elif savol == ism:
#         print(f"{ism.title()} - {familiya.title()}")

# if savol not in ismlar.keys() and savol not in ismlar.values():
#     print("Bizda bunday o'quvchi haqida ma'lumot yo'q !")
