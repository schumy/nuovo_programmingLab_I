class CSVFile():
    def __init__(self, name):
        self.name = name

        if not isinstance(name, str):
            print("Mammt!")
            raise TypeError

        try:
            with open(self.name, 'r') as f:
                f.readline()
        except FileNotFoundError:
            print('File non trovato.')

    def get_data(self, start = None, end = None):

        '''my_file = open(self.name, 'r')
        my_list = []
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1].strip()
                my_list.append([date, value])
        my_file.close()
        return my_list'''
        if start == None: start = 0

        with open(self.name, 'r') as f:
            my_list = []

            try:
                for idx, line in enumerate(f):
                    if idx <= end:
                        print(line) #fai quello che facevi prima
                        ...
                    else:
                        return my_list
            except TypeError:

                elements = f.readline(start)
                print(elements)
            #     if elements[0] != 'Date':
            #         date = elements[0]
            #         value = elements[1].strip()
            #         my_list.append([date, value])
            # return my_list

def main():
    file_pth = 'shampoo_sales.csv'
    ogg_csv = CSVFile(file_pth)
    ogg_csv.get_data()

if __name__ == '__main__':
    main()