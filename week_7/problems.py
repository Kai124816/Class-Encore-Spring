import doctest

def sum_every_other(lst: list):
    """
    Returns the sum of every other element in the list, starting from the first.

    >>> sum_every_other([1, 2, 3, 4, 5]) # doctest: +SKIP
    9
    >>> sum_every_other([10, 20, 30]) # doctest: +SKIP
    40
    >>> sum_every_other([]) # doctest: +SKIP
    0
    """
    return


def reverse_even_indices(strings: list[str]):
    """
    Reverses strings at even indices in the list and returns the modified list.

    >>> reverse_even_indices(["cat", "dog", "fish", "bird"]) # doctest: +SKIP
    ['tac', 'dog', 'hsif', 'bird']
    >>> reverse_even_indices(["a", "b", "c", "d", "e"]) # doctest: +SKIP
    ['a', 'b', 'c', 'd', 'e']
    """
    for i in range(len(strings)):
        if (i % 2) == 0:
            return #Finish this function


def first_repeating(lst: list):
    """
    Returns the first repeating element in the list. If none, returns -1.

    >>> first_repeating([1, 2, 3, 2, 4]) # doctest: +SKIP
    2
    >>> first_repeating([5, 6, 7]) # doctest: +SKIP
    -1
    >>> first_repeating([]) # doctest: +SKIP
    -1
    """
    return


def second_largest(lst: list):
    """
    Returns the second largest value in the list. If not available, returns -1.
    Assume the list does not have duplicates.

    >>> second_largest([1, 3, 2, 5]) # doctest: +SKIP
    3
    >>> second_largest([2, 9, 8]) # doctest: +SKIP
    8
    >>> second_largest([7]) # doctest: +SKIP
    -1
    """
    if len(lst) < 2:
        return -1
    
    largest = lst[0]
    second = None
    for i in range(1, len(lst)):
        if lst[i] > largest:
            pass #Fill this part in
        elif second == None:
            pass #Fill this part in
        elif lst[i] > second and lst[i] < largest:
            pass #Fill this part in
    return #Fill this part in


def recursive_sum(lst: list):
    """
    Recursively returns the sum of all elements in the list.

    >>> recursive_sum([1, 2, 3, 4]) # doctest: +SKIP
    10
    >>> recursive_sum([10]) # doctest: +SKIP
    10
    """
    return


def count_occurrences(lst: list, target: int):
    """
    Recursively counts how many times the target appears in the list.

    >>> count_occurrences([1, 2, 2, 3, 2, 4], 2) # doctest: +SKIP
    3
    >>> count_occurrences([5, 5, 5], 5) # doctest: +SKIP
    3
    >>> count_occurrences([1, 2, 3], 4) # doctest: +SKIP
    0
    """
    return


def flatten(lst: list):
    """
    Recursively flattens a nested list into a single list of elements.

    >>> flatten([1, [2, 3], [4, [5]]]) # doctest: +SKIP
    [1, 2, 3, 4, 5]
    >>> flatten([1, 2, 3]) # doctest: +SKIP
    [1, 2, 3]
    >>> flatten([]) # doctest: +SKIP
    []
    """
    flattened = []
    for el in lst:
        if isinstance(el, list):
            pass #Fill this part in
        else:
            pass #Fill this part in
    return #Fill this part in


def sum_of_nested_list(lst: list):
    """
    Recursively computes the sum of all numbers in a nested list.

    >>> sum_of_nested_list([1, [2, 3], [4, [5]]]) # doctest: +SKIP
    15
    >>> sum_of_nested_list([10, [20], 30]) # doctest: +SKIP
    60
    >>> sum_of_nested_list([]) # doctest: +SKIP
    0
    """
    return


if __name__ == "__main__":
    doctest.testmod()