nutrtion = [
    {"fruit" : "apple", "callorie" : 25},
    {"fruit" : "banana", "callorie" : 10},
    {"fruit" : "mango", "callorie" : 12}
]
fruitName = False

checkCal = input("item: ")
for fruit in nutrtion:
    if fruit['fruit'] in checkCal:
        print(f"calloreis:{fruit['callorie']}")
        fruitName = True
        break
if not fruitName:
    print("invalid")