def max_min(t1):
    max=t1[0]
    min=t1[0]

    for i in t1:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min
t1=(1,2,5,7,9,2,4,6,8,10)
max,min=max_min(t1)
print("maximum value:",max)
print("minimum value:",min)
