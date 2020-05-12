def prime(num):
    if num <= 1:
        return False
    elif num % 1 == 0 and num % num == 0 and num % 2 == 0:
        return False
    elif num % 1 == 0 and num % num == 0:
        return True

def output():
    num = int(input("Enter an integer to find out if it is prime: "))
    if prime(num):
        print("The integer is prime.")
    else: 
        print("The integer is not prime.")


if __name__ == "__main__":
    output()


""" Main idea (brainstorming)

def prime(num):
    num = int(input("Enter a number greater than 1 to find out if it is a prime number. "))
    if num % 1 == 0 and num % num == 0 and num % 2 == 0:
        print("False.")
    elif num % 1 == 0 and num % num == 0:
        print("True.")

prime(num)

"""