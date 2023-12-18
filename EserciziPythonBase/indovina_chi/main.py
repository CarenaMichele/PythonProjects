with open("personaggi.txt") as personaggi, open("domande1.txt") as domande1:
    pers=[]
    dom1=[]
    cont=0
    listaTitoli=[]
    valFin=[]
    valTot=[]
    for i in personaggi:
        val = i.strip().split(";")
        if cont==0:
            listaTitoli =val
        if cont>0:
            dizPers={"nome":val[0],"sesso":val[1],"coloreC":val[2],"lunghezzaC":val[3],"occhiali":val[4], "cappello":val[5], "baffi":val[6], "barba":val[7], "pelato": val[8]}
            pers.append(dizPers)
            # valTot.clear()
        cont+=1
    #pers1 = list(pers)
    for i in range(len(list(pers))):
        desired_value = "NO"
        for key, value in list(pers[i].items()):
            if value == desired_value:
                del pers[i][key]


    for i in domande1:
        val = i.strip().split(";")
        dizDom= {"nomeC":val[0]}
        dom1.append(dizDom)
#print(dom1)
valll= []
for i in pers:
    valKeys = i.keys()
    for j in valKeys:
        valll.append(j)
persMod=[]
for i in range(len(dom1)):
    print("MOSSA"+ str(i+1) + " - domanda: "+ dom1[i]["nomeC"] )
    print("personaggi selezionati:")
    if i==0:
        car = dom1[i]["nomeC"].split("=")
        val = car[1]
        for j in range(len(pers)):
            if pers[j]["coloreC"] == val:
                persMod.append(pers[j])
            #print(persMod)
        print(persMod)
    if i==1:
        car = dom1[i]["nomeC"].split("=")
        val = car[1]
        persMod2=[]
        for j in range(len(persMod)):
            if persMod[j]["lunghezzaC"] == val:
                persMod2.append(persMod[j])
            #print(persMod)
        print(persMod2)
    if i==2:
        car = dom1[i]["nomeC"].split("=")
        val = car[1]
        persMod3=[]
        for j in range(len(persMod2)):
            try:
                if persMod2[j]["occhiali"] == val:
                    persMod3.append(persMod2[j])
            except KeyError:
                continue
            #print(persMod)
        print(persMod3)

print("Gioco terminato, hai vinto! E' stato selezionato:")
for i in persMod3:
    print(i)

