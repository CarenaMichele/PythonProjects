nascita = "06/07/2002"
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
print(convertiroreData(nascita))
