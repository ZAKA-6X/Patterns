# Pattern: Increasing Staircase
n = 6
for i in range(1,n+1):
    stars = i * '*'
    print(stars)

# Pattern: Decreasing Staircase
n = 6
for i in range(n, 0, -1):
    stars = i * '*'
    print(stars)

# Pattern: Right-aligned Staircase
n = 6
for i in range(1,n+1):
    spaces = (n - i) * ' '
    stars = i * '*'
    print(spaces + stars)

# Pattern: Left-aligned Staircase
n = 6
for i in range(1,n):
    spaces = (i) * ' '
    stars = (n - i) * '*'
    print(spaces + stars)

# Pattern: Diamond
n = 11
head = (n)*' ' + '*'
print(head)
for i in range(1,n+1):
    spaces = ' ' * (n-i) 
    stars = '*' * i * 2 + '*'
    print(spaces + stars)

# Pattern: Reversed Diamond
n = 11
for i in range(1, n+1):
    spaces = ' ' * (i) 
    stars = '*' * (n-i) * 2 + '*'
    print(spaces + stars)
