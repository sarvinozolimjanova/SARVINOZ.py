""" 1 - mashq """
city = []
city.append(input("shahar nomini kiriting: ").lower())
city.append(input("shahar nomini kiriting: ").lower())
city.append(input("shahar nomini kiriting: ").lower())
city.append(input("shahar nomini kiriting: ").lower())
city.append(input("shahar nomini kiriting: ").lower())
city.append(input("shahar nomini kiriting: ").lower())
city.append(input("shahar nomini kiriting: ").lower())

print(city)

del city[0]
city.remove("samarqand")
city.pop()
print(city)

city.append("xiva")
city.insert(2, "navoi")
print(city)

city.sort()
print(city)    

city.sort(reverse=True)
print(city)      

city.clear()
print(city)

del city
print(city)


""" 2 - mashq """
friend = {
    "name":input("do'stingiz ismini kiriting: "),
    "surname":input("do'stingiz familiyasini kiriting: "),
    "age":int(input("do'stingiz yoshini kiriting: ")),
    "adress":input("do'stingiz manzilini kiriting: "),
    "number":input("do'stingiz telefon raqamini kiriting: "),
}
print(f"Mening do'stimning ismi {friend['name']}, familiyasi {friend['surname']} \
yoshi {friend['age']}da. U {friend['adress']} da yashaydi, uning tel_raqami {friend['number']}.")


""" 3 - mashq """
eng_uzb = {
    'rose':'atirgul',
    'key':'kalit',
    'book':'kitob',
    'pen':'ruchka',
}

savol = input("Biror so'z kiriting: ")
for key, value in eng_uzb.items():
    if savol == key:
        print(f"{key} - {value}")
    elif savol == value:
        print(f"{value} - {key}")
if savol not in eng_uzb.keys() and savol not in eng_uzb.values():
    print("Bizda bu so'z haqida ma'lumot yo'q!")


""" 4 - mashq """
books = {
    'key1':'book1',
    'key2':'book2',
}
print(books)

books = {'key3':'book3'}
books.update({'key4':'book4'})
print(books)

books['key3'] = 'book'
books.update({'key1':'boook'})
print(books)

del books['key1']
books.pop('key2')
books.popitem()
print(books)

books.clear()
print(books)

