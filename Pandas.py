import pandas as pd


def main():
    l = ['Mate', 'Fisics', 'Programming']
    d = {1: 'Yo', 2: 'Tu', 3: 'El', 4: 'Ellos', 5: 'Nosotros'}
    sl = pd.Series(data=l, dtype='string')
    dl = pd.Series(data=d)
    print(sl)
    print(dl)


if __name__ == '__main__':
    main()
