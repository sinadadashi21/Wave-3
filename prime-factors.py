n = int(input("Enter an integer (2 or greater): "))
print("The prime factors of" , n , "are:")

def factorization(n):
    factor = 2
    if n <= factor:
        print("The integer must be equal to or greater than 2.")
    while factor<= n:
        if n % factor == 0:
            n = n / factor
            print(int(factor))
        else:
            factor = factor + 1

factorization (n)