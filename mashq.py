""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
dastur = int(input("Nechta aylana yugurishimiz kerak: "))
print("Biz yugurishni boshladik! ")

for son in range(dastur):
    print(f"{son+1}-aylana tugadi! ")

print("Biz yugurishni tugatdik!")

savol = input("O'tirsak bo'ladimi: ").lower()
if savol == "ha":
    print("Rahmat!")
elif savol  == "yo'q":
    print("Yana qancha yugurishimiz kerak?")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
