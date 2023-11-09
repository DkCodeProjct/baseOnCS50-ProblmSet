def main():
    while True:
        getPassword = input("enter:_ ")
        
        if getPassword.isdigit():
            verifiedPsswrd = int(getPassword)
            
            if 5 < verifiedPsswrd < 10:
                getName = input("entrTheName:_ ")
                result = snakeCaseName(getName)
                print(result)
                break
            print("incorrectPassword>>")
        
        else:
            print("ivnalidInput<<")

def snakeCaseName(name):
    snakeCase = ""
    for char in name:
        if char.isupper():
            snakeCase += "_" + char.lower()
        else:
            snakeCase += char
    
    returnCaseName = snakeCase.lstrip()
    return f"logginSuccess/ {returnCaseName}"
if __name__ == "__main__":
    main()