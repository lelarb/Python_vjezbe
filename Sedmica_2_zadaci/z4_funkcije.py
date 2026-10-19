# =============================================================
# ZADATAK 4: Funkcije   (~8 minuta)
# =============================================================

# a) Napiši funkciju prosjek(lista) koja vraća prosjek brojeva u listi.
#    Ako je lista prazna, neka vrati 0.
def prosjek(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


# b) Napiši funkciju je_paran(n) koja vraća True ako je n paran,
#    a False ako nije.
def je_paran(n):
    return n % 2 == 0


# c) Napiši funkciju ocjena(bodovi) koja vraća ocjenu prema
#    pravilima iz Zadatka 3a.
def ocjena(bodovi):
    if 0 <= bodovi <= 54:
        return 5
    elif bodovi <= 64:
        return 6
    elif bodovi <= 74:
        return 7
    elif bodovi <= 84:
        return 8
    elif bodovi <= 94:
        return 9
    elif bodovi <= 100:
        return 10
    else:
        return "Neispravan broj bodova!"


# d) Napiši funkciju samo_parni(lista) koja vraća NOVU listu
#    samo sa parnim brojevima. Iskoristi funkciju je_paran!
def samo_parni(lista):
    rezultat = []

    for broj in lista:
        if je_paran(broj):
            rezultat.append(broj)
    return rezultat


# --- Testiranje (ne mijenjaj) -------------------------------
print(prosjek([8, 9, 10]))          # 9.0
print(prosjek([]))                  # 0
print(je_paran(4), je_paran(7))     # True False
print(ocjena(50), ocjena(78), ocjena(100))   # 5 8 10
print(samo_parni([1, 2, 3, 4, 5, 6]))        # [2, 4, 6]
