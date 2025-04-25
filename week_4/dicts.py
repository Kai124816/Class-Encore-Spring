#Problem 1
"""
Write a function word_count(sentence) that takes a string and returns a 
dictionary where the keys are words and the values are the number of 
times each word appears. The .split() method may be useful as it turns a sentence 
string into a list of words.
"""
def word_count(sentence:str):
    """
    >>> word_count("the cat and the dog")
    {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
    >>> word_count("Apple apple apple")
    {'Apple': 1, 'apple': 2}
    >>> word_count("")
    {}
    >>> word_count("to be or not to be")
    {'to': 2, 'be': 2, 'or': 1, 'not': 1}
    """
    return


#Problem 2
"""
Write a function that returns a dict where the keys are elements in
the list and the values are how many times each element appears in the list
"""
def count_all_values(li: list[str]) -> dict[str, int]:
    """Returns dict with counts of strings in li.
    >>> count_all_values(["carrot", "chocolate", "carrot", "strawberry"])
    {'carrot': 2, 'chocolate': 1, 'strawberry': 1}
    >>> count_all_values([])
    {}
    >>> count_all_values(["a", "b", "a", "a", "c"])
    {'a': 3, 'b': 1, 'c': 1}
    """


#Problem 3
"""
Write a function most_frequent_word(sentence) that returns the word that appears 
most frequently in a sentence. In case of a tie, return the word that appears first.
"""
def most_frequent_word(sentence: str) -> str:
    """
    >>> most_frequent_word("the cat and the dog")
    'the'
    >>> most_frequent_word("apple banana apple orange banana banana")
    'banana'
    >>> most_frequent_word("")
    ''
    """
    appears_most = " "


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


#problem 6
"Greatest Magnitude"
def magnitude_list(cities:list[int],magnitudes:list[int])->list[list[int]]:
    return
