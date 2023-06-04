#Fundamentos Comprehencions, Funciones y Manejo de errores

# Creaciopn de graficas

import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}bar.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()


if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [190, 490, 287]

    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)