""" ZOOPARK """
summa = 0
odam = int(input("Necha kishi kirmoqchisizlar: "))
for son in range(odam):
    yosh = int(input("Yoshingizni kiriting: "))
    if 0 < yosh <=7:
        # print("Sizga kirish bepul!") 
        summa += 0
    elif 7 < yosh <= 18:
        # print("Sizga kirish 15.000 so'm !")
        summa += 15.000
    elif 18 < yosh <=70:
        # print("Sizga kirish 25.000 so'm !")
        summa += 25.000
    elif 70 < yosh <= 100:
        # print("Sizga kirish bepul!")
        summa += 0
    elif yosh > 100:
        print("Siz hato son kiritdingiz!")
    else:
        print("Faqat musbat son kiritish mumkin!!!")

print(f"Sizdan {summa} so'm to'lov talab qilinadi !")


