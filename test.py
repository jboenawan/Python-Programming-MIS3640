def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    result = []
    counter = 0
    for i in t:
        counter += i
        result.append(counter)

    return result

team = [3,2,3,2]
print(cumsum(team))