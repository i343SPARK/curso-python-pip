#Fundamentos Comprehencions, Funciones y Manejo de errores

# Leer archivos csv

import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    path = './data.csv'
    read_csv(path)
    print(read_csv(path)[0])