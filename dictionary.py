"""
Theme: Dictionary(Lug'atlar)
"""

# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'olim':"mastava",
#     'nodir':'kabob'
# }

# """
# taomlar = {'ali':'osh'}
# nomi = {'key':'value'}
# """

# print(taomlar)
# print(type(taomlar)) # dictionary --> dict --> Lug'at

# print(taomlar['ali'])
# print(f"Olimning sevimli taomi {taomlar['olim']}")



# buyumlar = {
#     'ism':'Sarvinoz',
#     'yosh':15,
#     'abituryent':True,
#     'oila':['ota', 'ona', 'opa']
# }

# print(buyumlar)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

green_9 = {
    'olimjonova':'Sarvinoz',
    'botirova':'Hadicha',
    'malikova':'Naima',
    'tohirova':'Rahima',
}
# print(green_9)

""" Lug'atga element qo'shish """
green_9.update({'mamadova':'Oydina'})
print(green_9)

green_9['fazliddinova'] = 'Mubina'
print(green_9)

# green_9[input("Familiya kiriting: ").lower()] = input('Ism Kiriting: ')
# print(green_9)

""" Elementni o'zgartirish """
green_9.update({'mamadova':"Go'zal"})
print(green_9)

green_9['fazliddinova'] = 'Malika'


""" Elementni o'chirish """
del green_9['botirova']
print(green_9)

green_9.pop('fazliddinova')
print(green_9)

green_9.popitem()
print(green_9)


""" Lug'atni o'chirish """
# del green_9


""" MASHQ """
otam = {
    'ism':'Shuhrat',
    'familiya':'Alijonov',
    't_yil':1980,
    'shahar':'Namangan',
}

onam = {
    'ism':'Nargiza',
    'familiya':'Dadaboeva',
    't_yil':1983,
    'shahar':'Namangan',
}

opam = {
    'ism':'Zulfizar',
    'familiya':'Olimjonova',
    'yosh':19,
    'student':True
}


print(f"Dadamning ismi {otam['ism']}, {otam['t_yil']}-da, {otam['shahar']} da tug'ilgan.")


""" Lug'atni tozalash """
green_9.clear()
print(green_9)

""" Nusxa olish """
blue_9 = green_9.copy()
print(blue_9)

math_students = dict(green_9)
print(math_students)


""" .get() - metodi """
print(green_9['abdulahad']) # hato chqadgan kod


""" .keys(), values(), items() - metodlari """
green_9 = {
    'olimjonova':'Sarvinoz',
    'botirova':'Hadicha',
    'malikova':'Naima',
    'tohirova':'Rahima',
}

print(green_9.keys())
print(green_9.values())

print(f"9 Green sinfida quidagi o'quvchilar bor: ", end="")
for familiya in green_9.keys():
    print(familiya, end=" ")

print(f"9 Green sinfida quidagi o'quvchilar bor: ", end="")
for ism in green_9.keys():
    print(ism, end=" ")

""" .items() - metodi """
print(green_9.items())
for key, value in green_9.items():
    print(f"{key} - {value}")


eng_uz = {
    'book':'kitob',
    'bread':'non',
}

word = input("So'z kiriting: ").lower()
for key, value in eng_uz.items():
    if word == key:
        print(f"{key} - {value}")
    elif word == value:
        print(f"{value} - {key}")

if word not in eng_uz.keys() and word not in eng_uz.values():
    print("Bizda bu so'z haqida ma'lumot yo'q")


""" Mashq """
davlatlar = {
    'rossiya':'moskva',
    'uzbekistan':'toshkent',
    'angliya':'london',
    'fransiya':'parij',
    'ispaniya':'madrid',
    'portugaliya':'lissabon',
}

"""
1
"""
print(sorted(davlatlar))
print(davlatlar)

print("Davlatlar: ", end="")
for key in davlatlar.keys():
    print(key, end=" ")

print("Poytahtlar: ", end="")
for value in davlatlar.values():
    print(value, end=" ")

"""
2
"""
savol = input("Davlat yoki poytaht kiriting: ").lower()
for key, value in davlatlar.items():
    if savol == key:
        print(f"{key.title()} - {value.title()}")
    elif savol == value:
        print(f"{value.title()} - {key.title()}")

if savol not in davlatlar.keys() and savol not in davlatlar.values():
    print("Bizda bunday ma'lumot yo'q !")



""" 2-MASHQ"""
ismlar = {
    'olimjonova':'sarvinoz',
    'botirova':'hadicha',
    'malikova':'naima',
    'tohirova':'rahima',
}
savol = input("Ism kiriting: ").lower()

for familiya, ism in ismlar.items():
    if savol == ism:
        print(f"{familiya.title()} - {ism.title()}")
    elif savol == ism:
        print(f"{ism.title()} - {familiya.title()}")

if savol not in ismlar.keys() and savol not in ismlar.values():
    print("Bizda bunday o'quvchi haqida ma'lumot yo'q !")



""" 3- MASHQ """
restoran = {
    'pitsa':75_000,
    'lavash':24_000,
    'shashlik':12_000,
    'sushi':65_000,
    'kfc':50_000,
    'chechevitsa':22_000,
    'borsh':21_000,
    'gamburger':35_000,
    'pide':45_000,
    'mastava':22_000,
}

savol = input("Qanday taom hohlaysiz: ").lower()

for taom, narh in ismlar.items():
    if savol == taom:
        print(f"{taom} - {narh}")

if savol not in restoran.keys() and savol not in restoran.values():
    print("Kechirasz, bizda bunday taom yo'q !")






