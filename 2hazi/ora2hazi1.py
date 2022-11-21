def betuk_gyak(mondat):

    betuk_dict = {}

    for i in range(len(mondat)):
        if mondat[i] != ' ':
            if mondat[i] not in betuk_dict:
                betuk_dict[mondat[i]] = 1
            else:
                betuk_dict[mondat[i]] += 1
        else:
            continue
    print(betuk_dict)

def fordito(mondat):
    print(mondat[::-1])

def szavakl(mondat):

    szlista = mondat.split(' ')
    print(szlista)
    
if __name__ == "__main__":

    mondat = input("Adjon meg egy mondatot: ")

    print("Betűk gyakorisága: ")
    betuk_gyak(mondat)

    print("Fordítva: ")
    fordito(mondat)
    
    print("Listába rendezve szavanként: ")
    szavakl(mondat)

