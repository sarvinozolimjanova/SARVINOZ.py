""" Tashqi kutubhonalar """
""" datetime """
import datetime
# print(datetime.datetime.now())

hozir = datetime.datetime.now()
print(hozir.year)
print(hozir.month)
print(hozir.weekday())
print(hozir.day)
print(hozir.hour)
print(hozir.minute)
print(hozir.second)
print(hozir.microsecond)


""" ishlatish """
print(hozir.date()) # sana
print(hozir.strftime("%A")) # hafta kuni
print(hozir.strftime("%B")) # oy
print(hozir.strftime("%C")) # asr
print(hozir.strftime("%H")) # 
print(hozir.strftime("%I")) # 
print(hozir.strftime("%S")) # 
print(hozir.strftime("%Z")) # 
print(hozir.strftime("%b")) # 
print(hozir.strftime("%j")) # 
print(f"Bugun sana {hozir.strftime("%d-%m-%Y")}")


""" Sanadan sanani ayirish """
bugun = datetime.date.today()
ramazon = datetime.date(2025, 3, 1)
print(ramazon-bugun)

""" Vaqtdan vaqtni ayirish """
bugun1 = datetime.datetime.now()
ramazon1 = datetime.datetime(2025, 3, 1, 00, 00, 1)

print(bugun1)
print(ramazon1)

farq = ramazon1 - bugun1 
print(farq)
print(farq.days)


""" TIMEDELTA """
t_sana = datetime.datetime(2001, 1, 18, 3, 0, 0)
print(t_sana)

print(t_sana + datetime.timedelta(days=20, hours=8))


""" TUG'ILGAN SANANI TOPIB BERUVCHI """
