# """ 1 - mashq """
# for son in range(2001, 400, 2):
#     print(son)

# for son in range(302, 500, 2):
#     print(son)

# for son in range(10, 600):
#     if son%25==0:
#         print(son)


# """ 2 - mashq """
# countries = ['US', 'UK', 'Rossiya', 'Shvetsariya', 'Niderlandiya', 'Luxemburg', 'BAA']
# print(countries)

# del countries[-1]
# countries.remove("US")
# countries.pop()

# print(countries)


# """ 3 - mashq """
# names = ['sarvinoz', 'guli', 'oydina', 'naima']
# savol = input("Ismingizni kriting: ")

# if savol in names:
#     print("Kechirasiz sizning ismingiz mening ro'yhatimda bor ekan !")
# else:
#     print("Guruhga hush kelibsiz :)")


""" 4 - mashq """
ombor = ["qulupnay", "apelsin", "gilos", "non"]
print(f"Assalomu alekum. Do'konimizga hush kelibsiz! \nBizda quidagi {len(ombor)} ta mahsulotlar bor:", end=" ")
for mahsulot in ombor:
    if mahsulot == ombor[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == ombor[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")

bor = []
yoq = []
son = int(input("\nNechta mahsulot olmoqchisiz: "))
for s in range(son):
    mahsulot = input(f"{s+1}-mahsulotni kiriting: ")
    if mahsulot in ombor:
        bor.append(mahsulot)
    else:
        yoq.append(mahsulot)

print(f"\nBizda sz sotib olmoqchi bo'lgan quidagi {len(bor)} ta mahsulotlar bor:", end=" ")
for mahsulot in bor:
    if mahsulot == bor[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == bor[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")

print(f"\nBizda sz sotib olmoqchi bo'lgan quidagi {len(yoq)} ta mahsulotlar yo'q:", end=" ")
for mahsulot in yoq:
    if mahsulot == yoq[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == yoq[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")

