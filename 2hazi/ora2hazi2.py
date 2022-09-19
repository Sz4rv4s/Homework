def atvalto(szam, merterkegyseg):

    if mertekegyseg == 'cm':
        print(szam*2.54, 'inches')

    elif mertekegyseg == 'inch':
        print(szam/2.54), 'cm'

    else:
        print('Not correct unit!')

if __name__ == "__main__":
    szam = int(input("Adjon meg egy számot és egy mérétkegységet (cm/inch): \n"))
    mertekegyseg = input("")

    atvalto(szam, mertekegyseg)

