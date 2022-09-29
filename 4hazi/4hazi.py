def hanyados(a, b):

    try:

        hanyados = a/b
        print(hanyados)

    except ZeroDivisionError:

        print("Division by zero not allowed")
    
    print("Out of try except blocks")
    

if __name__ == "__main__":

    while True:
        
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))

        hanyados(a, b)