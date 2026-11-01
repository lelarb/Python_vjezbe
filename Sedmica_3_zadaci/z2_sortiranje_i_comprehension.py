# =============================================================
# ZADATAK 2: Sortiranje, list comprehension, zip, enumerate, random
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
import os
import random

studenti = ["Amra", "Emir", "Lejla", "Tarik", "Ana"]
bodovi = [78, 92, 65, 88, 92]

# a) Pomoću zip() napravi listu parova (ime, bodovi) i ispiši
#    svaki par u obliku:   Amra: 78
parovi = list(zip(studenti, bodovi))
for ime, bodovi_studenta in parovi:
    print(f"{ime}: {bodovi_studenta}")


# b) Sortiraj parove po bodovima OPADAJUĆE i ispiši rang listu
#    pomoću enumerate(..., start=1):
#       1. Emir - 92
#       2. Ana - 92
#       ...
#    Savjet: sorted(parovi, key=lambda p: p[1], reverse=True)
rang_lista = sorted(parovi, key=lambda p: p[1], reverse=True)
for redni_broj, (ime, bodovi_studenta) in enumerate(rang_lista, start=1):
    print(f"{redni_broj}. {ime} - {bodovi_studenta}")


# c) List comprehension: lista imena studenata sa 80 ili više bodova.
#    Očekivano: ['Emir', 'Tarik', 'Ana']
studenti_list = [studenti[i] for i in range(len(studenti)) if bodovi[i] >= 80]
print(studenti_list)


# d) Iz fajla real_birthdays.txt (format DD-MM) napravi pomoću
#    list comprehension-a listu MJESECI kao brojeve (int),
#    a zatim ispiši sortirane jedinstvene mjesece.
#    Očekivano: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")
with open(FAJL, "r", encoding="utf-8") as f:
    mjeseci = [ int(red.strip().split("-")[1])
                for red in f
                if red.strip() ]
jedinstveni_mjeseci = sorted(set(mjeseci))
print(jedinstveni_mjeseci)


# e) random: postavi random.seed(42), pa
#    - nasumično izaberi studenta koji odgovara (random.choice)
#    - napravi KOPIJU liste studenti i promiješaj je (random.shuffle)
#      -> to je redoslijed prezentacija
random.seed(42)

izabrani_student = random.choice(studenti)
print("Nasumično izabrani student:", izabrani_student)

prezentacije = studenti.copy()

random.shuffle(prezentacije)
print("Redoslijed prezentacija:", prezentacije)
