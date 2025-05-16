import doctest

def sum_every_other(lst: list):
    """
    Returns the sum of every other element in the list, starting from the first.

    >>> sum_every_other([1, 2, 3, 4, 5])
    9
    >>> sum_every_other([10, 20, 30])
    40
    >>> sum_every_other([])
    0
    """
    sum = 0
    for i in range(len(lst)):
        if (i % 2) == 0:  # Check if the index is even
            sum += lst[i]  # Add element to sum if index is even
    return sum


def reverse_even_indices(strings: list[str]):
    """
    Reverses strings at even indices in the list and returns the modified list.

    >>> reverse_even_indices(["cat", "dog", "fish", "bird"])
    ['tac', 'dog', 'hsif', 'bird']
    >>> reverse_even_indices(["a", "b", "c", "d", "e"])
    ['a', 'b', 'c', 'd', 'e']
    """
    for i in range(len(strings)):
        if (i % 2) == 0:  # Only reverse strings at even indices
            new_str = ""
            # Reverse the string manually by iterating backwards
            for j in range(len(strings[i])):
                new_str += strings[i][-j-1]
            strings[i] = new_str  # Replace the original with the reversed string
    return strings


def first_repeating(lst: list):
    """
    Returns the first repeating element in the list. If none, returns -1.

    >>> first_repeating([1, 2, 3, 2, 4])
    2
    >>> first_repeating([5, 6, 7])
    -1
    >>> first_repeating([])
    -1
    """
    appears_once = []  # Track seen elements
    for el in lst:
        if el in appears_once:  # If element already seen, it's the first repeat
            return el
        else:
            appears_once.append(el)  # Add to seen elements
    return -1  # No repeats found


def second_largest(lst: list):
    """
    Returns the second largest value in the list. If not available, returns -1.
    Assume the list does not have duplicates.

    >>> second_largest([1, 3, 2, 5])
    3
    >>> second_largest([2, 9, 8])
    8
    >>> second_largest([7])
    -1
    """
    if len(lst) < 2:
        return -1  # Not enough elements for second largest
    
    largest = lst[0]  # Start with the first element as the largest
    second = None  # Will store second largest
    
    for i in range(1, len(lst)):
        if lst[i] > largest:
            # Found new largest; update second
            second = largest
            largest = lst[i] 
        elif second == None:
            # First time setting second
            second = lst[i]
        elif lst[i] > second and lst[i] < largest:
            # Update second if current is between largest and current second
            second = lst[i]
    
    return second if second is not None else -1


def recursive_sum(lst: list):
    """
    Recursively returns the sum of all elements in the list.

    >>> recursive_sum([1, 2, 3, 4])
    10
    >>> recursive_sum([10])
    10
    """
    if len(lst) == 1:
        return lst[0]  # Base case: only one element
    else:
        return lst[0] + recursive_sum(lst[1:])  # Sum first + recursive call on rest


def count_occurrences(lst: list, target: int):
    """
    Recursively counts how many times the target appears in the list.

    >>> count_occurrences([1, 2, 2, 3, 2, 4], 2)
    3
    >>> count_occurrences([5, 5, 5], 5)
    3
    >>> count_occurrences([1, 2, 3], 4)
    0
    """
    if len(lst) == 0:
        return 0  # Base case: empty list
    if lst[0] == target:
        return 1 + count_occurrences(lst[1:], target)  # Match found, add 1
    else:
        return count_occurrences(lst[1:], target)  # No match, continue


def flatten(lst: list):
    """
    Recursively flattens a nested list into a single list of elements.

    >>> flatten([1, [2, 3], [4, [5]]])
    [1, 2, 3, 4, 5]
    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([])
    []
    """
    flattened = []
    for el in lst:
        if isinstance(el, list):
            # If element is a list, flatten it recursively
            flattened += flatten(el)
        else:
            # If not a list, add it directly
            flattened.append(el)
    return flattened


def sum_of_nested_list(lst: list):
    """
    Recursively computes the sum of all numbers in a nested list.

    >>> sum_of_nested_list([1, [2, 3], [4, [5]]])
    15
    >>> sum_of_nested_list([10, [20], 30])
    60
    >>> sum_of_nested_list([])
    0
    """
    sum = 0
    for el in lst:
        if isinstance(el, list):
            # Recurse into nested list and add to sum
            sum += sum_of_nested_list(el)
        else:
            # Add non-list element
            sum += el
    return sum


if __name__ == "__main__":
    doctest.testmod()  # Automatically run the tests written in the docstrings
