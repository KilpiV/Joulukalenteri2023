jarjestys = ""

verkko = {}
alotus_solmut = []

with open("file8_1.txt") as tiedosto:
    eka_rivi = True

    for rivi in tiedosto:
        rivi = rivi.strip()
        rivi = rivi.replace("(", "")
        rivi = rivi.replace(")", "")
        if not eka_rivi and rivi != "":
            osat = rivi.split(" = ")
            o_v = osat[1].split(", ")
            verkko[osat[0]] = [o_v[0], o_v[1]]
            if osat[0][2] == "A":
                alotus_solmut.append(osat[0])
        if eka_rivi:
            jarjestys = rivi
            eka_rivi = False
        if rivi == "":
            pass

lopputulos = []
for solmunen in alotus_solmut:

    askeleet = 0
    solmu = solmunen
    indeksi = 0
    while True:
        if solmu[2] == "Z":
            #loppu.append(solmu)
            break
        askeleet += 1
        suunta = jarjestys[indeksi]
        indeksi += 1
        if indeksi == len(jarjestys):
            indeksi = 0
        if suunta == "L":
            solmu = verkko[solmu][0]
        else:
            solmu = verkko[solmu][1]
    lopputulos.append(askeleet)
luvun_tekijat = {}
for luku in lopputulos:
    tekija = 2
    while tekija <= luku:
        while luku % tekija == 0:
            luvun_tekijat[tekija]=1
            luku /= tekija
        tekija +=1
loppusumma = 1
for luku in luvun_tekijat:
    loppusumma = loppusumma*luku
print(loppusumma)
    
