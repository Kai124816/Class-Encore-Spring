import doctest

#Final Mega Review

"""
Note: Uncomment print statements to get solutions for what does this print problems
Note: Remove # doctest: +SKIP to have the doctests run on your solution
"""

#What does this print problems

#1.
def f(x: int) -> int:
    y = x + 1
    return y

def g(y: int) -> int:
    x = f(y) + 1
    return x

def h(x: int) -> int:
    y = g(x) + 1
    return y

x = 7
y = h(x)
# print(x)
# print(y)


#2
POINTS = { "red": 5, "blue": 2, "yellow": 3}

def score(items: list[str]) -> int:
    """Scoring for an imaginary game"""
    total = 0
    for item in items:
        if item in POINTS:
            total += POINTS[item]
    return total

s = score(["red", "red", "yellow", "blue"])
# print(s)


#3
def riddle(low: int, high: int, keys: list[str], values: list[int]) -> int:
    assert len(keys) == len(values), "This riddle is only for parallel lists"
    tot = 0
    for idx in range(len(keys)):
        if keys[idx] >= low and keys[idx] <= high:
            tot += values[idx]
    return tot
x = riddle("c", "d", ["a", "b", "c", "d"], [5, 10, 20, 40])
# print(x)
y = riddle("a", "e", ["a", "b", "c", "d"], [5, 10, 20, 40])
# print(y)


#4
def mystery(li: list[int]) -> int:
    if li == []:
        return 0
    if li[0] == 5:
        return 1 + mystery(li[1:])
    else:
        return mystery(li[1:])
    
solution = mystery([3, 5, 3, 5, 8])
# print(solution)


#5
def f(x: int) -> int:
    y = x + 1
    return y

x = 7
y = 12
z = f(y)
# print(x)
# print(y)
# print(z)


#6
def avg_score(scores: list[int]) -> float:
    """Hypothetical grading scheme"""
    assert len(scores) > 2, "Requires at least three scores"
    lowest = scores[0]
    highest = scores[0]
    sum = 0
    for score in scores:
        if score < lowest:
            lowest = score
        if score > highest:
            highest = score
        sum += score
    n = len(scores) - 2
    sum = sum - (lowest + highest)
    return sum / n

exams = [80, 30, 100, 80]
avg = avg_score(exams)
# print(avg)


#7
def describe_day(hour):
    if hour < 12:
        print("morning")
    if hour < 18:
        print("afternoon")
    elif hour >= 18:
        print("evening")
    else:
        print("late night")
    return

time = 11
# describe_day(time)


#8
def divide(x, y):
    quotient = x / z
    return quotient

def half(n):
    result = divide(n, 2)
    return result

value = 100
final = half(value)
# print(final)



#List Comprehension Problems

#1
def lookup(item_key: str, keys: list[str], values: list[int]) -> int:
    """If item_key is an element of keys,
    return the value v such that keys[idx] == item_key and values[idx] == v,
    otherwise return -1.
    >>> lookup("tiger", ["lion", "tiger", "bear"], [13, 47, 17]) # doctest: +SKIP
    47
    >>> lookup("wolf", ["lion", "tiger", "bear"], [13, 47, 17]) # doctest: +SKIP
    -1
    """
    return


#2
def matches(x_l: list[str], y_l: list[str]) -> list[bool]:
    """Returns list m in which each m[i] is
    True if and only if x_l[i] is same as y_l[i].
    x_l and y_l are parallel lists.
    >>> matches(["a", "b", "c"], ["a", "x", "c"]) # doctest: +SKIP
    [True, False, True]
    """
    assert len(x_l) == len(y_l)
    return


#3
def ascending(l: list[int]) -> bool:
    """True if elements of l are strictly increasing, i.e.,
    each element is greater than the element before (if any).
    >>> ascending([]) # doctest: +SKIP
    True
    >>> ascending([1]) # doctest: +SKIP
    True
    >>> ascending([1, 1, 1]) # doctest: +SKIP
    False
    >>> ascending([1, 2, 8, 17]) # doctest: +SKIP
    True
    >>> ascending([1, 8, 2, 17]) # doctest: +SKIP
    False
    """
    return 


#4
def find_index(target: str, items: list[str]) -> int:
    """Returns the index of the first occurrence of target in items.
    If target is not found, return -1.
    
    >>> find_index("apple", ["banana", "apple", "cherry"]) # doctest: +SKIP
    1
    >>> find_index("date", ["banana", "apple", "cherry"]) # doctest: +SKIP
    -1
    """
    return


