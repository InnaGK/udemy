def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_rec(1))
print(fibonacci_rec(0))
print(fibonacci_rec(2))
print(fibonacci_rec(4))
print(fibonacci_rec(5))
print(fibonacci_rec(3))
