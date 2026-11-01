# =============================================================
# ZADATAK 1: Stvarni rođendani - da li se paradoks potvrdio?
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# U fajlu real_birthdays.txt su rođendani studenata (format DD-MM).
# Provjeri da li u našoj grupi postoje isti rođendani i uporedi
# rezultat sa teorijom (Birthday Paradox).
# =============================================================
import os
from collections import Counter

# Putanja do fajla koji se nalazi u istom folderu kao ova skripta
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")

# --- Učitavanje ---------------------------------------------
# Učitaj sve datume iz fajla u listu datumi.
# Savjet: with open(FAJL, "r", encoding="utf-8") as f:
#         strip() i preskoči prazne redove
datumi = []
with open(FAJL, "r", encoding="utf-8") as f:
    for red in f:
        datum = red.strip()
        if datum:
            datumi.append(datum)
print(datumi)


# a) Koliko je ukupno rođendana?            (očekivano: 38)
ukupno = len(datumi)
print("Ukupno rođendana:", ukupno)


# b) Koliko je JEDINSTVENIH rođendana?      (očekivano: 34)
#    Savjet: set()
jedinstveni = set(datumi)
broj_jedinstvenih = len(jedinstveni)
print("Broj jedinstvenih rođendana je:", broj_jedinstvenih)


# c) Postoje li duplikati? Ispiši True/False.
duplikati = len(datumi) != len(set(datumi))
print("Postoje duplikati:", duplikati)


# d) Koji se datumi ponavljaju? Ispiši ih SORTIRANO, npr:
#       03-01 -> 2 puta
#    Savjet: Counter(datumi), pa sorted(...)
brojac = Counter(datumi)
for datum, broj in sorted(brojac.items()):
    if broj > 1:
        print(f"{datum} -> {broj} puta")


# e) Uporedi sa teorijom.
#    Vjerovatnoća da u grupi od n osoba NIKO nema isti rođendan je:
#       (365/365) * (364/365) * (363/365) * ... * ((365-n+1)/365)
#    Vjerovatnoća poklapanja = 1 - to.
#    Napiši funkciju i ispiši:
#       Teorijska vjerovatnoća za 38 osoba: 86.4%
def vjerovatnoca_poklapanja(n):
    bez_poklapanja = 1
    for i in range(n):
        bez_poklapanja *= (365 - i) / 365
    return 1 - bez_poklapanja

rezultat = vjerovatnoca_poklapanja(len(datumi))
print(f"Teorijska vjerovatnoća za {len(datumi)} osoba: {rezultat * 100:.1f}%")


# BONUS: Koliko je rođendana u svakom mjesecu?
#    Savjet: mjesec je dio iza crtice -> datum.split("-")[1]
mjeseci = []

for datum in datumi:
    mjesec = datum.split("-")[1]
    mjeseci.append(mjesec)

broj_po_mjesecima = Counter(mjeseci)

for mjesec, broj in sorted(broj_po_mjesecima.items()):
    print(f"{mjesec}: {broj} rođendana")
