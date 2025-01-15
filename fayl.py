def kalkulyator():
    print("Kalkulyatorga xush kelibsiz!")
    print("Amallar:")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")

    tanlov = input("Amalni tanlang (1/2/3/4): ")

    if tanlov in ['1', '2', '3', '4']:
        try:
            a = float(input("Birinchi sonni kiriting: "))
            b = float(input("Ikkinchi sonni kiriting: "))

            if tanlov == '1':
                natija = a + b
                amal = "Qo'shish"
            elif tanlov == '2':
                natija = a - b
                amal = "Ayirish"
            elif tanlov == '3':
                natija = a * b
                amal = "Ko'paytirish"
            elif tanlov == '4':
                natija = a / b
                amal = "Bo'lish"
                
            print(f"{amal} natijasi: {natija}")
        except ValueError:
            print("Iltimos, sonlarni to'g'ri kiriting!")
    else:
        print("Noto'g'ri tanlov!")

kalkulyator()













