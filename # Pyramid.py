# Pyramid
n = 5  # Number of levels
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# Reverse Pyramid
for i in range(n, 0,-1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
