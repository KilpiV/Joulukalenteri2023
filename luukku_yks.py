with open("file.txt") as tiedosto:
    eka = 0
    toka = 0

    numerot = "0123456789"
    yhteensa = 0

    for rivi in tiedosto:
        ei_ekaa = True
        for merkki in rivi:
            if merkki in numerot:
                if ei_ekaa:
                    eka = merkki
                    toka = merkki
                    ei_ekaa = False
                else:
                    toka = merkki
        
        luku = int(f"{eka}{toka}")
        yhteensa += luku
print(yhteensa)

        