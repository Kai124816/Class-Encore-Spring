import doctest

#Final Mega Review Solutions


#List Comprehension Problems

#1
def lookup(item_key: str, keys: list[str], values: list[int]) -> int:
    """If item_key is an element of keys,
    return the value v such that keys[idx] == item_key and values[idx] == v,
    otherwise return -1.
    >>> lookup("tiger", ["lion", "tiger", "bear"], [13, 47, 17]) 
    47
    >>> lookup("wolf", ["lion", "tiger", "bear"], [13, 47, 17])
    -1
    """
    for idx in range(len(keys)):
        if keys[idx] == item_key:
            return values[idx]
    return -1


#2
def matches(x_l: list[str], y_l: list[str]) -> list[bool]:
    """Returns list m in which each m[i] is
    True if and only if x_l[i] is same as y_l[i].
    x_l and y_l are parallel lists.
    >>> matches(["a", "b", "c"], ["a", "x", "c"]) 
    [True, False, True]
    """
    assert len(x_l) == len(y_l)
    result = []
    
    for i in range(len(x_l)):
        r = False
        if x_l[i] == y_l[i]:
            r = True
        result.append(r)
    return result


#3
def ascending(l: list[int]) -> bool:
    """True if elements of l are strictly increasing, i.e.,
    each element is greater than the element before (if any).
    >>> ascending([]) 
    True
    >>> ascending([1]) 
    True
    >>> ascending([1, 1, 1])
    False
    >>> ascending([1, 2, 8, 17]) 
    True
    >>> ascending([1, 8, 2, 17]) 
    False
    """
    for i in range(1,len(l)):
        if l[i] <= l[i-1]:
            return False
    return True





#4
def find_index(target: str, items: list[str]) -> int:
    """Returns the index of the first occurrence of target in items.
    If target is not found, return -1.
    
    >>> find_index("apple", ["banana", "apple", "cherry"])
    1
    >>> find_index("date", ["banana", "apple", "cherry"]) 
    -1
    """
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


#5
def greater_than_all_before(nums: list[int]) -> list[bool]:
    """Returns a list where each element at index i is True
    if nums[i] is greater than all elements that come before it.
    
    >>> greater_than_all_before([3, 4, 2, 5, 1]) 
    [True, True, False, True, False]
    >>> greater_than_all_before([1, 2, 3]) 
    [True, True, True]
    >>> greater_than_all_before([]) 
    []
    """
    if len(nums) == 0:
        return []
    
    greatest = nums[0]
    final_list = [True]
    for i in range(1,len(nums)):
        if nums[i] > greatest:
            final_list.append(True)
            greatest = nums[i]
        else:
            final_list.append(False)
    return final_list



#6
def common_elements(a: list[int], b: list[int]) -> list[int]:
    """Returns a list of elements that appear in both a and b.
    Each common element should appear only once in the result.
    
    >>> common_elements([1, 2, 3], [3, 4, 5]) 
    [3]
    >>> common_elements([1, 2, 2, 3], [2, 2, 3]) 
    [2, 3]
    >>> common_elements([1, 2], [3, 4]) 
    []
    """
    common = []
    for el in a:
        if el in b and el not in common:
            common.append(el)
    return common



#Dictionary Problems

#1
def multiples(li: list[str]) -> list[str]:
    """Result is a list of items that appear more than
    once in li.
    >>> multiples(["apple", "orange", "apple", "banana", "banana"]) 
    ['apple', 'banana']
    """
    multiples = []
    count_dict = {}
    for el in li:
        if el in count_dict.keys() and count_dict[el] == 1:
            count_dict[el] += 1
            multiples.append(el)
        elif el not in count_dict.keys():
            count_dict[el] = 1
    return multiples



#2
def word_count(sentence):
    """Write a function word_count(sentence) that takes a string and returns a 
    dictionary where the keys are words and the values are the number of 
    times each word appears. 

    >>> word_count("the quick brown fox jumps over the lazy dog") 
    {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    >>> word_count("hello hello world") 
    {'hello': 2, 'world': 1}
    >>> word_count("") 
    {}
    >>> word_count("repeat repeat repeat") 
    {'repeat': 3}
    """
    sentence_list = sentence.split()
    count_dict = {}
    for el in sentence_list:
        if el not in count_dict.keys():
            count_dict[el] = 1
        else: 
            count_dict[el] += 1
    return count_dict


