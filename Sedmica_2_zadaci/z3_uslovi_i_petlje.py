# =============================================================
# ZADATAK 3: Uslovi i petlje   (~10 minuta)
# =============================================================
import random

# a) Korisnik unese broj bodova (0-100). Ispiši ocjenu:
#      0-54 -> 5,  55-64 -> 6,  65-74 -> 7,
#      75-84 -> 8, 85-94 -> 9,  95-100 -> 10

bodovi = int(input("Unesi broj bodova(0-100): "))
if 0 <= bodovi <= 54:
    print("Ocjena: 5")
elif bodovi <=64:
    print("Ocjena: 6")
elif bodovi <= 74:
    print("Ocjena: 7")
elif bodovi <= 84:
    print("Ocjena: 8")
elif bodovi <= 94:
    print("Ocjena: 9")
elif bodovi <= 100:
    print("Ocjena: 10")
else:
    print("Neispravan broj bodova!")


# b) Pomoću for petlje izračunaj sumu svih PARNIH brojeva od 1 do 100.
#    (Rezultat treba biti 2550)

suma = 0

for broj in range( 1, 101):
    if broj % 2 == 0:
        suma += broj

print("Suma parnih brojeva je: ", suma)


# c) MINI IGRA "Pogodi broj"
#    Računar zamisli broj od 1 do 20 (već napisano ispod).
#    Pomoću while petlje traži od korisnika da pogađa dok ne pogodi.
#    Nakon svakog pokušaja ispiši "Više!" ili "Manje!".
#    Na kraju ispiši iz koliko pokušaja je pogodio.
tajni_broj = random.randint(1, 20)

pokusaj = 0
pogodak = 0

while pogodak != tajni_broj:
    pogodak = int(input("Pogodi broj od 1 do 20: "))
    pokusaj += 1

    if pogodak < tajni_broj:
        print("Više!")
    elif pogodak > tajni_broj:
        print("Manje!")
    else:
        print(f"Bravo! Pogodili ste iz {pokusaj} pokušaja.")