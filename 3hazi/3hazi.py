def haromszog(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("A(z)", a,",",b,"és",c,"oldalú háromszög szerkeszthető.")
    else:
        print("A(z)", a,",",b,"és",c,"oldalú háromszög NEM szerkeszthető.")

if __name__ == "__main__":

    print("Adja meg a háromszög 3 oldalát cm-ben:")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))

    haromszog(a, b, c)