import math

def find_root(a,b,c):
    D=b**2-4*a*c
    if D>0:
        root1=(-b+math.sqrt(D))/(2*a)
        root2=(-b-math.sqrt(D))/(2*a)
        print("two real roots are:",root1,root2)

    elif  D==0:
        root=(-b)/(2*a)
        print("real root is:",root)
    else:
        real=(-b)/(2*a)
        imaginary=math.sqrt(-D)/(2*a)
        print("two complex roots:",real,"+",imaginary,"i and ",real,"-",imaginary,"i")

a=float(input("enter coefficient of a="))
b=float(input("enter coefficient of b="))
c=float(input("enter coefficient of c"))

if a==0:
    print("this is not a quadratic equation")
else:
    find_root(a,b,c)    




    
    
    
    



