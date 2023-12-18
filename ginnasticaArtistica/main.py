import operator
with open("punteggi.txt","r") as punteggiFile:
    risultati=[]
    for i in punteggiFile:
        info={}
        val=i.strip().split(" ")
        info={"nome":val[0],"cognome":val[1],"sesso":val[2],"nazione":val[3],"punteggi":sorted(val[4:])}
        risultati.append(info)
classificaDonne=[]
punteggi=[]
risultati.sort(key=operator.itemgetter("punteggi"), reverse=True)
punteggi=[]
puntTotali=[]
nazioni=[]
for i in risultati:
    dizionario={}
    dizionario={"nazione":i["nazione"], "punteggio":sum(list(map(float,i["punteggi"][1:4])))}
    puntTotali.append(dizionario)
    nazioni.append(dizionario["nazione"])
    if i["sesso"] == "F":
        punteggi.append(sum(list(map(float,i["punteggi"][1:4]))))
PunteggioVincitrice=max(punteggi)
for i,v in enumerate(range(len(punteggi))):
    if punteggi[v] == PunteggioVincitrice:
        occorrenza= i
        break;
print(f"la vincitrice è: {risultati[occorrenza]['nome']} {risultati[occorrenza]['cognome']}, {risultati[occorrenza]['nazione']} - Punteggio:{PunteggioVincitrice}")
print()
nazioniUniche= list(set(nazioni))
classificaFinalePunteggio=[]
punteggioo=0
for i in range(len(nazioniUniche)):
    for j in range(len(puntTotali)):
        if puntTotali[j]["nazione"]== nazioniUniche[i]:
            punteggioo+=puntTotali[j]["punteggio"]
            #print(punteggioo)
    dizionarioFinale={}
    dizionarioFinale={"nazione":nazioniUniche[i],"punteggio":punteggioo}
    classificaFinalePunteggio.append((dizionarioFinale))
    punteggioo=0
classificaFinalePunteggio.sort(key=operator.itemgetter("punteggio"), reverse=True)
print("Classifica complessiva nazioni:")
for i in range(3):
    print(str(i)+"°)"+classificaFinalePunteggio[i]["nazione"] + " - Punteggio totale:" + str(classificaFinalePunteggio[i]["punteggio"]))