#3
def count_occurrences(li: list[str]) -> dict[str, int]:
    """Count Occurrences: Given a list of strings, return a dictionary mapping 
    each unique string to the number of times it appears in the list.

    >>> count_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]) 
    {'apple': 3, 'banana': 2, 'orange': 1}
    >>> count_occurrences([]) 
    {}
    """
    count_dict = {}
    for el in li:
        if el not in count_dict.keys():
            count_dict[el] = 1
        else: 
            count_dict[el] += 1
    return count_dict


#4
def unique_items(li: list[str]) -> list[str]:
    """Return a list of items that appear exactly once in the input list.

    >>> unique_items(["a", "b", "a", "c", "d", "b", "e"]) 
    ['c', 'd', 'e']
    >>> unique_items(["x", "x", "x"]) 
    []
    >>> unique_items([]) 
    []
    """
    count_dict = {}
    for el in li:
        if el not in count_dict.keys():
            count_dict[el] = 1
        else:
            count_dict[el] += 1
    
    unique_list = []
    for key in count_dict.keys():
        if count_dict[key] == 1:
            unique_list.append(key)
    return unique_list



#5
def most_frequent_word(words: list[str]) -> str: #take note
    """Given a list of words, return the word that appears most frequently.
    If there is a tie, return any one of the most frequent words.

    >>> most_frequent_word(["a", "b", "a", "c", "b", "b"]) 
    'b'
    >>> most_frequent_word(["x"])
    'x'
    >>> most_frequent_word(["one", "two", "three", "two", "three", "three"])
    'three'
    """
    count_dict = {}
    for el in words:
        if el not in count_dict.keys():
            count_dict[el] = 1
        else:
            count_dict[el] += 1
    
    most_frequent = " "
    num_appearances = 0
    for key in count_dict.keys():
        if count_dict[key] > num_appearances:
            most_frequent = key
            num_appearances = count_dict[key]
    return most_frequent



#Binary Search Problems

#1
def binary_search(target: int, nums: list[int]) -> int:
    """Returns the index of `target` in sorted list `nums` using binary search.
    If not found, return -1.

    >>> binary_search(5, [1, 3, 5, 7, 9]) 
    2
    >>> binary_search(1, [1, 2, 3, 4, 5]) 
    0
    >>> binary_search(10, [1, 3, 5, 7, 9]) 
    -1
    >>> binary_search(3, []) 
    -1
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#2
def binary_contains(target: int, nums: list[int]) -> bool:
    """Returns True if `target` is in the sorted list `nums`, False otherwise.

    >>> binary_contains(8, [1, 2, 4, 6, 8, 10]) 
    True
    >>> binary_contains(5, [1, 2, 4, 6, 8, 10]) 
    False
    >>> binary_contains(1, [1]) 
    True
    >>> binary_contains(2, []) 
    False
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


#3
def first_occurrence(target: int, nums: list[int]) -> int:
    """Returns the index of the **first occurrence** of `target` in a sorted list `nums`.
    If `target` is not found, returns -1.

    >>> first_occurrence(3, [1, 2, 3, 3, 3, 4, 5]) 
    2
    >>> first_occurrence(6, [1, 2, 3, 4, 5]) 
    -1
    >>> first_occurrence(3, [3, 3, 3, 3]) 
    0
    >>> first_occurrence(1, []) 
    -1
    """
    left = 0
    right = len(nums) - 1
    result = -1  # Store result if found

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid       # Update result and continue left
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1     # Move to right half
        else:
            right = mid - 1    # Move to left half

    return result



#Recursion Problems

#1
DUST = "d"
MOUSE = "m"

def has_mice(nest) -> bool:
    """Returns True if MOUSE appears anywhere in the nest, otherwise False.
    >>> has_mice([[DUST], DUST, [MOUSE, DUST]])
    True
    >>> has_mice(([[DUST], DUST, [DUST, DUST]])) 
    False
    >>> has_mice([]) 
    False
    >>> has_mice(MOUSE) 
    True
    """
    if isinstance(nest, list):
        for e in nest:
            if has_mice(e):
                return True
        return False
    else:
        return nest == MOUSE


#2
"""
It may be useful to consider these facts:
• The sum of zero integers is zero. Thus, subset_sums(0, t) is always true.
• If k is positive, then there are two ways that the sum k could be produced: The first
element terms[0] could be included or not. If terms[0] is used, then it must be
possible to sum the remaining terms (terms[1:]) to k - terms[0]. If terms[0] is
not used, then it must be possible to sum the remaining terms to k.
def subset_sums(k: int, terms: list[int]) -> bool:
"""

