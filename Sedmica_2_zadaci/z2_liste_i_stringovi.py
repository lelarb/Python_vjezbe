# =============================================================
# ZADATAK 2: Liste i stringovi   (~7 minuta)
# =============================================================

ocjene = [8, 6, 10, 7, 9, 6, 8]

# a) Ispiši prvu i zadnju ocjenu.

print(ocjene[0])
print(ocjene[-1])


# b) Ispiši prve tri ocjene (koristi rezanje / slicing).

print(ocjene[:3])


# c) Student je dobio još jednu ocjenu: 10. Dodaj je u listu.

ocjene.append(10)
print(ocjene)


# d) Izračunaj i ispiši prosjek ocjena na 2 decimale.
#    Savjet: sum() i len()

prosjek = sum(ocjene) / len(ocjene)
print(f"Prosjek ocjena je {prosjek:.2f}")


# e) Ispiši da li student ima ocjenu 6 (True/False).

print(6 in ocjene)


# f) Zadana je rečenica. Ispiši koliko ima riječi
#    i koja je najduža riječ.
#    Savjet: split(), a za najdužu riječ max(rijeci, key=len)
recenica = "analiza podataka pomaže da donosimo bolje odluke"

recenica = "Analiza podataka pomaže da donosimo bolje odluke"

rijeci = recenica.split()
print(f"Broj rijeci: {len(rijeci)}")

najduza_rijec = max(rijeci, key=len)
print(f"Najduža riječ: {najduza_rijec}")
