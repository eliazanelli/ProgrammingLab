#==============================
#  Classe per file CSV
#==============================

class CSVFile():

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError ('Il nome del file non è una stringa')
            
        self.name = name
        self.can_read_file = True

    def get_data(self, start=None, end=None):
        
        # Inizializzo una lista vuota per salvare tutti i dati
        data = []
        
        if start is None:
            start = 0
        if end is None:
            end = -1
        
        try:
            # Apro il file
            file = open(self.name, 'r')
            lines = [line for line in file]
            
            # Leggo il file linea per linea
            for line in lines[start:end]:
                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')

                # Se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                    elements[-1] = elements[-1][0:-1]
                    
                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)
            
            # Chiudo il file
            file.close()
            
        except FileNotFoundError:
            
            # Il file non può essere aperto o non è illeggibile
            self.can_read_file = False
            print('Errore di Ricerca File: "{}" non è presente nella directory'.format(self.name))
            
        except Exception as e:

            # Errore generico
            print('Ho ottenuto un errore generico: "{}"'.format(e))

        # Quando ho processato tutte le righe, restituisco i dati
        return data


#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):

    def get_data(self, *args, **kwargs):

        # Chiamo la get_data del genitore 
        string_data = super().get_data(*args, **kwargs)

        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []

        # Ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:
            try:
                # Converto a float tutti gli elementi della riga tranne il primo. Ma se fallisco, stampo l'errore e passo alla riga successiva.
                string_row[-1] = float(string_row[-1])
                numerical_data.append(string_row)
            except Exception as e:
                # La stringa non è convertibile in stringa 
                print('Errore di Valore: "{}"'.format(e))
                pass
        return numerical_data

#pippo = CSVFile(3)
#print(pippo.get_data())

#pippo = CSVFile('pippo.csv')
#print(pippo.get_data())

#shampoo_sales = CSVFile('shampoo_sales.csv')
#print(shampoo_sales.get_data())

shampoo_sales = CSVFile('shampoo_sales.csv')
print(shampoo_sales.get_data())

numerical_shampoo_sales = NumericalCSVFile('shampoo_sales.csv')
print(numerical_shampoo_sales.get_data())

shampoo_sales = CSVFile('shampoo_sales.csv')
print(shampoo_sales.get_data(5, 4))

numerical_shampoo_sales = NumericalCSVFile('shampoo_sales.csv')
print(numerical_shampoo_sales.get_data(5, 4))