
def het_ora_ert():
    het_napja = input("Hét napja: ")
    ora_nev = input("Óra neve: ")
    ertekeles = int(input("Értékelés: (1-5): "))

    if ertekeles < 0:
        print("Az értékelés nem lehet negatív!")
    elif ertekeles > 5:
        print("5 pont feletti értékelés nem elfogadható!")
    elif ertekeles == 0:
        print("Nem lehet 0 az értékelés!")
    else:
        print("Köszönjük az értékelést!")

    print("I/A, B:")
    print(f"\t Hét napja:{het_napja}\n \t Óra neve:{ora_nev}\n \t Értékelés:{ertekeles}")
    print("I/C Köszönjük az értékelést!")