def subset_sums(k: int, terms: list[int]) -> bool:
    """Return True if it is possible to produce k by adding up
    some subset of terms (using each term no more than once).
    k is a positive integer or zero, and each element of terms is a
    positive integer or zero.
    >>> subset_sums(10, [1, 3, 5, 7]) 
    True
    >>> subset_sums(12, [2, 3, 5, 8]) 
    False
    """
    if k == 0:
        return True
    if len(terms) == 0 or k < 0:
        return False
    return subset_sums(k, terms[1:]) or subset_sums(k-terms[0], terms[1:])


#3
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
        return 0
    elif lst[0] == target:
        return 1 + count_occurrences(lst[1:],target)
    else:
        return count_occurrences(lst[1:],target)


#4
def is_palindrome(s: str) -> bool:
    """
    Determine if a string is a palindrome recursively.

    >>> is_palindrome("llol") 
    False
    >>> is_palindrome("tacocat") 
    True
    >>> is_palindrome("racecar") 
    True
    """
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
    


#5
def l_count(letter: str, word: str) -> int:
    """Number of times letter appears in word
    (using recursion only, with no other looping)
    >>> l_count("m", "mimosa") 
    2
    >>> l_count("x", "mimosa") 
    0
    >>> l_count("m", "") 
    0
    """
    if len(word) == 0:
        return 0
    elif word[0] == letter:
        return 1 + l_count(letter,word[1:])
    else:
        return 0 + l_count(letter,word[1:])



#Nested data structures

#1
def most(collection: list[tuple[str, int]]) -> str:
    """Which element of the non-empty collection of (key, count) pairs
    has the greatest total count? (All counts are positive.)
    >>> most([("dogs", 3), ("cats", 5), ("dogs", 3)]) 
    'dogs'
    >>> most([("dogs", 3), ("cats", 7), ("dogs", 3)]) 
    'cats'
    """
    assert len(collection) > 0

    sums = {}
    for key, count in collection:
        if key not in sums:
            sums[key] = 0
        sums[key] += count

    max_key = "nothing"
    max_sum = 0
    for key, sum in sums.items():
        if sums[key] > max_sum:
            max_sum = sums[key]
            max_key = key
    return max_key



#2
def nested_contains(lst:list,target:int)->bool:
    """
    Checks if a nested contains a number

    >>> nested_contains([1, [2, [3, 4], 5], 6], 4) 
    True
    >>> nested_contains([[1], [2, [3]], 4], 7) 
    False
    >>> nested_contains([],1) 
    False
    """
    for el in lst:
        if el == target:
            return True
        elif isinstance(el,list):
            if nested_contains(el,target) == True:
                return True
    return False


#3
def sum_nested(lst:list)->int:
    """
    Recursively sums all integers in a nested list structure.

    >>> sum_nested([1, [2, [3, 4], 5], 6])
    21
    >>> sum_nested([[[1], 2], 3]) 
    6
    >>> sum_nested([]) 
    0
    """
    nested_sum = 0
    for el in lst:
        if isinstance(el,list):
            nested_sum += sum_nested(el)
        else:
            nested_sum += el
    return nested_sum


#4
def total_scores(records: dict[str, list[int]]) -> dict[str, int]:
    """
    Given a dictionary where keys are student names and values are lists of test scores,
    return a new dictionary mapping each student to their total score (sum of their scores).

    >>> total_scores({"Alice": [80, 90], "Bob": [70, 85, 95], "Eve": []}) 
    {'Alice': 170, 'Bob': 250, 'Eve': 0}
    >>> total_scores({}) 
    {}
    >>> total_scores({"Tom": [100]})
    {'Tom': 100}
    """
    new_dict = {}
    for name in records.keys():
        score_list = records[name]
        score_sum = 0
        for score in score_list:
            score_sum += score
        new_dict[name] = score_sum
    return new_dict
        



#5
def max_sum_list(data: list[list[int]]) -> int: #take note
    """
    Given a list of lists of integers, return the sum of inner list that has the greatest sum.

    >>> max_sum_list([[1, 2, 3], [4, 5], [0], [10]]) 
    10
    >>> max_sum_list([[10, -5], [3, 3, 3], [6]]) 
    9
    >>> max_sum_list([]) 
    0
    >>> max_sum_list([[], [1], [2, -2]]) 
    1
    """
    largest_sum = 0
    for lst in data:
        running_sum = 0
        for num in lst:
            running_sum += num
        if running_sum > largest_sum:
            largest_sum = running_sum
    return largest_sum




if __name__ == "__main__":
    doctest.testmod()  