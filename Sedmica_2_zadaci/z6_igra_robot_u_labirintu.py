# =============================================================
# ZADATAK 6: IGRA "Robot traži dijamant"   (~25 minuta)
# =============================================================
# Robot se SAM kreće kroz labirint: svakih pola sekunde jedno
# polje naprijed. Strelica pokazuje gdje gleda:  ^  >  v  <
# Cilj: pronaći dijamant ◆ na kraju labirinta.
#
# Pokreni fajl odmah! Robot kreće ravno... i udari u zid,
# jer još nema "mozak". Tvoj zadatak je da ga napišeš:
#
#   NIVO 1: je_zid()              -> senzor koji vidi zid
#   NIVO 2: okreni_desno/lijevo() -> okretanje robota
#   NIVO 3: je_dijamant()         -> senzor koji vidi dijamant
#   NIVO 4: odluci_smjer()        -> mozak: zaobilaženje prepreka
#           4a: robot više ne udara u zid
#           4b: "pravilo desne ruke" -> robot pronalazi dijamant
#   BONUS : MAPA_2 i tvoja vlastita mapa
#

# Pišeš SAMO u DIO 1. DIO 2 (motor igre) ne mijenjaj.
# =============================================================
import os
import sys
import time

# =============================================================
# DIO 1: TVOJ KOD
# =============================================================

# NIVO 1: Senzor za zid
# Vrati True ako na polje (red, kol) robot NE smije stati:
#   - polje je izvan mape (red/kol manji od 0 ili preveliki), ili
#   - na polju je zid "#".
# Inače vrati False.
# Savjet: mapa[red][kol] je znak na polju, len(mapa) je broj redova.
def je_zid(mapa, red, kol):
    if red < 0 or red >= len(mapa):
        return True
    if kol < 0 or kol >= len(mapa[red]):
        return True
    return mapa[red][kol] == "#"


# NIVO 2: Okretanje
# Smjer je jedan znak:  "^" gore,  ">" desno,  "v" dole,  "<" lijevo
# okreni_desno vraća novi smjer nakon okreta za 90° udesno:
#   "^" -> ">",  ">" -> "v",  "v" -> "<",  "<" -> "^"
# okreni_lijevo radi isto, ali ulijevo.
# Savjet: if / elif / else
def okreni_desno(smjer):
    if smjer == "^":
        return ">"
    elif smjer == ">":
        return "v"
    elif smjer == "v":
        return "<"
    else:
        return "^"


def okreni_lijevo(smjer):
    if smjer == "^":
        return "<"
    elif smjer == "<":
        return "v"
    elif smjer == "v":
        return ">"
    else:
        return "^"


# NIVO 3: Senzor za dijamant
# Motor igre poziva ovu funkciju za polje na koje robot upravo
# dolazi. Vrati True ako je na polju (red, kol) dijamant "D".
# Pazi: polje može biti i izvan mape - iskoristi je_zid!
def je_dijamant(mapa, red, kol):
   if je_zid(mapa, red, kol):
       return False
   return mapa[red][kol] == "D"


# NIVO 4: Mozak robota - zaobilaženje prepreka
# Funkcija se poziva prije SVAKOG koraka i vraća smjer u kojem
# robot treba ići. Sada uvijek vraća isti smjer -> robot ide ravno.
#   - polje_ispred(robot, smjer) vraća (red, kol) polja ispred robota
#   - je_zid, okreni_desno, okreni_lijevo si već napisao/la
#
# 4a) DOK je ispred robota zid, okreni ga desno (while petlja).
#     Pokreni: robot više ne udara u zid... ali luta i ne nalazi
#     dijamant prije nego što se isprazni baterija.
#
# 4b) Pravilo desne ruke - robot "drži desnu ruku na zidu":
#     1. ako desno NIJE zid          -> vrati okreni_desno(smjer)
#     2. inače ako naprijed NIJE zid -> vrati smjer
#     3. inače ako lijevo NIJE zid   -> vrati okreni_lijevo(smjer)
#     4. inače (ćorsokak)            -> okreni se nazad
#     Ovako robot UVIJEK pronađe dijamant!
def odluci_smjer(mapa, robot, smjer):

    desno = okreni_desno(smjer)
    red, kol = polje_ispred(robot, desno)
    if not je_zid(mapa, red, kol):
        return desno

    red, kol = polje_ispred(robot, smjer)
    if not je_zid(mapa, red, kol):
        return smjer

    lijevo = okreni_lijevo(smjer)
    red, kol = polje_ispred(robot, lijevo)
    if not je_zid(mapa, red, kol):
        return lijevo

    return okreni_desno(okreni_desno(smjer))


