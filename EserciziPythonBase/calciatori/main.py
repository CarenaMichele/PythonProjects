import csv
from operator import itemgetter
with open('sportivi.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    giocatoreL = []
    for row in csv_reader:
        giocatoreD=dict()
        giocatoreD["goal"] = row[1]
        giocatoreD["dataN"] = row[3]
        giocatoreL.append(giocatoreD)

print()
with open("zodiaco.csv") as csv_zodiaco:
    csv_readerZ = csv.reader(csv_zodiaco,delimiter=",")
    zodiacoL = []
    #dataIn=[]
    #dataFin=[]
    for i in csv_readerZ:
        zodiacoD = dict()
        #dataIn.append(i[1].split("/"))
        #dataFin.append(i[2].split("/"))
        #print(dataIn)
        zodiacoD["segno"] = i[0]
        zodiacoD["dataI"] = i[1]
        zodiacoD["dataF"]  = i[2]
        zodiacoL.append(zodiacoD)

listaDateGiocatori = []
listaGoalGiocatori=[]
data=""
for gioc in giocatoreL:
    data=gioc["dataN"].split("/")
    listaDateGiocatori.append(data[1]+data[0])
    listaGoalGiocatori.append(gioc["goal"])
dataIn=""
dataFin=""
dataIniziale = []
dataFinale=[]
segno=[]
for zod in zodiacoL:
    dataIn= zod["dataI"].split("/")
    dataFin = zod["dataF"].split("/")
    segno.append(zod["segno"])
    dataIniziale.append(dataIn[1]+dataIn[0])
    dataFinale.append(dataFin[1]+dataFin[0])

# print(listaGoalGiocatori)
# print(listaDateGiocatori)
# print(dataIniziale)
# print(dataFinale)
i=0
goals=0
listaFinale= []

for data in range(len(listaDateGiocatori)):
    for dataI in range(len(dataIniziale)):
        if listaDateGiocatori[data] >= dataIniziale[dataI] and listaDateGiocatori[data] <= dataFinale[dataI]:
            #print("segno zodiacale", segno[dataI], "goal segnati", listaGoalGiocatori[data])
            dictFinale = dict()
            dictFinale["segno"] = segno[dataI]
            dictFinale["goal"] = listaGoalGiocatori[data]
            listaFinale.append(dictFinale)
            break
goalA=0
#print(segno)
listaFinale2=[]
for i in range(len(segno)):
    for j in range(len(listaFinale)):
        if listaFinale[j]["segno"]==segno[i]:
            goalA+=int(listaFinale[j]["goal"])
    dictFinale2=dict()
    #print(segno[i] + " ==> " +str(goalA))
    dictFinale2["segno"] = segno[i]
    dictFinale2["goal"] = goalA
    listaFinale2.append(dictFinale2)
    goalA=0

listaFinale2.sort(key=itemgetter("goal"),reverse=True)
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
