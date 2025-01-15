""" Theme: While"""

# kitoblar = []

# while True:
#     kitoblar.append((input("Biror kitob nomini kiriting: ")))

#     savol = input("Yana kitob qo'shmoqchimisiz(yes/no): ")
#     if savol.lower() == 'no':
#         break
#     elif savol.lower() == 'yes':
#         continue

# print(kitoblar)


""" PAROL TIZIMI """

# parol = '12345678'
# urunishlar_soni = 0
# while True :

#         savol = input("Parol kiriting: ")
#         if savol == parol:
#             print('Siz parolni topdingiz!')
#             break
#         elif savol != parol:
#             urunishlar_soni += 1
    
#         if urunishlar_soni >= 3:
#              while True:
#                   print("Siz parolni topa olmadingiz !!!")




#camellia
""" imtihon """
ball = int(input("Imtixondan necha ball oldingiz: "))
if 64 < ball <= 100:
    savol = int(input("Nechanchi o'rinni oldingiz: "))
    if savol == 1:
        print("Tabriklaymiz, siz 100% lik grantni qo'lga kiritdingiz !!!")
    elif savol == 2:
        print("Tabriklaymiz, siz 75% lik grantni qo'lga kiritdingiz !!!")
    elif savol == 3:
        print("Tabriklaymiz, siz 50% lik grantni qo'lga kiritdingiz !!!")
    elif savol == 4:
        print("Tabriklaymiz, siz 25% lik grantni qo'lga kiritdingiz !!!")
    elif savol > 4:
        print("Tabriklaymiz, siz imtihondan o'tdingiz :)")
elif 0 < ball <= 64:
    print("Siz imtihondan o'ta olmadingiz :(")
else:
    print("Iltimos, to'g'ri son kiriting !")