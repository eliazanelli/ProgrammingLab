class Model():

    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        # Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def evaluate(self, data):

        if not self.window_length:
            raise ValueError('Cannot evaluate a model without a window_length set')

        if len(data) <= self.window_length:
            raise ValueError('Evaluation data length ({}) is less or equal to ta window length ({}), cannot evaluate'.format(len(data), window_length))

        # Set empty errors list
        errors = []

        # Loop over all the windows of the data
        for windows_offset in range(len(data) - self.window_length):

            # Define the evaluation data for this window
            evaluation_window_data = data[window_offset:window_offset + self.window_length]

            # Get actual and predicted values
            predicted = self.predict(evaluation_window_data)
            actual = data[self.window_length + window_offset]

            # Add the (absolute) error
            errors.append(abs(actual - predicted))

        # Return the average absolute error
        return sum(errors) / len(errors)


class IncrementModel(Model):

    def __str__(self):
        return 'IncrementModel'

    def check_data(self, data):
        if not isinstance(data, list):
            raise TypeError ('Data "{}" is not a list (got "{}"'.format(data, type(data)))
        else:
            for item in data:
                if not (isinstance(item, int)) or (isinstance(item, float)):
                    raise TypeError('Item "{}" is not of type int or float (got "{}")'.format(item, item.__class__.__name__))
    
    def compute_avg_increment(self, data):

        # Check input list length
        if len(data) <= 1:
            raise ValueError('List is too short')
            
        # Variabile di supporto per il valore precedente
        prev_item = None

        # Preparo una variabile di supporto per calcolare l'incremento medio
        increment = 0

        # Processo i mesi in input su cui fare la predizione
        for item in data:

            # Caloclo l'incremento solo se è definito il "prev_item"
            if prev_item is not None:
                increment += item - prev_item

            # Riassegno la variabile "prev_item" con il valore di "item"
            prev_item = item

        # Calcolo l'incremento medio
        avg_increment = increment / (len(data)-1)

        return avg_increment
    
    def predict(self, predict_data):

        #Check data
        #self.check_data(predict_data)
        
        #Calcolo l'incremento medio sui dati della predict
        self.local_avg_increment = self.compute_avg_increment(predict_data)

        # Torno la predizione (incremento medio sommato all'ultimo valore)
        return predict_data[-1] + self.local_avg_increment
            

class FitIncrementModel(IncrementModel):

    def __str__(self):
        return 'FitIncrementModel'
    
    def fit(self, fit_data):

        #Check data
        #self.check_data(fit_data)
        
        # Calcolo l'incremento medio sui dati di fit
        self.global_avg_increment = self.compute_avg_increment(fit_data)
        
    def predict(self, predict_data):

        #Check data
        #self.check_data(predict_data)
        
        # Chiamo la predict della classe genitore "IncrementModel"
        parent_prediction = super().predict(predict_data)

        # Ora medio l'incremento del fit con quello della predict
        prediction_increment = (self.global_avg_increment + self.local_avg_increment) / 2

        # Torno la predizione (incremento medio sommato all'ultimo valore)
        return predict_data[-1] + prediction_increment

#=========================================#
#        Corpo del programma              #
#=========================================#

# Mini-dataset di test
test_fit_data = [8,19,31,41]
test_predict_data = [50,52,60]

# Test rapido su IncrementModel (non unit test in questo caso)
increment_model = IncrementModel()
prediction = increment_model.predict(test_predict_data) 
if not prediction == 65:
    raise Exception('IncrementModel sul dataset di test non mi torna 65 ma "{}"'.format(prediction))
else:
    print('IncrementModel test passed')

# Test rapido su FitIncrementModel (non unit test in questo caso)
fit_increment_model = FitIncrementModel()
fit_increment_model.fit(test_fit_data)
prediction = fit_increment_model.predict(test_predict_data)
if not prediction == 68:
    raise Exception('FitIncrementModel sul dataset di test non mi torna 68 ma "{}"'.format(prediction))
else:
    print('FitIncrementModel test passed')

# Linea vuota
print('')

# I dati delle mie vendite di shampoo
shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

# Definisco quanti mesi usare per la valutazione che verranno sottratti al dataset nel caso del fit
eval_months = 12
cutoff_month = len(shampoo_sales) - eval_months

evaluate_data = shampoo_sales[25:-1]

# Istanzio nuovo modello senza fit
increment_model = IncrementModel()

# Istanzio nuovo modello con fit
fit_increment_model = FitIncrementModel()
# Fitto sui dati fino al mese di cutoff
fit_increment_model.fit(shampoo_sales[0:cutoff_month])

# Metto entrambi i modelli in una lista
models = [increment_model, fit_increment_model]

for model in models:
    increment_model_mean_error = increment_model(evaluate_data)
