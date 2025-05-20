import doctest

#Problem 1
def mystery(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return mystery(s[1:-1])

# print(mystery("radar")) #What does this print?
# print(mystery("robot")) #What does this print?


#Problem 2
def classify(n: int) -> str:
    keys = [1000, 100, 10, 0]
    labels = ["giant", "big", "modest", "small"]
    label = "unknown"
    for i in range(len(keys)):
        if n >= keys[i]:
            label = labels[i]
            break
    return label

a = 85
b = classify(a)
# print(a) #What does this print?
# print(b) #What does this print?


#Problem 3
def num_digits(n: int) -> int:
    digits = 1
    while n >= 10:
        n = n // 10
        digits += 1
    return digits

# print(num_digits(5)) #What does this print?
# print(num_digits(999)) #What does this print?
# print(num_digits(10000)) #What does this print?


#Problem 4
def grade(score: int) -> str:
    bounds = [90, 80, 70, 60]
    grades = ["A", "B", "C", "D"]
    for i in range(len(bounds)):
        if score >= bounds[i]:
            return grades[i]
    return "F"

# print(grade(92)) #What does this print?
# print(grade(75)) #What does this print?
# print(grade(58)) #What does this print?


#Problem 5
def scale(n: int) -> int:
    result = 1
    for i in range(n):
        if i % 2 == 0:
            result *= 2
        else:
            result += 1
    return result

# print(scale(0)) #What does this print?
# print(scale(3)) #What does this print?
# print(scale(5)) #What does this print?


#Problem 6
def sum_even(lst: list) -> int:
    """
    Recursively returns the sum of all elements in the list.

    >>> sum_even([1, 2, 3, 4]) # doctest: +SKIP
    6
    >>> sume_even([10]) # doctest: +SKIP
    10
    """
    return


#Problem 7
def contains(lst:list[int], target:int) -> bool:
    """
    Check if a list contains an integer non recursively
    >>> contains_non_recursive(4, [1, 3, 5, 7]) # doctest: +SKIP
    False
    >>> contains_non_recursive(4, [1, 3, 4, 7]) # doctest: +SKIP
    False
    >>> contains_non_recursive(2, [1]) # doctest: +SKIP
    False
    """
    return


#Problem 8
def most_frequent_word(lst:list[str]) -> str:
    """
    >>> most_frequent_word(["apple", "banana", "apple", "kiwi", "kiwi", "kiwi", "banana"]) # doctest: +SKIP
    "kiwi"
    >>> most_frequent_word(["cat","dog","horse","chicken","chicken"]]) # doctest: +SKIP
    "chicken"
    >>> most_frequent_word(["tucan"]]) # doctest: +SKIP
    "tucan"
    """
    return


#Problem 9
def most(collection: list[tuple[str, int]]) -> str:
    """Which element of the non-empty collection of (key, count) pairs
    has the greatest total count? (All counts are positive.) Hint: Think about how
    you solved the previous problem
    >>> most([("dogs", 3), ("cats", 5), ("dogs", 3)]) # doctest: +SKIP
    'dogs'
    >>> most([("dogs", 3), ("cats", 7), ("dogs", 3)]) # doctest: +SKIP
    'cats'
    """
    count_dict = {}
    for tuple in collection:
        if tuple[0] in count_dict.keys():
            count_dict[tuple[0]] += tuple[1] #Increment the count by the second element in the corresponding tuple
        else:
            count_dict[tuple[0]] = tuple[1] #Set the count equal to the second element in the corresponding tuple
        #Finish this function
    return


#Problem 10
def bsearch(k: str, table: list[tuple[str, str]]) -> str:
    """Lookup k in table, which is sorted in key order.
    Returns string "NOPE" if k is not present. Hint: Keys are the first element in
    each tuple, the keys are sorted alphabetically. 
    >>> bsearch("dog", [("cat", "feline"), ("dog", "canine")]) # doctest: +SKIP
    'canine'
    >>> bsearch("b", [("a", "x"), ("b", "y"), ("c", "z"), ("d", "z")]) # doctest: +SKIP
    'y'
    >>> bsearch("y", [("a", "x"), ("b", "y"), ("c", "z"), ("d", "z")]) # doctest: +SKIP
    'NOPE'
    """
    low = 0
    high = len(table)-1

    while low <= high:
        mid = (low+high)//2
        if table[mid][0] == k: #If key is equal to k
            return table[mid][1]
        #Finish this function
    return


if __name__ == "__main__":
    doctest.testmod()  # Automatically run the tests written in the docstrings