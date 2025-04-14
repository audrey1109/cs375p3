def f(n):
    if n == 0 or n == 1: 
        return 1
    
    return f(n - 1) + f(n - 2)

for i in range(10):
    print(f(i))

print(f(100))