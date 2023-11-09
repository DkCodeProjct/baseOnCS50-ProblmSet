acceptedCoin = [20, 10, 15, 5]
ammount = 50
ammountInsert = 0

while ammountInsert < ammount:
    
    getCoin = int(input("putCoin: [valid: $20, $10, $15, $5] "))
    if getCoin in acceptedCoin:
        ammountInsert += getCoin
        remainingAmount = ammount - ammountInsert

        if remainingAmount > 0:
            print(f"Ammount Deu ${remainingAmount}")
        elif remainingAmount == 0:
            print("your payment coomplete!!")
        else:
            change = abs(remainingAmount)
            print(f"Change Ownd: ${change}")
            break
    else:
        print("invalid coin")