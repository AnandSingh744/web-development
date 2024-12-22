def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True    
def generate_firstprime(n):
    primes=[]
    num=2
    while len(primes)<n:
        if is_prime(num):
            primes.append(num)
        num+=1
    return primes   
n=int(input("enter the number "))

if n<=0:
    print("please enter positive number")
else:
    primes=generate_firstprime(n)
    print("first",n,"prime numbers are :",primes)    
