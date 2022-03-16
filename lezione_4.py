class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista = []
        file = open(self.name, 'r')
        for line in file:
            elements = line.split(',')
            if elements[0] != 'Date':
                elements[1] = elements[1][0:-1]
                lista.append(elements)
        return lista

# File = CSVFile('shampoo_sales.csv')
# print(File.get_data())
            