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


#problem 3
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
