# Fundamentos Comprehencions, Funciones y Manejo de errores

import utils
import read_csv
import charts

def run():

    data = read_csv.read_csv('data.csv')

    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda item: item['Country/Territory'], data))
    percentages = list(map(lambda item: item['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)


    country = input("Escribe el pais: ")

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
        #charts.generate_pie_chart(labels, values)


if __name__=='__main__':
    run()