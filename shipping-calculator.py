items = int(input("Enter the number of items to be shipped: "))
holder = items - 1
first = items - holder

def shipping(items): 
    if items == 1:
        cost = 10.95 * 1
        print("The cost of shipping will be $" + str(round(cost,2)))
    elif items > 1:
        cost = first * 10.95 + holder * 2.95
        print("The cost of shipping will be $" + str(round(cost,2)))

shipping(items)

