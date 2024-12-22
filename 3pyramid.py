def print_pyramid(n):
    for i in range(1,n+1):
        print("*"*(2*i-1))
def print_reverse_pyramid(n):
    for i in range(n-1,0,-1):
        print("*"*(2*i-1))
n=5

print_pyramid(n)
print_reverse_pyramid(n)
