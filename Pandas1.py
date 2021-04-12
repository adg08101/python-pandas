import numpy as np
import pandas as panda


def main():
    # DataFrame desde diccionario
    personas = {
        'nombre': ['luis', 'mario'],
        'edad': [20, 25]
    }

    tabla = panda.DataFrame(data=personas)

    # print(tabla)

    # DataFrame desde Lista de Listas
    data = [['monica', 10], ['maria', 15], ['marieta', 25]]
    columns = ['nombre', 'edad']

    datos = panda.DataFrame(data=data, columns=columns)
    # print(datos)

    # Desde Lista de Diccionarios

    data = [
        {'name': 'Abdul',
         'age': 115},
        {'name': 'Habat',
         'age': 231},
        {'name': 'Mamet',
         'age': 222},
        {'name': 'Mumot',
         'age': 412},
    ]

    df = panda.DataFrame(data=data)

    # print(df)

    df = panda.DataFrame(np.random.randn(4, 6), columns=['a', 'b', 'c', 'd', 'e', 'f'])
    print(df)

if __name__ == '__main__':
    main()
