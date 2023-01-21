import random
vel_lista = []
def veletlen_sorozat():
    i = 0
    szoveg = ""
    while i <= 7:
        vel = int(random.random() * 960) - 100
        vel_lista.append(vel)
        if i == 7:
            szoveg += str(vel) + ""
        else:
            szoveg += str(vel) + ";"
        i += 1


    print(f"II/A,B,C:\n \t {szoveg}")

def tizzel_oszthato():
    i = 0
    tiz_oszt_db = 0
    while i < len(vel_lista):
        if (vel_lista[i] % 10 == 0):
            tiz_oszt_db += 1
        i += 1
    return tiz_oszt_db


def konzol_liir():
    print(f"II/D,E\n \t Tízzel osztható számok száma: {tizzel_oszthato()}")

def fajlba_ir():
    fajl = open("vegeredmeny.txt", "w", encoding="utf-8")
    fajl.write(f"II/F\n \t Tízzel oszhtató számok száma: {tizzel_oszthato()}")
    fajl.close()