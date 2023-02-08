class Jatekos:
    def __init__(self, sor: str):
        adatok: [str] = sor.split(";")
        self.nev: str = adatok[0]
        self.elso: str = adatok[1]
        self.utolso: str = adatok[2]
        self.suly: int = int(adatok[3])
        self.magassag: int = int(adatok[4])
