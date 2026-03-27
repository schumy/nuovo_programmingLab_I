#ESERCIZIO 1
#Scrivete una funzione che sommi tutti gli elementi di una lista
def somma_lista(lista):
    tot = 0

    for el in lista:
        tot += int(el)

    return tot

#ESERCIZIO 2
#Scrivere una funzione che prende in input una stringa e ritorna True se è un
#palindromo, False altrimenti.
def palindromo(stringa):
    contrario = stringa[-1: :-1]    #Inverte la stringa e la salva in una var
    if stringa == contrario:
        return True
    else:
        return False
    
#ESERCIZIO 3
#Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di
#A[i] con A[j].
def scambia(lista, i, j):

    #salvo gli elementi degli indici scelti in variabili copia   
    for idx, el in enumerate(lista):
        if (idx == i):
            copia_i = lista[i]
        
        if (idx == j):
            copia_j = lista[j]
    
    #scambio gli elementi
    lista[i] = copia_j
    lista[j] = copia_i

    #metodo più veloce
    #lista[i], lista[j] = lista[j], lista[i]
    
#ESERCIZIO 4
#Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno
#almeno un elemento in comune
def comune(lista_1, lista_2):
    for i in lista_1:
        if i in lista_2:    #il ciclo for lo fa in automatico
            return True
    return False

#ESERCIZIO 5
#Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una
#lista di stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] -
#>["uno","zero","sette","nove","otto"]
def converti(lista):
    #lista convertita
    conv = []

    dizionario = {0: 'zero',
                  1: 'uno',
                  2: 'due',
                  3: 'tre',
                  4: 'quattro',
                  5: 'cinque',
                  6: 'sei',
                  7: 'sette',
                  8: 'otto',
                  9: 'nove'}
    
    for el in lista:
        conv.append(dizionario[el])

    return conv


def main():
    #ES 1
    # lista = [1, 2, 3, 4]
    # somma = somma_lista(lista)(
    # print(somma)

    #ES 2
    # stringa = input("Scrivi la stringa: ")
    # if palindromo(stringa):
    #     print("La stringa è palindroma.")
    # else:
    #     print("La stringa non è palindroma.")

    #ES 3
    #controllo sulla lista
    # lista = []
    # add = ""

    # #popolo la lista
    # print("Per uscire dal ciclo scrvere 'break'.")
    # while(True):

    #     add = input("Inserisci elemento lista: ")

    #     if add == "break":
    #         print(f"La lista è: {lista}")
    #         break

    #     lista.append(add)

    # #controllo indici
    # indice_1 = 0
    # indice_2 = 0

    # print("Scrivi gli indici che vuoi invertire.\n")

    # while(True):
    #     indice_1 = int(input("Indice 1: "))
    #     if (indice_1 < len(lista)) and (indice_1 >= 0):
    #         while(True):
    #             indice_2 = int(input("Indice 2: "))
    #             if (indice_2 < len(lista)) and (indice_2 >= 0):
    #                 break
    #             else:
    #                 print("Il numero scelto è troppo grande o minore di 0.")
    #         break
    #     else:
    #         print("Il numero scelto è troppo grande o minore di 0.")

    # scambia(lista, indice_1, indice_2)
    # print(f"Ecco la lista invertita: {lista}")

    #ES 4
    # lista_1 = [1, 2, "ciao", 4, 5]
    # lista_2 = [0, 6, 7, 8, "ciao"]

    # if comune(lista_1, lista_2):
    #     print("Hanno un elemento in comune.")
    # else:
    #     print("Non hanno elementi in comune.")

    #ES 5
    #popola la lista
    lista = []
    numeri_permessi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Per uscire scrivere un numero diverso da 0-9.")

    while(True):
        add = int(input("Aggiungi numero: "))

        if add not in numeri_permessi:
            break
        else:
            lista.append(add)

    lista_convertita = converti(lista)
    print(f"Ecco la lista corrispondente: {lista_convertita}")

if __name__ == "__main__":
    main()