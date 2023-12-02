with open("luukku2_1.txt") as tiedosto:
    
    yhteensa = 0

    for rivi in tiedosto:
        mahdollinen = True
        rivi = rivi.replace("\n","")
        rivi = rivi.replace(": ",":")
        rivi = rivi.replace("; ",";")
        rivi = rivi.replace(", ",",")
        pelin_osat = rivi.split(":")
        kierrokset = pelin_osat[1].split(";")
        
        pienin_pun = 0
        pienin_sin = 0
        pienin_vihr = 0

        for kierros in kierrokset:
            osat = kierros.split(",")
            for osa in osat:
                osaset = osa.split(" ")
                vari = osaset[1]
                luku = int(osaset[0])
                if vari == "green":
                    if pienin_vihr < luku:
                        pienin_vihr = luku
                elif vari == "blue":
                    if pienin_sin < luku:
                        pienin_sin = luku
                elif vari == "red":
                    if pienin_pun < luku:
                        pienin_pun = luku

        pienin_tulo = pienin_pun*pienin_sin*pienin_vihr
        yhteensa += pienin_tulo
print(yhteensa)

        