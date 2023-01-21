from Lotto import Lotto
lotto_lista = []
def beolvas():
    fajl = open("hatos.txt", "r")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()
    print(sorok)

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        lotto_lista.append(Lotto(sor))
        i += 1
    print(lotto_lista[2].het)


def huzasok_szama():

    return len(lotto_lista)

def elso_huzott_szam_atlag():
    i = 0
    osszeg = 0
    lotto_db = 0
    while i < len(lotto_lista):
        if lotto_lista[i].ev == 2022:
            osszeg += lotto_lista[i].szam1
            lotto_db += 1
        i += 1

    atlag_szamitas = osszeg / lotto_db
    return atlag_szamitas


