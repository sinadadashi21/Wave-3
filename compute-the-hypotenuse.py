import math
sideA = float(input("Enter side length of side A (cm): "))
sideB = float(input("Enter side length of side B (cm): "))

def hyp(sideA, sideB):
    hypotenuse = math.sqrt(math.pow(sideA, 2) + math.pow(sideB, 2))
    print("The hypotenuse is equal to", hypotenuse, "cm")


hyp(sideA, sideB)