#5
def greater_than_all_before(nums: list[int]) -> list[bool]:
    """Returns a list where each element at index i is True
    if nums[i] is greater than all elements that come before it.
    
    >>> greater_than_all_before([3, 4, 2, 5, 1]) # doctest: +SKIP
    [True, True, False, True, False]
    >>> greater_than_all_before([1, 2, 3]) # doctest: +SKIP
    [True, True, True]
    >>> greater_than_all_before([]) # doctest: +SKIP
    []
    """
    return


#6
def common_elements(a: list[int], b: list[int]) -> list[int]:
    """Returns a list of elements that appear in both a and b.
    Each common element should appear only once in the result.
    
    >>> common_elements([1, 2, 3], [3, 4, 5]) # doctest: +SKIP
    [3]
    >>> common_elements([1, 2, 2, 3], [2, 2, 3]) # doctest: +SKIP
    [2, 3]
    >>> common_elements([1, 2], [3, 4]) # doctest: +SKIP
    []
    """
    return



#Dictionary Problems

#1
def multiples(li: list[str]) -> list[str]:
    """Result is a list of items that appear more than
    once in li.
    >>> multiples(["apple", "orange", "apple", "banana", "banana"]) # doctest: +SKIP
    ['apple', 'banana']
    """
    return


#2
def word_count(sentence):
    """Write a function word_count(sentence) that takes a string and returns a 
    dictionary where the keys are words and the values are the number of 
    times each word appears. 

    >>> word_count("the quick brown fox jumps over the lazy dog") # doctest: +SKIP
    {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    >>> word_count("hello hello world") # doctest: +SKIP
    {'hello': 2, 'world': 1}
    >>> word_count("") # doctest: +SKIP
    {}
    >>> word_count("repeat repeat repeat") # doctest: +SKIP
    {'repeat': 3}
    """
    return


#3
def count_occurrences(li: list[str]) -> dict[str, int]:
    """Count Occurrences: Given a list of strings, return a dictionary mapping 
    each unique string to the number of times it appears in the list.

    >>> count_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]) # doctest: +SKIP
    {'apple': 3, 'banana': 2, 'orange': 1}
    >>> count_occurrences([]) # doctest: +SKIP
    {}
    """
    return


#4
def unique_items(li: list[str]) -> list[str]:
    """Return a list of items that appear exactly once in the input list.

    >>> unique_items(["a", "b", "a", "c", "d", "b", "e"]) # doctest: +SKIP
    ['c', 'd', 'e']
    >>> unique_items(["x", "x", "x"]) # doctest: +SKIP
    []
    >>> unique_items([]) # doctest: +SKIP
    []
    """
    return


#5
def most_frequent_word(words: list[str]) -> str:
    """Given a list of words, return the word that appears most frequently.
    If there is a tie, return any one of the most frequent words.

    >>> most_frequent_word(["a", "b", "a", "c", "b", "b"]) # doctest: +SKIP
    'b'
    >>> most_frequent_word(["x"]) # doctest: +SKIP
    'x' 
    >>> most_frequent_word(["one", "two", "three", "two", "three", "three"]) # doctest: +SKIP
    'three'
    """
    return



#Binary Search Problems

#1
def binary_search(target: int, nums: list[int]) -> int:
    """Returns the index of `target` in sorted list `nums` using binary search.
    If not found, return -1.

    >>> binary_search(5, [1, 3, 5, 7, 9]) # doctest: +SKIP
    2
    >>> binary_search(1, [1, 2, 3, 4, 5]) # doctest: +SKIP
    0
    >>> binary_search(10, [1, 3, 5, 7, 9]) # doctest: +SKIP
    -1
    >>> binary_search(3, []) # doctest: +SKIP
    -1
    """
    return


#2
def binary_contains(target: int, nums: list[int]) -> bool:
    """Returns True if `target` is in the sorted list `nums`, False otherwise.

    >>> binary_contains(8, [1, 2, 4, 6, 8, 10]) # doctest: +SKIP
    True
    >>> binary_contains(5, [1, 2, 4, 6, 8, 10]) # doctest: +SKIP
    False
    >>> binary_contains(1, [1]) # doctest: +SKIP
    True
    >>> binary_contains(2, []) # doctest: +SKIP
    False
    """
    return


