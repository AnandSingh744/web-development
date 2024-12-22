def cube_even_integer(n):
    cubes=[]
    for i in n:
        if type(i)==int and i%2==0:
            cubes.append(i**3)
    return cubes
n=[1,2,3,4,5,6,'hello',7,8,'d',10]
k=cube_even_integer(n)
print(k)        