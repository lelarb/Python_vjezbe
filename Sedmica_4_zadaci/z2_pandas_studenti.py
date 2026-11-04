# =============================================================
# ZADATAK 2: Studenti u pandasu
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# Isti podaci kao u Zadatku 1, ali sada sa pandasom.
# Uporedi koliko je koda trebalo u Zadatku 1, a koliko ovdje!
#
# a) Učitaj studenti.csv i ispiši dimenzije i prvih 5 redova.
#       očekivano: Dimenzije: (40, 7)
#
# b) Dodaj kolonu "prosjek" = (matematika + programiranje + statistika) / 3
#
# c) Ispiši top 5 studenata po prosjeku (kolone ime, smjer, prosjek).
#    Savjet: sort_values("prosjek", ascending=False, kind="stable").head(5)
#       očekivano: Ema 9.00, Selma 8.67, Ismar 8.67, Tarik 8.33, Dino 8.33
#
# d) Koliko studenata ima svaki smjer?  Savjet: value_counts()
#       očekivano: Informatika 14, Elektrotehnika 14, Menadžment 12
#
# e) Prosjek po smjeru, sortiran opadajuće.  Savjet: groupby
#       očekivano: Informatika 8.10, Elektrotehnika 7.29, Menadžment 7.00
#
# f) Koji studenti imaju prisustvo ispod 70%? Ispiši ime i prisustvo.
#       očekivano: 8 studenata
#
# BONUS: dodaj kolonu "polozio" (True ako su sve tri ocjene >= 6).
#        Koliko je položilo ukupno, a koliko po smjeru?
#       očekivano: 25 ukupno; Informatika 14, Elektrotehnika 8, Menadžment 3
# =============================================================
import os
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "studenti.csv")

# a) TODO: učitaj podatke i ispiši shape i head()


# b) TODO: kolona prosjek


# c) TODO: top 5


# d) TODO: value_counts


# e) TODO: groupby


# f) TODO: filtriranje prisustva


# BONUS: TODO

print("Zadatak 2 - dopuni TODO dijelove.")
