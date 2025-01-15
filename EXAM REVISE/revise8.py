""" 1 - mashq """
name = "    AnToNy      "
print(name.rstrip())
print(name.lstrip())
print(name.lower())
print(name.upper())
print(name.title())


""" 2 - mashq """
names = ["sarvinoz", 'guli', 'mohinur', 'ruhshona', 'malika', 'maftuna']
print(len(names))

names.sort()
print(names)

names.sort(reverse=True)
print(names)

names.remove("maftuna")
print(names)

names.insert(1, "rano")
names.insert(2, "hadicha")
print(names)


"""3 - mashq """
from math import sqrt
sonlar = list(range(101, 700, 2))
for son in sonlar:
    if son < 200:
        print(son**2)
    elif 300 < son < 400:
        print(sqrt(son))
    elif 500 < son < 700:
        print(son**4)


""" 4 - mashq """










# exam 
#  1ta lugat 1ta while 3ta funksiya













