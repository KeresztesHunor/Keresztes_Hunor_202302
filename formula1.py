from Jatekos import Jatekos


jatekosok: [Jatekos] = []


def beolvasas():
    f = open("balkezesek.txt", "r", encoding="utf8")
    sorok: [str] = f.readlines()
    for i in range(1, len(sorok)):
        jatekosok.append(Jatekos(sorok[i]))
    f.close()


def jatekosok_szama():
    print("III/A,B:\n\tA balkezes játékosok száma:", len(jatekosok))


def atlagsuly():
    osszeg: int = 0
    for i in range(len(jatekosok)):
        osszeg += jatekosok[i].suly
    print(f"III/C:\n\tA versenyzők átlag súlyértéke: {osszeg / len(jatekosok)} font")


def legmagasabb():
    legmagasabb_indexe: int = 0
    for i in range(1, len(jatekosok)):
        if jatekosok[i].magassag > jatekosok[legmagasabb_indexe].magassag:
            legmagasabb_indexe = i
    print(f"III/D:\n\tA legmagasabb játékos: {jatekosok[legmagasabb_indexe].nev}, magassága: {jatekosok[legmagasabb_indexe].magassag * 2.54} cm.")
