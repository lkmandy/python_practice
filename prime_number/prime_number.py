# Check whether an integer is a prime number or not

def is_prime(value):
    if value > 1:
        # check for factors
        for i in range(2, value):
            if (value % i) == 0:
                print(value, "is not a prime number")
                break
        else:
            print(value, "is a prime number")
    # if input number is less than or equal to 1, it is not prime
    else:
        print(value, "is not a prime number")


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    is_prime(number)