import random


def bekeres():
    print("I/A:")
    r_nev: str = input("\tRendező neve: ")
    f_cim: str = input("\tFilm címe: ")


def pontozas():
    pont: int = random.randint(0, 10)
    print("I/B:\n\tPontozás (0-10):", pont)
    if pont < 4:
        print("\tGyenge film.")
    elif pont < 8:
        print("\tÉrdemes megnézni!")
    else:
        print("\tKihagyhatatlan film!")
