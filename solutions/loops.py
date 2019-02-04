def div_by_33():
    """
    Constructs a list of all numbers between 0 and 1000 that are evenly divisible by 33.
    """
    result = []
    for i in range(0, 1000):
        if i % 33 == 0:
            result.append(i)
    return result


def get_total_length(strings):
    """
    Returns the sum of the length of the strings passed as input.
    """
    total = 0
    for string in strings:
        total += len(string)
    return total


def get_sublist(strings):
    """
    Filters the given list of strings for those that contain the letter "d" or "m"
    """
    sublist = []
    for string in strings:
        if "d" in string or "m" in string:
            sublist.append(string)
    return sublist

