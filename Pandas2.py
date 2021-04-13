import numpy as np
import pandas as panda
import Pandas

def main():
    """nf = panda.read_excel("persons.xlsx", sheet_name='Sheet_name_1', index_col=0)
    print(nf.groupby(['country']).get_group('cuba').agg(np.max))"""

    datos = {'nombre': ['María', 'Luis', 'Carmen'],
                'edad':[18, 22, 20],
                'Matemáticas': [8.5, 7, 3.5],
                'Economía': [8, 6.5, 5],
                'Programación': [6.5, 4, 9]
             }
    df = panda.DataFrame(datos)
    df1 = df.melt(id_vars=['nombre', 'edad'], var_name='asignatura', value_name='nota')
    print(df1)
    print(df1.pivot(index='nombre', columns='asignatura', values='nota'))


if __name__ == '__main__':
    main()