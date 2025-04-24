#Problem 1 dicts.py
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
    new_sentence = sentence.split()
    count_dict = {}
    for word in new_sentence:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return count_dict


#Problem 2 dicts.py
"""
Write a function that returns a dict where the keys are elements in
the list and the values are how many times each element appears in the list
"""
def count_all_values(li: list[str]) -> dict[str, int]:
    """
    >>> count_all_values(["carrot", "chocolate", "carrot", "strawberry"])
    {'carrot': 2, 'chocolate': 1, 'strawberry': 1}
    >>> count_all_values([])
    {}
    >>> count_all_values(["a", "b", "a", "a", "c"])
    {'a': 3, 'b': 1, 'c': 1}
    """
    count_dict = {}
    for word in li:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return count_dict


#Problem 3 dicts.py
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
    new_sentence = sentence.split()
    count_dict = {}
    max_word = ' '
    max_appearences = 0
    for word in new_sentence:
        if word not in count_dict:
            count_dict[word] = 1
            if max_word == ' ':
                max_word = word
                max_appearences = 1
        else:
            count_dict[word] += 1
            if count_dict[word] > max_appearences:
                max_word = word
                max_appearences = count_dict[word]
    return count_dict


#problem 1 lists.py
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
    combined = []
    for el in list1:
        if el in list2:
            combined.append(el)
    return combined


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
    smallest_dict = {}
    for pair in li:
        if pair not in smallest_dict.keys():
            smallest_dict[pair[0]] = pair[1]
        elif smallest_dict[pair[0]] > pair[1]:
            smallest_dict[pair[0]] = pair[1]
    
    
        