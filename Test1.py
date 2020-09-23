import doctest
def average(list):
    """
    This function calculates the average of a list of values passed as parameter.
    >>> average([ 87987, 321, 6857, 21.15, 798, -42, 54363, 159 ])
    18808.01875
    """
    result = 0
    for factor in list:
        result = factor + result
    return result / len(list)


values = [ 87987, 321, 6857, 21.15, 798, -42, 54363, 159 ]
result = average(values)
print("Result: %f" % result)
doctest.testmod(verbose=True)
