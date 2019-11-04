# Problem 24 #

## Summary ##

Find the millionth lexicographic permutation of the numbers 0-9.
Full details of the problem can be found [here](https://projecteuler.net/problem=24 "Link to Problem 24").


## Usage ##

The first argument provided will be the maximum number in the list,
and the second is the index (from one) of the permutation.
Use the `--cyclic` flag if the requested permutation needs to loop through more than once.

    $ python3 findpermutation.py 3 1
    0123
    $ python3 findpermutation.py 3 24
    3210
    $ python3 findpermutation.py 4 121 --cyclic
    01234
    $ python3 findpermutation 4 0 --cyclic
    43210
    $ python3 findpermutation 4 -1 --cyclic
    43201


## Structure of the program ##

### `findpermutation.py` ###

The main file of this project is `findpermutation.py`.
It handles argument parsing
(pulling the maximum value - 0-9, the permutation number, and whether or not to account for cyclic permutations),
and checks to see that those inputs make sense together.
It then passes them off to `find_permutation` to do the processing.

### `perm_lib.py` ###

This handles all the calculations for Problem 24.
It exports the validation functions for the arguments, and also calculates the desired permutation.
This calculation is done recursively.
It finds the first digit of the permutation by computing the number of permutations available to the right of the current digit, divides the count of permutations by that, and then takes the third element from the list.
The remainder in that calculation, as well as the list without the chosen element, are passed to `find_permutation` again.
In the end, there will only be one number left in the list, and that will be the last element.


## Timing ##

The recursive approach used here was the first one that came to mind for me.
But as a comparison, I decided to check out an iterative method for coming to the same conclusion.
I used an algorithm from [Wikipedia](https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order) and implemented in `./naive/naive.py`

When comparing the runtime using `timeit`, the results favor the recursive approach for the assigned task.
This was unsurprising, but good to verify.
Timings:

    Recursive version
    0.0021903690067119896
    Iterative version
    1.8555911029689014

Note the timing for the recursive version was for 10000 runs, and the iterative timing was for one run.
The iterative approach could no doubt be optimized, but for the problem at hand, recursion FTW.
