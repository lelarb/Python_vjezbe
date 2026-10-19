# =============================================================
# ZADATAK 5: Rječnici i skupovi - "Rođendani u grupi"  (~5 minuta)
# Veza sa predavanjem: Birthday Paradox
# =============================================================

rodjendani = [
    "03-14", "07-22", "11-05", "03-14", "01-30", "09-09",
    "12-25", "07-22", "05-17", "02-28", "10-10", "07-22",
    "04-01", "08-15", "06-06", "11-05", "03-03", "09-18",
]

# a) Koliko je ukupno rođendana u listi?
print("Ukupan broj rođendana:", len(rodjendani))


# b) Koliko ima JEDINSTVENIH rođendana?  Savjet: set()
jedinstveni = set(rodjendani)
print("Jedinstvenih rođendana imamo:", len(jedinstveni))


# c) Postoje li duplikati? Ispiši True/False.
print("Duplikati:", len(rodjendani) != len(set(rodjendani)))


# d) Pomoću rječnika (ili Counter-a) prebroj koliko se puta
#    pojavljuje svaki datum i ispiši SAMO datume koji se ponavljaju.
#    Očekivano:  03-14 -> 2 puta,  07-22 -> 3 puta,  11-05 -> 2 puta
brojac = {}
for datum in rodjendani:
    if datum in brojac:
        brojac[datum] += 1
    else:
        brojac[datum] = 1
for datum, broj in brojac.items():
    if broj > 1:
        print(f"{datum} -> {broj} puta")


# e) BONUS: Koliko je studenata rođeno u martu (mjesec "03")?
#    Savjet: datum[:2] daje mjesec
mart = 0

for datum in rodjendani:
    if datum[:2] == "03":
        mart += 1
print("U martu je rođeno studenata:", mart)
