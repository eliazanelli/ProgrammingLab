file = open('shampoo_sales.csv', 'r')

def sum_csv(file_name):
    sum_value = 0
    for line in file_name:
        elements = line.split(',')
        if elements[0] != 'Date':
            value = float(elements[1])
            sum_value += value
    return sum_value
print("The sum of shampoo sales over yers is: {}".format(sum_csv(file)))