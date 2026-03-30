#-----------FUNZIONI--------------

#ESERCIZIO 1
#Scrivere una funzione che prende una lista di parole e restituisce un dizionario con il
#conteggio delle occorrenze.
def occorrenze(lista):
    dizionario = dict()

    for word in lista:
        word = word.title()

        if word not in dizionario:
            dizionario[word] = 1
        else:
            dizionario[word] += 1
    
    return dizionario

#ESERCIZIO 2
#Definire una funzione che sommi tutti i valori delle vendite degli shampoo del file
#passato come argomento
def vendite(file):
    tot = float()

    with open('shampoo.csv', 'r') as file:
        for row in file:
            linea = row.split(',')

            #controllo che non sia l'intestazione
            if linea[0] != 'Date':
                tot += float(linea[1])

    return tot

#ESERCIZIO 3
#Definire una funzione che prende in input un file ed una parola e conta quante volte
#quella parola è presente sul file
#da implementare con le regex
def conta_parola(file, parola):
    count = 0

    with open(file, 'r') as file:
        for row in file:
            linea = row.split()

            for word in linea:
                if word.lower() == parola.lower():
                    count += 1
    return count

#ESERCIZIO 4
#Definire una funzione conteggio che prende come input un file e ritorna un dizionario
#con chiave le parole e valore il numero di volte che la parola è presente nel file.
def conteggio(file):
    dizionario = dict()

    with open(file, 'r') as file:
        for row in file:
            linea = row.split()

            for word in linea:
                if word.lower() not in dizionario:
                    dizionario[word.lower()] = 1
                else:
                    dizionario[word.lower()] += 1

    return dizionario

#ESERCIZIO 5
#Definire una funzione che prende come input un file, rimuove tutte le righe duplicate,
#scrive il risultato in un nuovo file chiamato unique.txt.
def del_duplicate(file):
    nuovo_file = open("unique.txt", 'a') #se uso w riscrive il contenuto del file nel caso esista, se uso a aggiunge in coda
    prec = []

    with open(file, 'r') as file:
        for row in file:
            
            if row == prec:
                prec = row
            else:
                nuovo_file.write(row)
                prec = row
    nuovo_file.close()

def main():
    ...
    # #ES 1
    # lista = ['ciao', 'mondo', 'Ciao']
    # dizionario = occorrenze(lista)
    # print(dizionario)

    #ES 2
    # file = 'shampoo.csv'
    # tot = vendite(file)
    # print(f"Il totale delle vendite è: {tot}€.")

    #ES 3
    # #da implementare con le regex
    # file = "Foglio1.py"
    # tot = conta_parola(file, 'tot')
    # print(tot)

    #ES 4
    #implementare regex e ordinamento
    # file = "Foglio1.py"
    # dizionario = conteggio(file)
    
    # for key in dizionario:
    #     print(f"{key}: {dizionario[key]}")

    #ES 5
    file = "shampoo.csv"
    del_duplicate(file)

if __name__ == "__main__":
    main()
