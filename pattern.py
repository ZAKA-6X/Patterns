# Pattern: Increasing Staircase
n = 7
for item in range(1, n+1):
    line = '*' * item
    print(line)

print('\n')

# Pattern: Decreasing Staircase
n = 7
for item in range(n, 0, -1):
    line = '*' * item
    print(line)

print('\n')

# Pattern: Right-aligned Staircase
n = 7
for item in range(n, 0, -1):
    spaces = ' ' * (n - item)
    stars = '*' * item
    line = spaces + stars
    print(line)

print('\n')

# Pattern: Left-aligned Staircase
n = 7
for item in range(n, 0, -1):
    spaces = ' ' * item
    stars = '*' * (n - item)
    line = spaces + stars
    print(line)

print('\n')

# Pattern: Diamond
n = 7
print(' ' * (n-1) + '*')
for item in range(2, n+1):
    spaces = ' ' * (n - item)
    stars = '*' * (2 * item - 1)
    line = spaces + stars
    print(line)

print('\n')

# Pattern: Reversed Diamond
n = 7
for item in range(n, 1, -1):
    spaces = ' ' * (n - item)
    stars = '*' * (2 * item - 1)
    line = spaces + stars
    print(line)
print(' ' * (n-1) + '*')