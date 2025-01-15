""" -------------------------Takrorlash--------------------------"""
def full_name(name:str, surname:str) -> str:
    """ Ism va familiyani olib undan to'liq ism qaytaruvchi funksiya """
    full = f"{name.title()} {surname.title()}"
    return full

otabek = full_name("otabek", "ahmedov")
print(otabek)


def yosh_top(ism:str, t_yil:int, h_yil=2024) -> str: # standart / o'zgarmas qiymat
    """ Foydalanuvchidan ismi va tug'ilgan yilini so'rab, yoshini topib beruvchi funksiya """

    """ 1 - usul """
    natija = f"{ism.title()}ning yoshi {h_yil-t_yil} da."
    return natija
    # """ 2 - usul """
    # return f"{ism.title()}ning yoshi {h_yil-t_yil} da."

lola = yosh_top("lola", 2005)
abror = yosh_top("abror", 1986, h_yil=2021)
oydina = yosh_top("oydina", 2009, h_yil=2028)

print(lola)
print(abror)
print(oydina)
