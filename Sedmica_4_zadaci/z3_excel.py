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


# b) TODO: kolona "grupa"


# c) TODO: concat


# d) TODO: prosjek i polozio


# e) TODO: ExcelWriter sa dva sheeta


# f) TODO: Excel -> CSV i provjera

print("Zadatak 3 - dopuni TODO dijelove.")
