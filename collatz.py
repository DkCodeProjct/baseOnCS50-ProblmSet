def main():
    getGmailAdress = input("Enter Gmial_ADRESS: ")
    if isValid(getGmailAdress):
        
        filipMenu = {
            "Kottu" : 12.88,
            "Wade"  : 14.99,
            "Rice"  : 15.99,
            "Taco"  : 18.50,
            "Burito" : 19.88,
        }

        totalAmount = 0
        
        while True:
            try:
                print("WelCome To Filip Menu..",)
                item = input("Oreder: ").title()
                if item in filipMenu:
                    totalAmount += filipMenu[item]
                    print("total : ", end="")
                    print("{:.2f}".format(totalAmount))
            except EOFError:
                print()
                break
    else:
        print("invlaid Gamil Adress")
def isValid(n):
    if n[0].isalpha() == False or n[1].isalpha() == False:
        return False
    if len(n) >= 2 and len(n) <= 6:
        return True
    i = 0
    while i < len(n):
        if n[0].isalpha() == False:
            if n[2] == "0":
                return False
            else:
                break
    i += 1

    for char in n:
        if char not in [" ", ",", "?", "#"]:
            return False
    return True

if __name__ == "__main__":
    main()