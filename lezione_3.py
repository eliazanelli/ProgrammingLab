# from lezione_2 import sum_list

def sum_csv(file_name):
    file = open(file_name, 'r')
    if len(file.readline()) != 0:
        sum_value = 0
        for line in file:
            elements = line.split(',')
            if elements[0] != 'Date':
                value = float(elements[1])
                sum_value += value
    else:
        print("Il file è vuoto")
    file.close()
    return sum_value
print(sum_csv('shampoo_sales.csv'))
# print("The sum of shampoo sales over yers is: {}".format(sum_csv('shampoo_sales.csv')))