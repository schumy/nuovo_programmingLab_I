class ExamExeption(Exception):
    pass

class MovingAvarege():

    def __init__(self, winlen):
        try: 
            if (winlen > 0) and (type(winlen) == int):
                self.winlen = winlen
            else:
                raise ExamExeption('La lunghezza deve essere un intero strettamente positivo')
            
        except TypeError:
            raise ExamExeption('La lunghezza deve essere un intero strettamente positivo')

    def compute(self, lista):
        if self.winlen >= len(lista): raise ExamExeption('Lista troppo corta.')
        try:
            '''Definisco le variabili che uso'''
            curr = 0
            media_mobile = []

            '''controllo tipo dati lista'''
            '''controllo se winlen > lista'''

            while(curr + self.winlen <= len(lista)):
                lista_tmp = [num for num in lista[curr:curr+self.winlen]]
                media_mobile.append(sum(lista_tmp)/self.winlen)
                curr += 1
            
            return media_mobile
        
        except TypeError:
            raise ExamExeption('Gli rgomenti della lista non sono numeri')

def main():
    lista = [2, 4, 8, 16]
    
    prova = MovingAvarege(5)
    result = prova.compute(lista)
    print(result)

if __name__ == '__main__':
    main()