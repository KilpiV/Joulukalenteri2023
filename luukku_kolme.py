
numerot = "0123456789"
piste = "."
matriisi = []
yhteensa = 0

with open("luukku3_1.txt") as tiedosto:
    for rivi in tiedosto:
        mat_rivi = []
        rivi = rivi.replace("\n", "")
        for merkki in rivi:
            mat_rivi.append(merkki)
        matriisi.append(mat_rivi)

#print(matriisi)
rivi_nro = 0
sarake_nro = 0
numero_kelpaa = False
numeron_alku = rivi_nro, sarake_nro
matriisi_leveys = len(matriisi[0])
for rivi in matriisi:
    numero = ""
    numero_alkanut = False
    sarake_nro = -1
    for merkki in rivi:
        sarake_nro += 1
        if not numero_alkanut:
            numeron_alku = rivi_nro, sarake_nro
        if merkki in numerot:
            numero_alkanut = True
            numero += merkki

        numero_kelpaa = False
        if numero_alkanut:
            if merkki not in numerot or sarake_nro == matriisi_leveys-1:
#        if (merkki not in numerot and numero_alkanut) or :
                kohta = [numeron_alku[0],numeron_alku[1]]
                if numeron_alku[0] == 0:
                    alku_rivi = numeron_alku[0]
                else:
                    alku_rivi = numeron_alku[0]-1
                if numeron_alku[0] == len(matriisi)-1:
                    lop_rivi = numeron_alku[0]
                else:
                    lop_rivi = numeron_alku[0]+1

                if numeron_alku[1] == 0:
                    alku_sar = numeron_alku[1]
                else:
                    alku_sar = numeron_alku[1]-1
                if numeron_alku[1]+len(numero) == matriisi_leveys:
                    lop_sar = numeron_alku[1]+len(numero)
                else:
                    lop_sar = numeron_alku[1]+len(numero)+1
                #print(alku_rivi, lop_rivi, "-", alku_sar, lop_sar, "-numero:", numero)
                for i in range(alku_rivi, lop_rivi+1):
                    for j in range(alku_sar, lop_sar):
                        
                        tutki = str(matriisi[i][j])
                        if tutki not in numerot and tutki not in piste:
                            numero_kelpaa = True
                        if numero_kelpaa:
                            break
                    if numero_kelpaa:
                        break
                if numero_kelpaa:
                    yhteensa += int(numero)
                
                numero = ""
                numero_alkanut = False
    rivi_nro += 1
print(yhteensa)