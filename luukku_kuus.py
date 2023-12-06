#tiedot = [(7,9), (15, 40), (30, 200)]
tiedot = [(58, 478), (99, 2232), (64, 1019), (69, 1071)]
yhteensa = 1
for tieto in tiedot:
    luku = 0
    for i in range(tieto[0]+1):
        matka = i*(tieto[0]-i)
        if matka> tieto[1]:
            lisaa = (tieto[0]+1)-(2*(i))
            yhteensa *= lisaa
            break
        
print(yhteensa)
