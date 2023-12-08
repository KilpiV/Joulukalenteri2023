jarjestys = ""

verkko = {}

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
        if eka_rivi:
            jarjestys = rivi
            eka_rivi = False
        if rivi == "":
            pass
    pass

askeleet = 0
solmu = "AAA"
indeksi = 0
while True:
    if solmu == "ZZZ":
        break
    askeleet += 1
    suunta = jarjestys[indeksi]
    indeksi += 1
    if indeksi == len(jarjestys):
        indeksi = 0
    if suunta == "L":
        solmu = verkko[solmu][0]
        #print("oikea", solmu)
    else:
        solmu = verkko[solmu][1]
        #print("vasen", solmu)
print(askeleet)
    
