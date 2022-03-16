file = open('shampoo_sales.csv', 'r')

def sum_csv(file_name):
    if len(file_name.readline()) != 0:
        sum_value = 0
        for line in file_name:
            elements = line.split(',')
            if elements[0] != 'Date':
                value = float(elements[1])
                sum_value += value
    else:
        print("Il file è vuoto")
    return sum_value
print("The sum of shampoo sales over yers is: {}".format(sum_csv(file)))