def fibb(n):
    result = 1
    if n <= 2: 
        return result
    else:
        result = fibb(n-2) + fibb(n-1)
        return result

print(fibb(4))