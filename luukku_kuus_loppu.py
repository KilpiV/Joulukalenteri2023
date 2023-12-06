#tiedot = [(71530),(940200)]
tiedot = [58996469, 478223210191071]
yhteensa = 1
luku = 0
for i in range(tiedot[0]+1):
    matka = i*(tiedot[0]-i)
    if matka> tiedot[1]:
        lisaa = (tiedot[0]+1)-(2*(i))
        yhteensa *= lisaa
        break
        
print(yhteensa)
