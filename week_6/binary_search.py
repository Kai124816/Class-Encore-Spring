import doctest
#Note when you test the functions remove "# doctest: +SKIP" for each of the doctests

#Problem 1
def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target's index.

    >>> binary_search([1, 3, 5, 7, 9], 5) # doctest: +SKIP
    2
    >>> binary_search([1, 3, 5, 7, 9], 6) # doctest: +SKIP
    -1
    >>> binary_search([], 1) # doctest: +SKIP
    -1
    """
    pass  # implementation here


#Problem 2
def find_first_last(arr, target):
    """
    Find the first and last position of a target in a sorted array.

    >>> find_first_last([1, 2, 2, 2, 3, 4], 2) # doctest: +SKIP
    (1, 3)
    >>> find_first_last([1, 2, 3, 4], 5) # doctest: +SKIP
    (-1, -1)
    >>> find_first_last([], 1) # doctest: +SKIP
    (-1, -1)
    """
    pass  # implementation here


#Problem 3
def search_insert_position(arr, target):
    """
    Find the index where target should be inserted in sorted array.

    >>> search_insert_position([1, 3, 5, 6], 5) # doctest: +SKIP
    2
    >>> search_insert_position([1, 3, 5, 6], 2) # doctest: +SKIP
    1
    >>> search_insert_position([1, 3, 5, 6], 7) # doctest: +SKIP
    4
    """
    pass  # implementation here


#Problem 4
def sqrt_int(x):
    """
    Compute the integer square root of a non-negative integer.
    Return -1 if no square root exists

    >>> sqrt_int(8) # doctest: +SKIP
    -1
    >>> sqrt_int(16) # doctest: +SKIP
    4
    >>> sqrt_int(1) # doctest: +SKIP
    1
    >>> sqrt_int(0) # doctest: +SKIP
    0
    """
    pass  # implementation here


#Problem 5
def find_first_with_prefix(words, target):
    """
    Returns the index of the first word which matches the target word in a sorted list.
    Hint if a word comes before another word in alphabetical order it's value is less than 
    that other word's. For example "apple" < "banana".

    >>> find_first_with_prefix(["apple", "banana", "cherry", "date", "fig", "grape"], "cherry")
    2
    >>> find_first_with_prefix(["apple", "banana", "banana", "banana", "cherry"], "banana")
    1
    >>> find_first_with_prefix(["apple", "banana", "cherry"], "kiwi")
    -1
    >>> find_first_with_prefix([], "any")
    -1
    """
    pass # implementation here


if __name__ == "__main__":
    doctest.testmod()