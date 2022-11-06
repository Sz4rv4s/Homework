def is_palindrome(word):
    special_letters = ["cs", "dz", "ly", "ty", "ny", "zs", "sz", "gy",]
    letters = []
    reverse = ""

    for i in range(len(word)):
        letters.append(word[i])

    for i in range(len(letters)-1):
        if letters[i]+letters[i+1] in special_letters:
            letters[i], letters[i+1] = letters[i+1], letters[i]
    for i in range(len(letters)-2):
        if letters[i] + letters[i+1] + letters[i+2] == "dzs":
            letters[i], letters[i+2] = letters[i+2], letters[i]
    

    for i in letters[::-1]:
        reverse += i
    
    if word == reverse:
        print("Is polindrome.")
    else:
        print("Isn't polindrome.")

def main():

    word = input("Type your word here: ")
    is_palindrome(word)

if __name__ == "__main__":

    main()