import pandas as panda

def main():
    # DataFrame desde diccionario
    personas = {
        'nombre': ['luis', 'mario'],
        'edad': [20, 25]
    }

    tabla = panda.DataFrame(data=personas)

    print(tabla)

    # DataFrame desde Lista de Listas
    data = [['monica', 10], ['maria', 15], ['marieta', 25]]
    columns= ['nombre', 'edad']

    datos = panda.DataFrame(data=data, columns=columns)
    print(datos)

if __name__ == '__main__':
    main()