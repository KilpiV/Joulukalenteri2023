with open("luukku2_1.txt") as tiedosto:
    pelinro = 0
    pun = 12
    vihr = 13
    sini = 14
    
    yhteensa = 0

    for rivi in tiedosto:
        mahdollinen = True
        pelinro += 1
        rivi = rivi.replace("\n","")
        rivi = rivi.replace(": ",":")
        rivi = rivi.replace("; ",";")
        rivi = rivi.replace(", ",",")
        pelin_osat = rivi.split(":")
        kierrokset = pelin_osat[1].split(";")
        for kierros in kierrokset:
            osat = kierros.split(",")
            for osa in osat:
                osaset = osa.split(" ")
                vari = osaset[1]
                if vari == "green":
                    if int(osaset[0]) > vihr:
                        mahdollinen = False
                elif vari == "blue":
                    if int(osaset[0]) > sini:
                        mahdollinen = False
                elif vari == "red":
                    if int(osaset[0]) > pun:
                        mahdollinen = False
        if mahdollinen:
            yhteensa += pelinro
print(yhteensa)

        