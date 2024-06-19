#
#   Solving this after finish cs50P, its been 3,4 months.. 
#   and i could come up with much more simple and efficent solution
#
ammout = 50
pay = 0
validCoin = [5,10,15]


while ammout > pay:
    get = int(input('> '))
    if get in validCoin:
        pay += get
    else:
        print('invalid')

    if pay >= ammout:
        change = pay  - ammout
        print(f'change:{change}')
    else:
        need = ammout - pay
        print(f'Need:{need}')
        continue


"""
// 7 MONTHS AGO SOLUTION

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
"""