def len(a,b):
    return (a**2 + b**2) ** 0.5

print(len(3, 5))

def fac(n):
    if n == 1:
        return 1;
    else:
        return n * fac(n - 1);

print(fac(5))