#3
def first_occurrence(target: int, nums: list[int]) -> int:
    """Returns the index of the **first occurrence** of `target` in a sorted list `nums`.
    If `target` is not found, returns -1.

    >>> first_occurrence(3, [1, 2, 3, 3, 3, 4, 5]) # doctest: +SKIP
    2
    >>> first_occurrence(6, [1, 2, 3, 4, 5]) # doctest: +SKIP
    -1
    >>> first_occurrence(3, [3, 3, 3, 3]) # doctest: +SKIP
    0
    >>> first_occurrence(1, []) # doctest: +SKIP
    -1
    """
    return


#Recursion Problems

#1
def has_mice(nest) -> bool:
    """Returns True if MOUSE appears anywhere in the nest, otherwise False.
    >>> has_mice([[DUST], DUST, [MOUSE, DUST]]) # doctest: +SKIP
    True
    >>> has_mice(([[DUST], DUST, [DUST, DUST]])) # doctest: +SKIP
    False
    >>> has_mice([]) # doctest: +SKIP
    False
    >>> has_mice(MOUSE) # doctest: +SKIP
    True
    """
    return


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
    >>> subset_sums(10, [1, 3, 5, 7]) # doctest: +SKIP
    True
    >>> subset_sums(12, [2, 3, 5, 8]) # doctest: +SKIP
    False
    """
    return


#3
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


#4
def is_palindrome(s: str) -> bool:
    """
    Determine if a string is a palindrome.

    >>> is_palindrome("llol") # doctest: +SKIP
    False
    >>> is_palindrome("tacocat") # doctest: +SKIP
    True
    >>> is_palindrome("racecar") # doctest: +SKIP
    True
    """
    return


#5
def l_count(letter: str, word: str) -> int:
    """Number of times letter appears in word
    (using recursion only, with no other looping)
    >>> l_count("m", "mimosa") # doctest: +SKIP
    2
    >>> l_count("x", "mimosa") # doctest: +SKIP
    0
    >>> l_count("m", "") # doctest: +SKIP
    0
    """



#Nested data structures

#1
def most(collection: list[tuple[str, int]]) -> str:
    """Which element of the non-empty collection of (key, count) pairs
    has the greatest total count? (All counts are positive.)
    >>> most([("dogs", 3), ("cats", 5), ("dogs", 3)]) # doctest: +SKIP
    'dogs'
    >>> most([("dogs", 3), ("cats", 7), ("dogs", 3)]) # doctest: +SKIP
    'cats'
    """
    assert len(collection) > 0
    return


#2
def nested_contains(lst:list,target:int)->bool:
    """
    Checks if a nested contains a number

    >>> nested_contains([1, [2, [3, 4], 5], 6], 4) # doctest: +SKIP
    True
    >>> nested_contains([[1], [2, [3]], 4], 7) # doctest: +SKIP
    False
    >>> nested_contains([],1) # doctest: +SKIP
    False
    """
    return


#3
def sum_nested(lst:list)->int:
    """
    Recursively sums all integers in a nested list structure.

    >>> sum_nested([1, [2, [3, 4], 5], 6]) # doctest: +SKIP
    21
    >>> sum_nested([[[1], 2], 3]) # doctest: +SKIP
    6
    >>> sum_nested([]) # doctest: +SKIP
    0
    """
    return


#4
def total_scores(records: dict[str, list[int]]) -> dict[str, int]:
    """
    Given a dictionary where keys are student names and values are lists of test scores,
    return a new dictionary mapping each student to their total score (sum of their scores).

    >>> total_scores({"Alice": [80, 90], "Bob": [70, 85, 95], "Eve": []}) # doctest: +SKIP
    {'Alice': 170, 'Bob': 250, 'Eve': 0}
    >>> total_scores({}) # doctest: +SKIP
    {}
    >>> total_scores({"Tom": [100]}) # doctest: +SKIP
    {'Tom': 100}
    """
    return


#5
def max_sum_list(data: list[list[int]]) -> int:
    """
    Given a list of lists of integers, return the sum of inner list that has the greatest sum.

    >>> max_sum_list([[1, 2, 3], [4, 5], [0], [10]]) # doctest: +SKIP
    9
    >>> max_sum_list([[10, -5], [3, 3, 3], [6]]) # doctest: +SKIP
    9
    >>> max_sum_list([]) # doctest: +SKIP
    0
    >>> max_sum_list([[], [1], [2, -2]]) # doctest: +SKIP
    [1]
    """
    return



if __name__ == "__main__":
    doctest.testmod()  