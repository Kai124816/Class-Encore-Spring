#problem 1
"""
Write a function common_elements(list1, list2) that takes two lists and returns a 
new list containing only the elements that appear in both.
"""
def common_elements(list1:list, list2:list)->list:
    """
    >>> common_elements([1, 2, 3], [2, 3, 4])
    [2, 3]
    >>> common_elements(["a", "b", "c"], ["c", "d", "e"])
    ['c']
    >>> common_elements([1, 2], [3, 4])
    []
    """
    return


#problem 2
"""
Smallest Each: From a list of (name, value) pairs, select the pairs with the smallest
value for each name.
"""
def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    >>> smallest_each([("apple", 13), ("orange", 12), ("apple", 7), ("orange", 22)])
    [('apple', 7), ('orange', 12)]
    >>> smallest_each([])
    []
    >>> smallest_each([("a", 5), ("a", 3), ("b", 2)])
    [('a', 3), ('b', 2)]
    """
   


#problem 3 
"""
Return the item in li with maximum length.
Break ties in favor of first occurrence.
"""
def longest_string(li: list[str]) -> str:
    """
    >>> longest_string(["fish", "dog", "avocado", "onion"])
    'avocado'
    >>> longest_string([])
    ''
    >>> longest_string(["winter", "spring", "summer", "fall"])
    'winter'
    """


#problem 4
"""
Count Occurrences: Given a list of strings, return a dictionary mapping each unique 
string to the number of times it appears in the list.
"""
def count_occurrences(li: list[str]) -> dict[str, int]:
    """
    >>> count_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"])
    {'apple': 3, 'banana': 2, 'orange': 1}
    >>> count_occurrences([])
    {}
    """


#problem 5
"""
Filter Greater: Return a new list containing only the elements from the input list 
that are greater than a given threshold.
"""
def filter_greater(li: list[int], threshold: int) -> list[int]:
    """
    >>> filter_greater([1, 5, 10, 3, 7], 4)
    [5, 10, 7]
    >>> filter_greater([2, 3], 10)
    []
    >>> filter_greater([], 5)
    []
    """
