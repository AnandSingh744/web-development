def validate_name(n):
    for char in n:
        if any(char.isdigit() or not char.isalpha() and char!=" " for char in n):
            raise ValueError("unvalid name. ")
    return True
try:
    n=input("enter your name:")

    if validate_name(n):
        print("valid name:",n)
except ValueError as e:
    print("error:",e)            
