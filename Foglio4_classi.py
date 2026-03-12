import random as rm

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

# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
# 2) abbia un attributo “name” che ne contenga il nome
# 3) abbia un metodo“get_data()” che torni i dati dal file CSV come lista di liste,
# ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
class FileCVS():
    def __init__(self, file_pth):
        self.name = file_pth
        self.file_pth = file_pth

    def get_data(self):
        lista_dati = []

        with open(self.file_pth) as file:
            
            #popolo la lista dati come lista di liste
            for row in file:
                lista_tmp = row.split(',')

                lista_dati.append(f"{lista_tmp}")

        return lista_dati

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
    
    CSVFile = FileCVS("shampoo.csv")
    print(CSVFile.get_data())


if __name__ == "__main__":
    main()