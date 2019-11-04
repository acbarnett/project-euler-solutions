# This is the naive implementation


array_of_digits = [0,1,2,3,4,5,6,7,8,9]


def next_permutation(digits):
    # Find largest k s. t. a[k] < a[k+1]
    # Find largest l > k s.t. a[k] < a[l]
    # Swap a[k], a[l]
    # Reverse a[k+1] to a[n] the final element
    length = len(digits)
    k = None
    l = None

    i = 0
    while i < length - 1:
        if digits[i] < digits[i+1]:
            k = i
        i += 1
    if k is None:
        raise ValueError('Max number of iterations reached')

    i = k
    while i < length:
        if digits[k] < digits[i]:
            l = i
        i += 1
    if l is None:
        raise ValueError('Could not find value for `l`')

    # Yes there's a way to do this that doesn't use a swap variable
    # But let's maximize clarity
    swap_var = digits[k]
    digits[k] = digits[l]
    digits[l] = swap_var

    # Reverse the trailing digits
    digits_to_keep = digits[:k+1]
    digits_to_reverse = digits[k+1:]
    digits_to_reverse.reverse()

    return digits_to_keep + digits_to_reverse

def get_millionth_permutation(digits):
    iteration_count = 1
    desired_iteration_count = 1000000
    while iteration_count < desired_iteration_count:
        digits = next_permutation(digits)
        iteration_count += 1

    string_digits = [str(i) for i in digits]
    return ''.join(string_digits)



print(get_millionth_permutation(array_of_digits))

