"""  GAME  """
import random

savol = int(input("1-10gacha son kiriting: "))
son = random.randrange(1, 10)

if savol == son:
    print("Siz toptingiz !!!")
else:
    print(f"Siz yutqzdingiz! Komp tanlagan son {son} edi.")











