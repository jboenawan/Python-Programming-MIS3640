def remove_middle(data):
    '''
    Remove the middle element if the list length is odd,
    or the middle two elements if the list length is even.  
    No return is required.
    data: the list of values to process
    '''
    middle = float(len(data))/2
    if middle % 2 != 0:
        del data[int(middle + 0.5)]
    else:
        del data[int(middle)] 
        del data[int(middle)-1]


# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN)