import csv
import operator


def convertiroreData(data):
    sequenza = list(data)
    for i in sequenza:
        if i == "/":
            sequenza.remove(i)
    temp = sequenza[2:4]
    sequenza[2:4] = sequenza[0:2]
    sequenza[0:2] = temp
    anno = "".join(sequenza)
    return anno[0:4]

with open("sportivi.csv","r", encoding="utf-8") as testo:
    sportivi = csv.reader(testo)
    listaCalciatori = []
    for riga in sportivi:
        calciatore = {"nome" : riga[0], "goal" : riga[1], "nazionalità":riga[2], "nascita":riga[3]}
        listaCalciatori.append(calciatore)
    for riga in listaCalciatori:
        riga["nascita"] = convertiroreData(riga["nascita"])
    # print(listaCalciatori)
    with open("zodiaco.csv","r",encoding="utf-8") as documento:
        zodiaco = []
        for segno in documento:
            #qui ho usato un dizionario al posto di una semplice lista, poi ho messo tutto in una lista successivamente
            dizionarioZ={}
            val = segno.strip().split(",")
            dizionarioZ={"segnoZ":val[0], "dataI":val[1], "dataF":val[2]}
            zodiaco.append(dizionarioZ)
        for segno in range(len(zodiaco)):
            zodiaco[segno]["dataI"] = convertiroreData(zodiaco[segno]["dataI"])
            zodiaco[segno]["dataF"] = convertiroreData(zodiaco[segno]["dataF"])
# print(zodiaco)
print(listaCalciatori)
print(zodiaco)
listaFinale=[]
for giocatore in range(len(listaCalciatori)):
    for segno in range(len(zodiaco)):
        if (zodiaco[segno]["dataI"]) <= (listaCalciatori[giocatore]["nascita"]) <= (zodiaco[segno]["dataF"]):
            #qui non ti prendeva tutti i goal di tutti i calciatori ma solo gli ultimi del giro
            #per semplificare, ogni volta che trovo una data tra le due, vado a creare un nuovo dizionario con all'interno
            #il segno e il goal di quel giocatore. Quindi in questa lista di dizionari avrò ancora dei duplicati nei segni zodiacali
            # zodiaco[segno]["goal"]=listaCalciatori[giocatore]["goal"]
            dictFinale = dict()
            dictFinale["segno"] = zodiaco[segno]["segnoZ"]
            dictFinale["goal"] = listaCalciatori[giocatore]["goal"]
            listaFinale.append(dictFinale)
            break
print(listaFinale)

goalA=0
#print(segno)
listaFinale2=[]
#qui infine sommo semplicemente i goal dei segni zodiacali uguali
for i in range(len(zodiaco)):
    for j in range(len(listaFinale)):
        if listaFinale[j]["segno"]==zodiaco[i]["segnoZ"]:
            goalA+=int(listaFinale[j]["goal"])
    dictFinale2=dict()
    #print(segno[i] + " ==> " +str(goalA))
    dictFinale2["segno"] = zodiaco[i]["segnoZ"]
    dictFinale2["goal"] = goalA
    listaFinale2.append(dictFinale2)
    goalA=0
print(listaFinale2)


listaFinale2.sort(key=operator.itemgetter("goal"),reverse=True)
for i in range(len(listaFinale2)):
    if i==0:
        ValAsterischi = listaFinale2[i]["goal"]/50
    numAsterischi = int(listaFinale2[i]["goal"]/ValAsterischi)
    num=""
    for j in range(numAsterischi):
        num+="*"
    if len(listaFinale2[i]["segno"]) >7:
        print(listaFinale2[i]["segno"] + "\t(" + str(listaFinale2[i]["goal"]) + ")\t" + num)
    else:
        print(listaFinale2[i]["segno"] + "\t\t(" + str(listaFinale2[i]["goal"]) + ")\t" + num)
    num=""
# for giocatore in listaCalciatori:
#     for segno in zodiaco:
#         if int(segno[1]) < int(giocatore["nascita"]) < int(segno[2]):
#             segno.append(giocatore["goal"])
#
# print(zodiaco)
# for segno in zodiaco:
#     for i in range(len(segno)-1):
#         if i == 1:
#             segno.pop(i)
#         elif i == 2:
#             segno.pop(i)
# print(zodiaco)





# listaFinale = []                #ha dentro solo i nomi dei segni zodiacali
# for riga in zodiaco:
#     for campo in range(len(riga)):
#         if campo == 0:
#             listaFinale.append(riga[campo])

# for riga in zodiaco:
#     for campo in riga:
#         print(campo)
#         if campo == {}:
#             print("a")
#
#         # if campo == 3:
#         #     for chiavi in riga[campo]:
#         #         if chiavi == "goal":
#         #             print(riga[campo][chiavi])
# #                     somma = somma + int(riga[campo][chiavi])
# #                 somma = 0
# # zodiaco.append(somma)
# # print(zodiaco)
#
#
#
#
#
#
#
#
