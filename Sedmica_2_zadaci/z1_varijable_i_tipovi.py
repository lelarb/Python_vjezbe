# =============================================================
# ZADATAK 1: Varijable, unos i aritmetika   (~7 minuta)
# =============================================================

# a) Napiši program koji pita korisnika za ime i godinu rođenja,
#    a zatim ispiše poruku oblika:
#       "Zdravo Amra, ove godine puniš 21, a 2030. ćeš imati 25 godina."
#    Savjet: input() vraća tekst -> koristi int()

TRENUTNA_GODINA = 2026
ime = input("Unesite svoje ime: ")
godina_rodjenja = int(input("Unesite godinu rodjenja: "))

godine = TRENUTNA_GODINA - godina_rodjenja
godine_2030 = 2030 - godina_rodjenja

print(f"Zdravo {ime}, ove godine puniš {godine}, a 2030. ćeš imati {godine_2030} godina.")


# b) Korisnik unese broj sekundi (npr. 3725).
#    Ispiši koliko je to sati, minuta i sekundi:
#       "3725 s = 1 h 2 min 5 s"
#    Savjet: koristi // (cjelobrojno dijeljenje) i % (ostatak)

sekunde = int(input("Unesite broj sekundi: "))

sati = sekunde // 3600
minute = (sekunde % 3600) // 60
ostatak = sekunde % 60

print(f"{sekunde}s = {sati}h {minute}min {ostatak}s")
