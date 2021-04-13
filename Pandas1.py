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

    df = panda.DataFrame(np.random.randn(4, 6), columns=['a', 'b', 'c', 'd', 'e', 'f'])
    df.to_excel("output.xlsx", sheet_name='Sheet_name_1')

    nf = panda.read_excel("output.xlsx", sheet_name='Sheet_name_1', index_col=0)
    print(nf)
    print(properties(nf))

def properties(s = None):
    l = {
        'info()' : '''Devuelve información (número de filas, número de columnas, índices, tipo de las columnas y'
                      memoria usado) sobre el DataFrame df.''',
        'shape' : 'Devuelve una tupla con el número de filas y columnas del DataFrame df.',
        'size' : 'Devuelve el número de elementos del DataFrame.',
        'columns' : 'Devuelve una lista con los nombres de las columnas del DataFrame df.',
        'index' : 'Devuelve una lista con los nombres de las filas del DataFrame df.',
        'dtypes' : 'Devuelve una serie con los tipos de datos de las columnas del DataFrame df.',
        # 'head(n)' : 'Devuelve las n primeras filas del DataFrame df.',
        # 'tail(n)' : 'Devuelve las n últimas filas del DataFrame df.'
    }

    i = 1

    for k in l:
        oper = 's.' + k
        print(str(i) + '.', l[k], ': \nResulted\n'
        if l[k].find('una serie') != -1 else ': Resulted\t', eval(oper))
        i += 1
        print('\n')
if __name__ == '__main__':
    main()
