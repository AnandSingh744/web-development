def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n/2)+1):
       if n%i==0:
           return False
    return True
n=int(input("enter a number:"))

if is_prime(n):
   print(n,"is a prime number")
else:
    print(n,"isn't a prime number")




# def check_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n/2)+1):
#         if n%i==0:
#             return False
#     return True  
# n=int(input("enter a number:"))  
# if check_prime:
#     print(n,"is a prime number")
# else:
#    print(n,"isn't a prime number")   
    