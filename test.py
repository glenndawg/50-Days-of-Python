def eq(a,b):
    return lambda x: a*x**2 + b*x

f = eq(5,7)

print(f(12))
    
