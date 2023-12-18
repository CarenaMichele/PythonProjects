# Esercizio: realizzare una versione semplifica del gioco "campo minato" o "prato fiorito"

# Regole del gioco:
# 1) in un campo da gioco di dimensioni RxC, vengono piazzate N mine in modo casuale
#    (di default, campo 9x9 con 10 mine)
# 2) Il giocatore, ad ogni mossa, seleziona una casella (posizione x,y)
# 3a) Se nella casella selezionata c'è una mina, il giocatore ha perso
# 3b) Altrimenti, viene visualizzato il numero di mine presenti nelle 8 caselle adiacenti
# 4) Quando tutte le caselle senza mine vengono esplorate, il giocatore ha vinto


# Suggerimento: sviluppare delle funzioni per
# 1) piazzare le mine in modo casuale (stampate la matrice solo per verificare che funzioni, poi nascondetela)
# 2) contare il numero di mine adiacenti, data una posizione x,y
# 3) mostrare al giocatore il campo attualmente esplorato (con i contatori nelle celle già visitate)

# L'algoritmo principale si può sviluppare nella funzione main.

# Versione "avanzata": il gioco prevede che, se la cella selezionata non ha mine adiacenti (contatore = 0),
# si visitano automaticamente tutte le celle vicine, fino ad ottenere un perimetro di celle con contatore > 0
# (provate a giocate per capire: https://campo-minato.com/)

#from matrici import stampa_matrice
from random import randint


def main():

    NRIGHE = 9
    NCOLONNE = 9
    NMINE = 10
    campo = crea_campo_minato(NRIGHE, NCOLONNE)
    contatori_mine_adiacenti = crea_matrice_vuota(NRIGHE, NCOLONNE)
    piazza_mine(campo, NMINE)

    hai_perso = False
    hai_vinto = False

    #stampa_matrice(campo)
    #stampa_mine(campo)
    stampa_contatori(contatori_mine_adiacenti)

    print("Inizia la partita!")

    while not hai_vinto and not hai_perso:
        print("Dove vuoi cliccare?")
        riga = int(input("Inserisci riga: "))
        colonna = int(input("Inserisci colonna: "))
        #TODO: verifica l'input!!

        # verifico se l'utente ha beccato una mina
        if(campo[riga][colonna]):
            # ha perso
            print('Hai colpito una mina!')
            print('Partita terminata')
            hai_perso = True
        else:
            mine_adiacenti = conta_mine_adiacenti(campo, riga, colonna)
            contatori_mine_adiacenti[riga][colonna] = mine_adiacenti
            print(f"Mine adiacenti: {mine_adiacenti}")
            stampa_contatori(contatori_mine_adiacenti)

            ## TODO: verifica se hai vinto
            # Suggerimento: mantenere un contatore di caselle visitate (oppure ricavarlo dalla matrice dei contatori)


def crea_campo_minato(nrighe, ncolonne):
    ## Creiamo una matrice di elementi booleani (True = c'è una mina, False = non c'è una mina)
    campo_minato = []
    for i in range(nrighe):
        nuova_riga_vuota = [False] * ncolonne     # riga con tutti gli elementi a False
        campo_minato.append(nuova_riga_vuota)
    return campo_minato


def crea_matrice_vuota(nrighe, ncolonne):
    m = []
    for i in range(nrighe):
        nuova_riga_vuota = [-1] * ncolonne     # riga con tutti gli elementi a False
        m.append(nuova_riga_vuota)
    return m

def piazza_mine(m, nmine):
    ncolonne = len(m[0])
    nrighe = len(m)
    conta_mine = 0

    while conta_mine < nmine:
        colonna = randint(0, ncolonne-1)
        riga = randint(0, nrighe-1)
        # verifica che nella posizione estratta non ci sia una mina, altrimenti piazzala
        #if m[riga][colonna]:
        #    pass
        #else:
        if not m[riga][colonna]:
            m[riga][colonna] = True
            conta_mine = conta_mine + 1

        #print(f'{conta_mine=} {riga=} {colonna=}')
        #stampa_mine(m)


def stampa_mine(m):
    ncolonne = len(m[0])
    nrighe = len(m)
    #stampa prima righa di intestazione
    print('  ', end='')     # spazi iniziali per far posto alla colonna di intestazione
    for i in range(ncolonne):
        print(i,end=' ')
    print()

    #stampa mine
    for i in range(nrighe):
        # colonna di intestazione
        print(i, end=' ')       # numero di riga

        # colonne nella matrice
        for j in range(ncolonne):
            if m[i][j]:
                carattere = '*'
            else:
                carattere = '.'
            print(carattere, end=' ')
        print()


def stampa_contatori(m):
    ncolonne = len(m[0])
    nrighe = len(m)
    #stampa prima righa di intestazione
    print('   ', end='')     # spazi iniziali per far posto alla colonna di intestazione
    for i in range(ncolonne):
        print(i,end='  ')
    print()

    #stampa mine
    for i in range(nrighe):
        # colonna di intestazione
        print(i, end=' ')       # numero di riga

        # colonne nella matrice
        for j in range(ncolonne):
            print(f"{m[i][j]:2d}", end=' ')
        print()



def conta_mine_adiacenti(m, riga, colonna):
    ncolonne = len(m[0])
    nrighe = len(m)

    if riga == 0:
        range_riga = [riga, riga+1]
    elif riga == nrighe-1:
        range_riga = [riga-1, riga]
    else:
        range_riga = [riga-1, riga, riga+1]

    if colonna == 0:
        range_colonna = [colonna, colonna + 1]
    elif colonna == ncolonne - 1:
        range_colonna = [colonna - 1, colonna]
    else:
        range_colonna = [colonna - 1, colonna, colonna + 1]

    contatore = 0
    for i in range_riga:
        for j in range_colonna:
            #if i!=riga and j!=colonna:  # salta elemento centrale
                if m[i][j]:
                    contatore = contatore + 1

    return  contatore


if __name__ == "__main__":
    main()
