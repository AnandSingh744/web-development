t1=(1,2,5,7,9,2,4,6,8,10)
def get_even_number(t1):
    list=[]
    for i in t1:
        if i%2==0:
            list.append(i)
    return tuple(list)

m=get_even_number(t1)
print("tuple with even number :",m)        