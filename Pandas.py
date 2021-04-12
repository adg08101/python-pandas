import pandas as pd

def view(s):
    print(s)
    print('Items:', s.size, 'Index:', s.index,'Type:', s.dtype)
    print('\n')

def main():
    l = ['Mate', 'Fisics', 'Programming']
    d = {1: 'Yo', 2: 'Tu', 3: 'El', 4: 'Ellos', 5: 'Nosotros'}
    sl = pd.Series(data=l)
    dl = pd.Series(data=d)
    view(sl)
    view(dl)


if __name__ == '__main__':
    main()
