import math

import pandas as pd

def view(s):
    print(s)
    print('Items:', s.size, 'Index:', s.index,'Type:', s.dtype)
    print('\n')

def properties(s = None):
    l = {
        'count()': 'Devuelve el número de elementos que no son nulos ni NaN en la serie s',
        'sum()': '''Devuelve la suma de los datos de la serie s cuando los datos son de un tipo numérico, o
                    la concatenación de ellos cuando son del tipo cadena str.''',
        'cumsum()': '''Devuelve una serie con la suma acumulada de los datos de la serie s cuando los datos
                    son de un tipo numérico.''',
        'value_counts()': '''Devuelve una serie con la frecuencia(número de repeticiones) de
                            cada valor de la serie s''',
        'min()': 'Devuelve el menor de los datos de la serie s.',
        'max()': 'Devuelve el mayor de los datos de la serie s.',
        'mean()': 'Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico.',
        'std()': 'Devuelve la desviación típica de los datos de la serie s cuando los datos son de un tipo numérico.',
        'describe()': '''Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo,
                        el máximo, la media, la desviación típica y los cuartiles.'''
    }

    i = 1

    for k in l:
        oper = 's.' + k
        ke = list(l.keys())
        print(str(i) + '.', str(ke[i - 1]).upper(), l[k], ': \nResulted\n'
        if l[k].find('una serie') != -1 else ': Resulted\t', eval(oper))
        i += 1
        print('\n')

def get_pos(s, p):
    print(s[p])
    print('\n')

def main():
    """l = ['Mate', 'Fisics', 'Programming']
    d = {'Mat': 6.0,  'Eco': 4.5, 'Pro': 8.5}
    sl = pd.Series(data=l, dtype='string')
    dl = pd.Series(data=d)
    view(sl)
    get_pos(sl, 0)
    # get_pos(sl, '0:2')
    view(dl)
    get_pos(dl, 0)
    get_pos(dl, ['Pro', 'Eco'])
    properties(dl)"""

    l = [
        # chr(i) for i in range(97, 123)
        i for i in range(1, 20)
    ]

    ls = pd.Series(l)
    # print(ls)

    # print(ls)
    ls = ls.apply(math.log)

    # print(ls[ls > 2])

    print(ls[ls > 2].sort_index(ascending=False))

    print('\n', ls.values)
    # print(ls.apply(str.upper))


if __name__ == '__main__':
    main()
