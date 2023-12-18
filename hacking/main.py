with open("prodotti.txt") as prodotti,open("acquisti.txt") as acquisti:
    listaProdotti=[]
    listaAcquisti=[]
    for prod in prodotti:
        val=prod.strip().split()
        prodo={"id_prodotto":val[0], "id_rivenditore":val[1]}
        listaProdotti.append(prodo)
    for acq in acquisti:
        val=acq.strip().split()
        acqui={"id_prodottoC":val[0], "id_rivenditoreC":val[1]}
        listaAcquisti.append(acqui)
contSospetto=0
for i in range(len(listaProdotti)):
    for j in range(len(listaAcquisti)):
        if listaAcquisti[j]["id_prodottoC"]==listaProdotti[i]["id_prodotto"]:
            if listaAcquisti[j]["id_rivenditoreC"]!=listaProdotti[i]["id_rivenditore"]:
                contSospetto+=1
                listaProdotti[i]["rivSosp"] = listaAcquisti[j]["id_rivenditoreC"]
    if contSospetto==1:
        listaProdotti[i]["sospetto"]=True
    else:
        listaProdotti[i]["sospetto"]=False
    contSospetto=0
print(listaProdotti)
print("Elenco transazioni sospette:")
cont=0
for i in range(len(listaProdotti)):
    if listaProdotti[i]["sospetto"]==True:
        print(f"codice Prodotto: {listaProdotti[i]['id_prodotto']}")
        print(f"Rivenditore ufficiale: {listaProdotti[i]['id_rivenditore']}")
        for j in range(len(listaAcquisti)):
            if listaAcquisti[j]["id_prodottoC"] == listaProdotti[i]["id_prodotto"]:
                if cont==0:
                    print("lista Rivenditori:", end="")
                cont+=1
                print(f"{listaAcquisti[j]['id_rivenditoreC']}\t", end="")
        print()
        cont=0
