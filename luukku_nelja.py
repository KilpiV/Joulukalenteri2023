yhteensa = 0
with open("file4_1.txt") as tiedosto:
    for rivi in tiedosto:
        voitto_nrot = []
        omat_nrot = []
        samoja = 0
        rivi = rivi.replace("\n", "")
        rivi = rivi.replace("  ", " ")
        osat = rivi.split(": ")
        rivi = osat[1]
        nrot = rivi.split(" | ")
        v_nrot = nrot[0].split(" ")
        o_nrot = nrot[1].split(" ")
        for nro in v_nrot:
            voitto_nrot.append(int(nro))
        for nro in o_nrot:
            omat_nrot.append(int(nro))
        for nro in voitto_nrot:
            if nro in omat_nrot:
                samoja += 1
        if samoja > 0:
            yhteensa += 2**(samoja-1)
print(yhteensa)