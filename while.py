"""
Theme: While
"""

ismlar = []

# for i in range(5):
#     ismlar.append(input("Ism kiriting: "))


""" 1 """
# while True:
#     ismlar.append(input("Ism kiriting: "))

#     savol = input("Dastur tugasinmi (ha/xa): ")
#     if savol == "ha" or savol == "xa":
#         break


""" 2 """
# while True:
#     son = int(input("Son kiriting: "))
#     print(f"Siz kiritgan {son} ning kvadrati {son**2} ga teng.")

#     savol = input("Chiqishni hohlayszmi (ha/yoq): ").lower()
#     if savol == 'ha':
#         print("Dastur tugadi.")
#         break
#     elif savol == 'yoq':
#         continue
#     # else:
#     #     print("Noto'g'ri belgi kiritdingiz !")


""" 3mashq """
# while True:
#     yosh = int(input("Yoshingizni kiriting: "))
#     print(f"Siz {2024-yosh}-yilda tug'ilgansiz.")

#     savol = input("Chiqishni hohlayszmi (exit/quit): ")
#     if savol == 'exit' or savol == 'quit':
#         break
#     else:
#         continue


""" Tug'ilgan yil """
# while True:
#     yosh = input("Tug'ilgan yilingizni kiriting(chiqish uchun 'exit' deb kiriting): ")

#     if yosh.isdigit():
#         print(f"Sizning yoshingiz {2024-int(yosh)} da.")
        
#     elif yosh == 'exit':
#         print("Dastur tugadi.")
#         break


"""
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin.
Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring).  
"""


""" 1 - mashq """
# while True:
#     yosh = input("Yoshingizni kiriting (chiqish uchun 'exit' deb yozing): ")
#     if yosh == 7:
#         print("Sizga kirish 2000 so'm.")
#     elif 8 <= yosh <= 18:
#         print("Sizga kirish 3000 so'm.")
    


""" imtihon tahlil """
# while True:
    # son1 = input("1-sonni kriting: ").lower()
    # if son1 == "stop":
    #     print("Dastur tugadi.")
    #     break

    # son2 = input("2-sonni kriting: ").lower()
    # if son2 == "stop":
    #     print("Dastur tugadi.")
    #     break

    # if son1.isdigit() and son2.isdigit():
    #     son1 = int(son1)
    #     son2 = int(son2)

    #     if son1 > son2:
    #         print(f"{son1} > {son2}")
    #     if son1 < son2:
    #         print(f"{son1} < {son2}")
    #     else:
    #         print(f"{son1} = {son2}")
    # else:
    #     print("Siz faqat son kiritishingiz kerak !")


""" mashq """
# while True:
#     son = input("Son kiriting: ").lower()

#     if son == "chiqish":
#         print("Dastur tugadi.")
#         break

#     if son.isdigit():
#         son = int(son)
#         if son%2 == 0:
#             print(f"{son} juft son.")
#         else:
#             print(f"{son} toq son.")
#     else:
#         print("Faqat son yoki 'chiqish' deb kiritishingiz mumkin.")



""" PAROL TIZIMI """
# s = 0
# parol = 12345
# while True:
#     savol = int(input("Parolni kriting: "))
#     s += 1
#     if savol == parol:
#         print("Hush kelibsiz! ")
#         break
#     if s >= 3:
#         while True:
#             print("ERROR❌")
            






