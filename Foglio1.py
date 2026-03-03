#ESERCIZIO 1
#Stampare l’equivalente di 538 minuti nel formato 8h:58min.


def converti_ora():
    tot = int(input("Quanti minuti? "))
    ore = int(tot/60)
    min = int(tot%60)

    print(f"{tot} minuti sono: {ore}h:{min}min.")

#converti_ora()

#ESERCIZIO 2
#Scrivere un programma che chiede all’utente un numero intero e stampa il suo quadrato e il suo cubo.

def quadrato_cubo():
    x = int(input("Inserisci un intero da elevare: "))
    quadrato = x**2
    cubo = x**3

    print(f"Il quadrato di {x} è {quadrato}.\nIl cubo di {x} è {cubo}.")

#quadrato_cubo()

#ESERCIZIO 3
#Scrivere un programma che verifica se un numero inserito dall’utente è pari o dispari.

def pari_dispari():
    x = int(input("Inserisci numero: "))

    if (x%2 == 0):
        print("Il numero è pari.")
    else:
        print("Il numero è dispari.")

# pari_dispari()

#ESERCIZIO 4
#Definire una funzione che prende come argomento una parola e una lettera e ritorna quante volte
#quella lettera è contenuta nella parola.

def conta_lettera(parola, lettera):
    count = 0
    lettera = lettera.lower()

    for a in parola:
        if lettera == a.lower():
            count += 1

    return count

#parola = input("Inserisci parola: ")
#lettera = input("Che lettera vuoi contare? ")

#tot = conta_lettera(parola, lettera)
#print(tot)

'''
for idx, item in enumerate(parola):
    print(idx, item)

    restituisce da solo l'indice
'''

#ESERCIZIO 5
#Scrivere un programma che verifica se un numero inserito dall’utente è primo.

def is_prime():
    num = int(input("Inserisci numero: "))
    divisore = 2
    verifica = 0

    while(divisore < num/2):
        if (num % divisore) == 0:
            verifica = 1

        divisore += 1

    if (verifica == 1):
        print("Il numero non è primo.")
    else:
        print("Il numero è primo.")

#is_prime()

#ESERCIZIO 6 
#Scrivere un programma che fa la somma di n numeri inseriti dall’utente. Di all'utente di scrivere 0 per
#fermarsi.

def somma_inf():

    x = -1
    tot = 0

    print("Quando vuoi fermarti scrivi 0")

    while(x != 0):
        x = int(input("Inserisci numero: "))
        tot += x

    print(f"La somma è: {tot}")
    #return tot

#somma_inf()


#ESERCIZIO 7
#Definire la funzione fattoriale (versione iterativa).

def fattoriale():
    x = int(input("Inserisci numero: "))
    fattore = 1
    tot = 1

    while(fattore <= x):
        tot *= fattore
        fattore += 1
    
    print(f"Il fattoriale di {x} è {tot}")

#fattoriale()

#ESERCIZIO 8
#Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un
#triangolo e, se sì, di che tipo di triangolo.

#restituisce il maggiore di tre 
def maggiore(a, b, c):
    if (a >= b and a >= c):
        return a
    if (b >= a and b >= c):
        return b
    return c
 
def triangolo(a, b, c):
    #triangolo eqilatero
    if (a == b and b == c):
        return print("Il triangolo è eqilatero.")
    
    #triangolo isoscele
    if (a == b or b == c or c == a):
        return print("Il triangolo si può fare ed è isoscele.")
    
    #t. scaleno
    x = maggiore(a,b,c)
    #verifica
    if ((a + b + c - x) > x):
        return print("Il triangolo si può fare ed è scaleno")
    else:
        return print("Non si può creare nessun triangolo con questi lati.")

#a = int(input("Primo lato: "))
#b = int(input("Secondo lato: "))
#c = int(input("Terzo lato: "))
#triangolo(a, b, c)
    
#ESERCIZIO 9
#Definire una funzione che conta quante vocali sono presenti in una stringa.

def conta_vocali():
    stringa = input("Stringa: ")
    vocali = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in stringa:
        for vocale in vocali:
            if letter.lower() == vocale:
                count += 1

    print(count)

conta_vocali()