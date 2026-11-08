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
studenti = pd.read_csv(FAJL)

print("Dimenzije:", studenti.shape)
print("\nPrvih 5 studenata:")
print(studenti.head())

# b) TODO: kolona prosjek
studenti["prosjek"] = ( studenti["matematika"] +
                        studenti["programiranje"] +
                        studenti["statistika"] ) / 3
print("\nProsjek prvih 5 studenata:")
print(studenti[["ime", "matematika", "programiranje", "statistika", "prosjek"]].head())

# c) TODO: top 5
top_5 = studenti.sort_values( "prosjek",
                              ascending = False,
                              kind = "stable" ).head(5)
print("\nTop 5 studenata po prosjeku:")
print(top_5[["ime", "smjer", "prosjek"]])

# d) TODO: value_counts
broj_po_smjeru = studenti["smjer"].value_counts()

print("\nBroj studenata po smjeru:")
print(broj_po_smjeru)

# e) TODO: groupby
prosjek_po_smjeru = studenti.groupby("smjer")["prosjek"].mean()
prosjek_po_smjeru = prosjek_po_smjeru.sort_values(ascending = False)

print("\nProsjek po smjeru:")
print(prosjek_po_smjeru.round(2))

# f) TODO: filtriranje prisustva
nisko_prisustvo = studenti[studenti["prisustvo"] < 70]

print("\nStudenti sa prisustvom ispod 70%:")
print(nisko_prisustvo[["ime", "prisustvo"]])

# BONUS: TODO
studenti["polozio"] = ( (studenti["matematika"] >= 6) &
                        (studenti["programiranje"] >= 6) &
                        (studenti["statistika"] >= 6) )
ukupno_polozilo = studenti["polozio"].sum()
print("\nUkupno polozilo:", ukupno_polozilo)

polozili_po_smjeru = studenti.groupby("smjer")["polozio"].sum()
print("\nUkupno polozilo po smjeru:")
print(polozili_po_smjeru)