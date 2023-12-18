import operator


def main():
    listaTot=[]
    with open("glucometers.txt") as info:
        try:
            for i in info:
                val = i.strip().split()
                dizioTot={"codice":val[0], "orario":val[1], "glicemia":int(val[2]), "temperatura":val[3], "frequenza":val[4]}
                listaTot.append(dizioTot)
        except FileNotFoundError:
            print("file non esistente")
    valSuperamento = 200
    listaSuperamenti=[]
    listaCodice=[]
    for i in range(len(listaTot)):
        if listaTot[i]["glicemia"]>=valSuperamento:
            listaSuperamenti.append(listaTot[i])
            listaCodice.append(listaTot[i]["codice"])
    listaSuperamenti.sort(key=operator.itemgetter("codice"))
    cont=0
    conteggi=[]
    listaCod=set(listaCodice)
    for j in listaCod:
        for i in range(len(listaSuperamenti)):
            if listaSuperamenti[i]["codice"] == j:
                cont+=1
        conte={"codice":j, "conteggio":cont}
        conteggi.append(conte)
        cont=0
    conteggi.sort(key=operator.itemgetter("conteggio"),reverse=True)
    for i in range(len(conteggi)):
        for j in range(len(listaSuperamenti)):
            if listaSuperamenti[j]["codice"]== conteggi[i]["codice"]:
                print(listaSuperamenti[j]["codice"]+ " " + listaSuperamenti[j]["orario"]+ " " +str(listaSuperamenti[j]["glicemia"]))
if __name__ == "__main__":
    main()

