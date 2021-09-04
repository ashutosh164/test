num = int(input('Enter a number: '))

if num > 1:
    for i in range(2,int(num/2)+1):
        if (num % i) == 0 :
            print(num,'is not a prime number')
            break
    else:
        print(num,'is a prime number')
else:
    print(num,'is not a prime number')

# PRINT FIRST 20 PRIME NUMBER


def is_prime(n):
    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


for n in range(1, 21):
    print(n , is_prime(n))

# CHECK A NUMBER IS PRIME OR NOT


n = int(input('Enter a number: '))


def is_prime():
    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


print(n, is_prime())






