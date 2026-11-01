# =============================================================
# ZADATAK 5: Grafikon - rođendani po mjesecima
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# Nacrtaj stupčasti grafikon (bar chart) koji pokazuje koliko
# studenata iz real_birthdays.txt je rođeno u svakom mjesecu.
# (Prvo instaliraj matplotlib, vidi primjer p5_grafikon.py.)
# =============================================================
import os
from collections import Counter
from matplotlib import pyplot as plt

FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")
MJESECI = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun",
           "Jul", "Avg", "Sep", "Okt", "Nov", "Dec"]

# a) Učitaj datume i prebroj koliko ih je u svakom mjesecu.
#    Mjesec je dio iza crtice: "15-06" -> 6
#    Savjet: Counter(...) ili rječnik
# TODO


# b) Napravi listu broj_po_mjesecima sa 12 brojeva, redom od januara
#    do decembra. Očekivano: [5, 2, 3, 3, 2, 2, 5, 6, 3, 3, 2, 2]
broj_po_mjesecima = []
# TODO

print("Broj rođendana po mjesecima:", broj_po_mjesecima)

# c) Nacrtaj bar chart:
#    plt.bar(MJESECI, broj_po_mjesecima)
#    naslov: "Rođendani po mjesecima (38 studenata)"
#    oznaka y ose: "Broj rođendana"
#    pa plt.show()
# TODO


# d) BONUS:
#    - mjesec sa najviše rođendana oboji drugom bojom
#      (savjet: lista boja, npr. ["#3A7CA5", ..., "#F2A541", ...] i color=boje)
#    - iznad svakog stupca ispiši broj (plt.text(x, y, tekst, ha="center"))
#    - sačuvaj sliku: plt.savefig("z5_grafikon.png") PRIJE plt.show()
# TODO
