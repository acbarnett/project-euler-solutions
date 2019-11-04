from math import factorial

def range_is_valid(maximum):
    """Determine if the provided range is valid. Since the numbers that make
    up the list are expected to be from 0 to 9, ensure the provided maximum
    falls into that range.
    Parameters
    ----------
    maximum: int
    Returns
    -------
    boolean
        Whether or not the provided maximum is valid
    """
    return maximum <= 9 and maximum >= 0

def permutation_will_be_cyclic(maximum, permutation_count):
    """Determine if the permutation will be cyclic. It's possible the user
    may not have realized they wanted to wrap around after finishing all possible
    permutations. The user can pass a command-line argument to the main program if
    this behavior is desired
    Parameters
    ----------
    maximum: int
        The largest number to appear in the list of digits to be permuted
    permutation_count: int
        The index of the desired permutation, indexed from 0
    Returns
    -------
    boolean
        Whether or not the permutation will be cyclic
    """
    return permutation_count < 0 or permutation_count >= factorial(maximum + 1)

def make_symbol_list(maximum):
    """For a given maximum, return the list of symbols to compute permutations for
    For instance, 3 would return ['0', '1', '2', '3']
    Parameters
    ----------
    maximum: int
    Returns
    -------
    List[str]
        A list of strings representing the symbols to be permuted
    """
    return [str(i) for i in range(0, maximum + 1)]

def find_permutation(symbol_list, permutation_count):
    """Recursively find the nth permutation of a list of symbols. If the length
    of the list of symbols is 1, then return that. Otherwise, take the count and
    use that to determine the first symbol of the permutation. That will have an index
    in the list given by the count divided by the number of possible permutations of
    the digits after the leading one (the factorial of the length of the list - 1)
    The digit at that index in the list will be the leading digit of the permutation.
    Use the remainder of that calculation, and the list after that number has been
    extracted, to recursively find the rest of the permutation.
    Parameters
    ----------
    symbol_list: List[str]
        A list of one or more strings
    permutation_count: int
        The number, indexed from 0, of permutations to be performed on the list
    Returns
    -------
    str
        A string representing the nth permutation of symbol_list
    """
    list_length = len(symbol_list)
    # First, handle the base case, else process the list recursively
    if list_length == 1:
        return symbol_list[0]

    # How many permutations will there be in the symbols after we've found the first one?
    trailing_permutations = factorial(list_length - 1)
    # The index of the leading symbol will be offset by the permutation count
    # divided by the number of trailing permutations (mod handles cyclic permutations)
    index_of_leading_digit = (permutation_count // trailing_permutations) % list_length
    leading_digit = symbol_list.pop(index_of_leading_digit)
    # Use the remainder of the above division to find out where in the trailing
    # permutations the desired permutation is
    sub_permutation_count = permutation_count % trailing_permutations
    # And recurse!
    return leading_digit + find_permutation(symbol_list, sub_permutation_count)

