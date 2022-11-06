def multiTable(num):
    
    layout = "{:>3}{:>6}" + ("{:>4}" * (num - 1))
    numbers = list(range(1,num + 1))

    print(layout.format("", *numbers))
    print("  :------" + ("----" * (num-1)))

    for i in numbers:
        output = [str(i) + ":"]
        for j in numbers:
            output.append(str(i * j))
        print(layout.format(*output))

def main():
    num = int(input("Lenght of the multiplication table: "))
    multiTable(num)

if __name__ == "__main__":
    main()