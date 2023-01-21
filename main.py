import ertekel
import sorozat
import hatoslotto

#ertekel.het_ora_ert()
sorozat.veletlen_sorozat()
sorozat.tizzel_oszthato()
sorozat.konzol_liir()
sorozat.fajlba_ir()

hatoslotto.beolvas()
print(f"III/A,B\n \t A húzások száma: {hatoslotto.huzasok_szama()}")
print(f"III/C\n \t A 2022-ben húzott számok átlag: {hatoslotto.elso_huzott_szam_atlag():.2f}")
