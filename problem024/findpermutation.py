import argparse
import sys

from perm_lib import range_is_valid, make_symbol_list, find_permutation, permutation_will_be_cyclic

perm_description = 'For a range of numbers, find the nth lexicographic permutation'
perm_parser = argparse.ArgumentParser(description=perm_description)

perm_parser.add_argument('Maximum',
                         type=int,
                         help='The maximum number in the range. 9 is the max supported')


perm_parser.add_argument('PermutationNumber',
                         type=int,
                         help='The number of the permutation you want, indexed from 1')

perm_parser.add_argument('--cyclic',
                         action='store_true',
                         dest='Cyclic',
                         help='Whether or not to allow cyclic permutations, such as the 9999th permutation of 012')

args = perm_parser.parse_args()

max_of_range = args.Maximum
# for ease of use, this permutation number is indexed from 1
permutation_number = args.PermutationNumber
allow_cyclic_permutations = args.Cyclic

# create a zero-indexed permutation for consumption inside the program
zero_indexed_permutation_number = permutation_number - 1

# Is the maximum valid? This only support ranges up to 0-9.
# 0-5 is fine, but we're not going into hexadecimal. Yet.
if not range_is_valid(max_of_range):
    print('Only numbers up to 9 are supported at this time. Please try again.')
    sys.exit()

if permutation_will_be_cyclic(max_of_range, zero_indexed_permutation_number) and not allow_cyclic_permutations:
    print('Use the --cyclic flag to compute permutations with negative index, or permutations with will complete more than one full cycle')
    sys.exit()

# Find and print the desired permutation
permutation = find_permutation(make_symbol_list(max_of_range),
                               zero_indexed_permutation_number)
print(permutation)