# BONUS: Postavi MAPA = MAPA_2 (dolje u DIO 2) ili nacrtaj svoju mapu.


# =============================================================
# DIO 2: DATI KOD - "motor" igre
# =============================================================
#   #  = zid      .  = slobodno polje
#   S  = start    D  = dijamant

MAPA_1 = [
    "###############",
    "#S..#.....#...#",
    "#.#.#.###.#.#.#",
    "#.#...#...#.#.#",
    "#.#####.###.#.#",
    "#.....#.....#.#",
    "###.#.#####.#.#",
    "#...#.......#D#",
    "###############",
]

MAPA_2 = [
    "#####################",
    "#S....#.......#.....#",
    "#.###.#.#####.#.###.#",
    "#.#...#.#...#...#...#",
    "#.#.###.#.#.#####.###",
    "#.#.....#.#.......#.#",
    "#.#######.#######.#.#",
    "#.......#.#.....#...#",
    "#######.#.#.###.###.#",
    "#.......#...#.....#D#",
    "#####################",
]

MAPA = MAPA_1           # promijeni u MAPA_2 za težu mapu
POCETNI_SMJER = ">"     # robot na startu gleda desno
PAUZA = 0.5             # sekundi između dva koraka
BATERIJA = 200          # najviše koraka

# Smjer robota je ujedno i njegov znak na mapi:
#   ^ gore    > desno    v dole    < lijevo
SMJEROVI = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def polje_ispred(robot, smjer):
    """Vraća (red, kol) polja koje je ispred robota u zadanom smjeru."""
    dr, dk = SMJEROVI[smjer]
    return (robot[0] + dr, robot[1] + dk)


def pronadji(mapa, znak):
    """Vraća (red, kol) prvog polja sa zadanim znakom."""
    for red in range(len(mapa)):
        for kol in range(len(mapa[red])):
            if mapa[red][kol] == znak:
                return (red, kol)
    return None


def prikazi_mapu(mapa, robot, smjer, koraci):
    """Crta mapu: robot je strelica u smjeru kretanja, dijamant je ◆."""
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("\n" * 2)
    for red in range(len(mapa)):
        linija = ""
        for kol in range(len(mapa[red])):
            znak = mapa[red][kol]
            if (red, kol) == robot:
                znak = smjer
            elif znak == "D":
                znak = "◆"
            elif znak in ".S":
                znak = " "
            linija += znak + " "
        print(linija)
    print(f"Koraci: {koraci}/{BATERIJA}")


def cekaj_tipku():
    """Čeka pritisak tipke (u PyCharm konzoli: Enter)."""
    poruka = "Pritisni bilo koju tipku za start..."
    try:
        if sys.stdin.isatty():
            if os.name == "nt":
                import msvcrt
                print(poruka)
                msvcrt.getch()
                return
            import termios
            import tty
            print(poruka)
            fd = sys.stdin.fileno()
            staro = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, staro)
            return
    except Exception:
        pass
    input("Pritisni Enter za start...")


def igraj(mapa):
    robot = pronadji(mapa, "S")
    smjer = POCETNI_SMJER
    koraci = 0

    prikazi_mapu(mapa, robot, smjer, koraci)
    cekaj_tipku()

    while koraci < BATERIJA:
        # 1. Robot (tvoj kod) odlučuje kuda dalje
        smjer = odluci_smjer(mapa, robot, smjer)
        sljedece = polje_ispred(robot, smjer)

        # 2. Fizika igre: ako je tamo zid, robot se razbije
        red, kol = sljedece
        if not (0 <= red < len(mapa) and 0 <= kol < len(mapa[red])) or mapa[red][kol] == "#":
            prikazi_mapu(mapa, robot, smjer, koraci)
            print("BUM! Robot je udario u zid. Kraj igre.")
            return

        # 3. Robot (tvoj kod) provjerava da li je ispred dijamant
        nasao = je_dijamant(mapa, red, kol)

        # 4. Korak naprijed
        robot = sljedece
        koraci += 1
        prikazi_mapu(mapa, robot, smjer, koraci)

        if nasao:
            print(f"BRAVO! Robot je pronašao dijamant u {koraci} koraka!")
            return

        time.sleep(PAUZA)

    print("Baterija je prazna! Robot nije pronašao dijamant.")


if __name__ == "__main__":
    igraj(MAPA)
