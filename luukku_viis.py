seeds = []
soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
locattion = []

kaikki = [seeds, soil, fertilizer, water, light, temperature, humidity, locattion]

seurattavat = []
rivi_nro = 0
indeksi = 0

eka_rivi = True
nimi_rivi = False
tyhja_rivi = False
tieto_rivi = False

with open("file5testi.txt") as tiedosto:
    for rivi in tiedosto:
        #rivi_nro += 1
        if tieto_rivi:
            if rivi == "\n":
                # laske uudet arvot???
                tyhja_rivi = True
                tieto_rivi = False
            else:
                rivi = rivi.replace("\n", "")
                osat = rivi.split(" ")
                #print(osat, indeksi)
                kaikki[indeksi].append((int(osat[0]), int(osat[1]), int(osat[2])))
                print(kaikki[indeksi])
            
        if nimi_rivi:
            rivi = rivi.replace("\n", "")
            print(rivi, "nimi_rivi")
            nimi_rivi = False
            tieto_rivi = True
        if tyhja_rivi:
            indeksi += 1
            tyhja_rivi = False
            nimi_rivi = True
        if eka_rivi:
            #vaihdetaan tokaan osaan...
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(": ")
            rivi = rivi[1].split(" ")
            for luku in rivi:
                seurattavat.append(int(luku))
            seurattavat.sort()
            print("eka rivi", seurattavat)
            tyhja_rivi = True
            eka_rivi = False
        if rivi_nro == 1:
            print(rivi)
        else:
            pass
    print("päästy eteenpäin")
#        while rivi != "\n":
 #           print("testi")
  #          pass
        #for rivi in tiedosto:

         #   if rivi == "\n":
          #      print("vaihtuu osa")
    pass