import random as rm

class Errore(Exception):
    pass

def formattazione(word):
    if word.endswith(r'\\n'):
        word = word[0:-3]
        return word
    return word


class Coin():

    def __init__(self, materiale):
        self.faccia = ""
        self.materiale = materiale

    def __str__(self):
        return f"La faccia è: {self.faccia}."

    #Quando viene lanciata la moneta cambia la faccia
    def lancio(self):
        numero = rm.randint(0,1)

        if numero == 0:
            self.faccia = "Testa"
        else:
            self.faccia = "Croce"
        
        print(f"E' uscito: {self.faccia}")

#Scrivete una classe denominata Veicolo che disponga di questi attributi dati:
# ● modello (per il modello del veicolo);
# ● marca (per la marca del veicolo);
# ● anno (per l'anno del veicolo).
# ● speed (per la velocità del veicolo)
# E di questi metodi:
# ●
# __
# init__ che accetti come argomenti l’anno, il modello, e la marca. Il metodo dovrebbe inoltre
# assegnare 0 all’attributo dati speed.
# ● __str__ che restituisce una stringa con i dettagli del veicolo (marca, modello, anno e velocità)
# ● accellerare che aggiunge 5 all’attributo dati speed ogni volta che viene chiamato.
# ● frenare che sottrae 5 dall’attributo dati speed ogni volta che viene chiamato.
# ● get_speed che restituisce la velocità corrente.
class Veicolo:

    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return f"--- Dati ---\nMarca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}\nVelocità: {self.speed}"

    def accelerare(self):
        self.speed += 5

    def frenare(self):
        if self.speed == 0:
            print("Sei gia fermo!")
        else:
            self.speed -= 5 


    def get_speed(self):
        return self.speed

#ESERCIZIO 2
# Crea una sottoclasse auto di veicolo che ha in aggiunta l'attributo
# numero_porte e cambia il metodo _str__ di conseguenza
# Crea una sottoclasse moto che ha in aggiunta l'attributo tipo (ad esempio,
# "Sportiva" o "Touring") e cambia il metodo _str__ di conseguenza
class Auto(Veicolo):

    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    #nfjadnvdsabvndskl
    def __str__(self, marca, modello, anno):
        Veicolo().__str__(self, marca, modello, anno)
        return f"Numero porte: {self.numero_porte}"

# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
# 2) abbia un attributo “name” che ne contenga il nome
# 3) abbia un metodo“get_data()” che torni i dati dal file CSV come lista di liste,
# ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
class FileCVS():
    def __init__(self, file_pth, name):

        #provo a leggere il file
        try:
            with open(file_pth, 'r') as f:
                f.readline()

        #il file non viene trovato
        except FileNotFoundError:
            print("L'oggetto è stato inizializzato a None.")
            print('Il file inserito non è stato trovato!') 
            self.name = name
            self.file_pth = None
        
        #se esiste
        else:
            self.name = name
            self.file_pth = file_pth
        
    def get_data(self):

        lista_dati = []
        with open(self.file_pth) as file:
                
            #popolo la lista dati come lista di liste
            for row in file:
                lista_tmp = row.strip().split(',')
                lista_dati.append(f"{lista_tmp}")

            return lista_dati
        
# Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che
# converta automaticamente a numero float tutte le colonne tranne la prima (della data).
# Chiamate la get_data originale con super().get_data(), poi converite tutto a float.
# A questo punto, aggiungete a mano questi due campi al file “shampoo_sales.csv”:
class NumericalCSVfile(FileCVS):

    #converte tutta la lista in float se può farlo
    def get_data(self):
        lista = super().get_data()

        print(type(lista))
        for lis in lista:
            print(type(lis))
        # for idx, el in enumerate(lista[1:]):
        #     riga = el.split(',')
        #     print(riga)
            # for idx, dato in enumerate(el):
            #     try:
            #         if idx != 0:
            #             print(f'{idx}: {dato}')
            #             #dato = float(dato)
            #         else:
            #             pass
            #     except ValueError:
            #         print(el)
            #         lista.remove(el)


# Scrivete una definizione di una classe di nome Canguro con i metodi
# seguenti:
# 1. Un metodo
# lista vuota.
# __
# init__ che inizializza un attributo lista contenuto_tasca con paramatro di default
# 2. Un metodo di nome intasca che prende un oggetto di qualsiasi tipo e lo inserisce in
# contenuto_tasca.
# 3. Un metodo __str__ che restituisce una stringa di rappresentazione dell’oggetto Canguro e dei
# contenuti della tasca.
# ● Provate il codice creando due oggetti Canguro, assegnandoli a variabili di
# nome can e guro, e aggiungendo elementi a can. 
class Canguro():
    def __init__(self, contenuto_tasca = None):
        if contenuto_tasca == None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = contenuto_tasca

    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)

    def __str__(self):
        return f"Il canguro ha: {self.contenuto_tasca}"

def main():
    ...
    # #Prove per Coin
    # moneta = Coin("Oro")
    # print(moneta.faccia, moneta.materiale)
    # moneta.materiale = "Argento"
    # print(moneta.materiale)
    # print(moneta)

    # moneta.lancio()

    #Auto
    #auto = Veicolo("Audi", "A4", "2015")
    
    CSVFile = NumericalCSVfile("shampoo_sales.csv", 'Shampoo')
    print(CSVFile.get_data())

    # can = Auto("Audi", "A4", "2015", 5)
    # print(can)

if __name__ == "__main__":
    main()