def is_prime(num):
    if  num<=1:
        return False
    for i  in range(2,int(num/2) +1):
        if num%i==0:
            return False
    return True
def generate_prime(n):
    primes=[] 
    for i in range(2,n+1):
        if is_prime(i):
            primes.append(i)
    return primes
n=int(input("enter a number"))

if n<2:
    print("no prime number less than 2.")
else:
    primes=generate_prime(n)
    print("prime numbers upto ",n,"is",primes)    