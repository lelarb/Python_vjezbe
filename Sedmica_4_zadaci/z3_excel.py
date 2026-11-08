# =============================================================
# ZADATAK 3: Excel - spajanje sheetova, obrada i export
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# studenti.xlsx ima dva sheeta: "Grupa_A" i "Grupa_B" (po 20 studenata).
# Instalacija (ako već nije): pip install pandas openpyxl
#
# a) Učitaj oba sheeta u dva DataFrame-a.  Savjet: sheet_name="Grupa_A"
#
# b) Svakom dodaj kolonu "grupa" sa vrijednošću "A", odnosno "B".
#
# c) Spoji ih u jedan DataFrame.  Savjet: pd.concat([...], ignore_index=True)
#       očekivano: (40, 8)
#
# d) Dodaj kolone:
#       "prosjek" = (matematika + programiranje + statistika) / 3, zaokruženo na 2
#       "polozio" = True ako su sve tri ocjene >= 6
#       očekivano: (40, 10), položilo 25
#
# e) Spremi u "rezultati.xlsx" sa DVA sheeta:
#       "Svi"      - svih 40 studenata
#       "Polozili" - samo oni koji su položili (25)
#    Savjet:
#       with pd.ExcelWriter(putanja) as pisac:
#           df.to_excel(pisac, sheet_name="Svi", index=False)
#
# f) Pretvori sheet "Svi" iz rezultati.xlsx u "rezultati.csv" (index=False),
#    pa ga učitaj nazad i ispiši shape.  očekivano: (40, 10)
# =============================================================
import os
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
EXCEL = os.path.join(FOLDER, "studenti.xlsx")
IZLAZ_XLSX = os.path.join(FOLDER, "rezultati.xlsx")
IZLAZ_CSV = os.path.join(FOLDER, "rezultati.csv")

# a) TODO: učitaj Grupa_A i Grupa_B
grupa_a = pd.read_excel(EXCEL, sheet_name="Grupa_A")
grupa_b = pd.read_excel(EXCEL, sheet_name="Grupa_B")

# b) TODO: kolona "grupa"
grupa_a["grupa"] = "A"
grupa_b["grupa"] = "B"

# c) TODO: concat
studenti = pd.concat([grupa_a, grupa_b], ignore_index=True)

print("\nSpojeni podaci:")
print(studenti.shape)
print(studenti.head())

# d) TODO: prosjek i polozio
studenti["prosjek"] = ( studenti["matematika"] +
                        studenti["programiranje"] +
                        studenti["statistika"] ) / 3
studenti["prosjek"] = studenti["prosjek"].round(2)

studenti["polozio"] = ( (studenti["matematika"] >= 6) &
                        (studenti["programiranje"] >= 6) &
                        (studenti["statistika"] >= 6) )

print("\nDimenzije nakon dodavanja kolona:", studenti.shape)
print("\nUkupno položilo:", studenti["polozio"].sum())

# e) TODO: ExcelWriter sa dva sheeta
with pd.ExcelWriter(IZLAZ_XLSX) as pisac:
    studenti.to_excel(pisac, sheet_name="Svi", index=False)

    polozili = studenti[studenti["polozio"] == True]

    polozili.to_excel(pisac, sheet_name="Polozili", index=False)

# f) TODO: Excel -> CSV i provjera
svi_studenti = pd.read_excel(IZLAZ_XLSX, sheet_name="Svi")

svi_studenti.to_csv(IZLAZ_CSV, index=False)

provjera = pd.read_csv(IZLAZ_CSV)

print("\nDimenzije učitanog CSV fajla:", provjera.shape)
