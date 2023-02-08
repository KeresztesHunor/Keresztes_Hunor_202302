import random


lista: [int] = []


def generalas(db: int):
    for i in range(db):
        lista.append(random.randint(10, 350))


def kiiras():
    print("II/A,B,C:", end="\n\t")
    for i in range(len(lista) - 1):
        print(lista[i], end="#")
    print(lista[len(lista) - 1])


def parosok_szama() -> int:
    parosok_db: int = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            parosok_db += 1
    return parosok_db


def konzol_kiir(parosok_db: int):
    print("II/D,E:\n\tA párosok száma:", parosok_db)


def file_kiir(parosok_db: int):
    f = open("kimutatas.txt", "w", encoding="utf8")
    f.write(f"II/F:\n\tA párosok száma: {parosok_db}")
    f.close()
