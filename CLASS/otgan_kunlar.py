

# import datetime

# def otgan_kunlar(yil:int, oy:int, kun:int) -> str:
#     """ Yashab o'tgan vaqtingizni yil va kun hisobida hisoblab beruvchi funksiya 

#         year - Tug'ilgan yil
#         month - Tug'ilgan oy
#         day - kun 

#         9Green sinfi bilan yasalgan funksiya (06-02-2025)
#     """

#     t_yil = yil # Tug'ilgan yil 
#     t_oy = oy # Tug'ilgan oy
#     t_kun = kun # Tug'ilgan kun
#     t_sana = datetime.date(yil, oy, kun) # Tug'ilgan sana
#     bugun = datetime.date.today() # bugungi sana

#     if (bugun-t_sana).days <= 365: # Hali 1 yoshga to'lmagan chaqaloq uchun
#         return f"Siz tug'ilganizga {(bugun-t_sana).days} kun bo'ldi"
    
#     elif bugun.month > t_oy:
#         yil = bugun.year - t_kun
#         kun = bugun- datetime.date(bugun.year, t_oy, t_kun)
#         return f"Siz tug'ilganizga {yil}-yilu, {kun.days} kun bo'ldi"
    
#     elif bugun.month == t_oy:
#         if bugun.day < t_kun:
#             yil = bugun.year - t_yil-1
#             kun = bugun-datetime.date(bugun.year-1, t_oy, t_kun)
#             return f"Siz tug'ilganizga {yil}-yilu, {kun.days} kun bo'ldi"

#         elif bugun.day == t_kun:
#             yil = bugun.year - t_yil
#             return f"Siz bugun {yil} yoshga toldingiz. Tabriklaymiz !"
        
#         else:
#             yil = bugun.year - t_yil
#             kun = datetime.date(bugun.year, t_oy, t_kun)
#             return f"Siz tug'lganizga {yil}_yilu, {kun.days} kun bo'ldi"
        
#     else:
#         yil = bugun.year - t_yil - 1
#         kun = bugun-datetime.date(bugun.year-1, t_oy, t_kun)
#         return f"Siz tug'ilganizga {yil}-yilu, {kun.days} kun bo'ldi"
    


# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# oy = int(input("Tug'ilgan oyingizni kiriting:"))
# kun = int(input("Tug'ilgan kuningizni kiriting:"))

# foydalanuvchi = otgan_kunlar(yil, oy, kun)
# print(foydalanuvchi)


""" mashq """
from datetime import datetime

# Bugungi sanani olish
today = datetime.today()

# Haftaning kunini raqamda olish (0 = Dushanba, 6 = Yakshanba)
day_of_week = today.weekday()

print(day_of_week)


