# author: mbender
"""
a
b
"""

def f(n):
    vals = [1, 1]
    while len(vals) <= n:
        vals.append(vals[-1] + vals[-2])

    return vals[-1]

print(f(100))

for i in range(101, 200):
    print(f(i))