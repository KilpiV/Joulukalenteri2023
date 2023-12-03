
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

for i in range(len(matriisi)):
    for j in range(len(matriisi[0])):
        if matriisi[i][j] == "*":
            eka_loytynyt = False
            toka_loytynyt = False
            numero_loytynyt = False
            eka = ""
            toka = ""
            luvut = []
            paikat = []
            for k in range(-1, 2):
                for h in range(-1, 2):
                    if (i+k) < len(matriisi[0]) and (j+h) < len(matriisi):                    
                        if (i+k) > -1 and (j+h) > -1:
                            
                            if matriisi[i+k][j+h] in numerot:
                                numero_loytynyt = True
                                eka = ""
                                l=0
                                while matriisi[i+k][j+h-l] in numerot:
                                    l += 1
                                l -= 1
                                paikat.append((i+k,j+h-l))
                                while matriisi[i+k][j+h-l] in numerot:
                                    eka += str(matriisi[i+k][j+h-l])
                                    l -= 1
                                    if j+h-l == len(matriisi[0]):
                                        break
                                luvut.append(int(eka))
            
            if len(luvut) > 0:
                lisays_tehty = False
                eri_luvut = False
                loytynyt = False
                eka_luku = luvut[0]
                eka_paikka = paikat[0]
                lisays = 0
                for paikka in paikat:
                    if eka_paikka != paikka:
                        loytynyt = True
                if loytynyt:
                    for luku in luvut:
                        if  eka_luku != luku and not lisays_tehty:
                            lisays = eka_luku*luku
                            lisays_tehty = True
                            eri_luvut = True
                    if not eri_luvut:
                        lisays = eka_luku*eka_luku
                        lisays_tehty = True
                yhteensa += lisays

print(yhteensa)