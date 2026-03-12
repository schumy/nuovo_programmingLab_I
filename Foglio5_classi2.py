#ESERCIZIO 1
class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print(f"Ciao sono {self.ruolo}, {self.nome} {self.cognome}")
        
class Studente(Persona):
    def __init__(self, nome, cognome, corsi_frequentati = list()):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi_frequentati = corsi_frequentati

    def saluta(self):
        print(f"{self.nome} frequenta: ")
        for corso in self.corsi_frequentati:
            print(f"  -{corso}")

    '''
    per ogni corso frequentato (self.corsi_frequentati)

    '''
    def sono_insegnati(self):
        tutti_insegnati = 0

        for corso in self.corsi_frequentati:
            check = 0
            #prof è key
            for prof in Professore.lista_professori.values():
                if corso in prof:
                    check = 1
            if check == 0:
                print(f"{corso} non è insegnato da nessuno!")
                tutti_insegnati = 1

        if tutti_insegnati == 0:
            print("Tutti i corsi hanno un professore.")
        # if all(corso in Professore.lista_professori.values() for corso in self.corsi_frequentati):
        #     print("Sei un genio!")
        

class Professore(Persona):

    lista_professori = dict()

    def __init__(self, nome, cognome, corsi_insegnati):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi_insegnati = corsi_insegnati
        self.lista_professori[f"{self.cognome} {self.nome}" ] = corsi_insegnati

    def saluta(self):
        print(f"{self.nome} insegna: ")
        for corso in self.corsi_insegnati:
            print(f"  -{corso}")

    #verifica se un professore insegna in tutti i corsi frequentati da uno studente
    def confronta_corsi(self, corsi_studente):
        #per ogni elemento in corsi studente è in corsi insegnati, ritorna true se sono tutti veri
        if all(elemento in self.corsi_insegnati for elemento in corsi_studente): 
            print("Il professore insegna tutti i corisi di questo studente.")

#ESERCIZIO 2
# Crea una sottoclasse auto di veicolo che ha in aggiunta l'attributo
# numero_porte e cambia il metodo _str__ di conseguenza
# Crea una sottoclasse moto che ha in aggiunta l'attributo tipo (ad esempio,
# "Sportiva" o "Touring") e cambia il metodo _str__ di conseguenza
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

#sottoclasse Auto
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)  #serve per prendere gli attributi dalla super-classe
        self.numero_porte = numero_porte

    def __str__(self):
        return f"--- Dati ---\nMarca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}\nNumero di porte: {self.numero_porte}\nVelocità: {self.speed}"

#sottoclasse Moto
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f'\nTipo: {self.tipo}'
    
def main():
    ...
    # ogg_auto = Moto('Audi', 'a4', 2014, 'touring')
    # print(ogg_auto)

    corsi_alberto = ['Analisi 2', 'Fisica', 'Divano 1']
    
    ogg_alberto = Studente("Alberto", "Lo Bue", corsi_alberto)
    ogg_alberto.saluta()

    corsi_francesco = ['Analisi 2', 'Analisi 1', 'Algebra lineare', 'Probabilità']
    ogg_francesco = Professore("Francesco", "Candido", corsi_francesco)
    ogg_francesco.confronta_corsi(ogg_alberto.corsi_frequentati)

    corsi_piero = ['Chimica', 'Fisica', 'Analisi 2']
    ogg_piero = Professore("Piero", "Del Grosso", corsi_piero)

    ogg_alberto.sono_insegnati()

if __name__ == "__main__":
    main()