def destroy():
    with open("D:/Homework/9hazi/hazi.txt", "r", encoding="UTF-8") as file:

        lines = list(line for line in (l.strip() for l in file) if line)

    mgh = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű', 'y']
    irj = ['.', ',', '-', '!', '"', '?', '!', '(', ')']

    to_destroy = []
    to_write = ""

    for i in range(0, len(lines), 3):
        to_destroy.append(lines[i])

    for sor in range(len(to_destroy)):
        for karakter in range(len(to_destroy[sor])):
            if to_destroy[sor][karakter] not in mgh and to_destroy[sor][karakter] not in irj:
                to_write += to_destroy[sor][karakter]
    
    with open("D:/Homework/9hazi/kimenet.txt", "w", encoding="UTF-8") as file:
        file.write(to_write)

def main():
    destroy()

if __name__ == "__main__":
    main()