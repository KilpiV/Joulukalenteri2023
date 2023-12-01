with open("file.txt") as tiedosto:
    eka = 0
    toka = 0

    luvut = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0': 0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    yhteensa = 0

    for rivi in tiedosto:
        ei_ekaa = True
        for alku in range(len(rivi)):
            for numero in luvut:
                loppu = alku +len(numero)
                if rivi[alku:loppu] == numero:
                    if ei_ekaa:
                        eka = luvut[numero]
                        toka = eka
                        ei_ekaa = False
                    else:
                        toka = luvut[numero]
        
        luku = int(f"{eka}{toka}")
        yhteensa += luku
print(yhteensa)

        