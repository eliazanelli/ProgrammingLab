class CSVFile:

    def __init__(self, file_name):
        self.name = file_name

    def get_data(self):
        lista = list()
        file = open(self.name, 'r')
        for line in file:
            if line.startswith('Date'):
                pass
            else:
                elements = line.split(',')
                elements[1] = str(float(elements[1]))
                lista.append(elements)
        return lista

File = CSVFile('shampoo_sales.csv')
print(File.get_data())
            