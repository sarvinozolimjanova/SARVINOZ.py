# import datetime

# """ Vaqtdan vaqtni ayirish """
# hozir = datetime.datetime.now()
# print(hozir)

# bugun = datetime.date.today()
# print(bugun)

# """ Sanadan sanani ayirish """
# tsana = datetime.date(2009, 2, 19)
# print((bugun-tsana).days)

# print(f"{tsana} dan {(bugun-tsana).days} kun o'tib ketdi.")



from datetime import date
""" mashq """
kun = int(input("Tug'ilgan kuningizni kiriting: "))
oy = int(input("Tug'ilgan oyingizni kiriting: "))

bugun = date.today()
yil = bugun.year

tugilgan_kun = date(yil, oy, kun)

if tugilgan_kun < bugun:
    tugilgan_kun = date(yil + 1, oy, kun)

qolgan_kunlar = (tugilgan_kun-bugun).days

print(f"Sizning keyingi tug'ilgan kuningizga {qolgan_kunlar} kun qoldi.")


