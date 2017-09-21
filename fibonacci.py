def fibb(n):
    if n <= 2: 
        result = 1
        return result
    else:
        result = fibb(n-2) + fibb(n-1)
        return result

print(fibb(4))