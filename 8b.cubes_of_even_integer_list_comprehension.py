def cube_of_even_integer(n):
    return[i**3 for i in n if type(i)==int and i%2==0]
n=[1,2,3,4,5,6,'hello','7','8']
k=cube_of_even_integer(n)
print(k)