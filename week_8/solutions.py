import doctest

#Problem 1
def mystery(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return mystery(s[1:-1])

print(mystery("radar")) #Prints True
print(mystery("robot")) #Prints False


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
print(a) #Prints 85
print(b) #Prints modest


#Problem 3
def num_digits(n: int) -> int:
    digits = 1
    while n >= 10:
        n = n // 10
        digits += 1
    return digits

print(num_digits(5)) #Prints 1
print(num_digits(999)) #Prints 3
print(num_digits(10000)) #Prints 5


#Problem 4
def grade(score: int) -> str:
    bounds = [90, 80, 70, 60]
    grades = ["A", "B", "C", "D"]
    for i in range(len(bounds)):
        if score >= bounds[i]:
            return grades[i]
    return "F"

print(grade(92)) #Prints A
print(grade(75)) #Prints C
print(grade(58)) #Prints F


#Problem 5
def scale(n: int) -> int:
    result = 1
    for i in range(n):
        if i % 2 == 0:
            result *= 2
        else:
            result += 1
    return result

print(scale(0)) #Prints 0
print(scale(3)) #Prints 6
print(scale(5)) #Prints 14


#Problem 6
def sum_even(lst: list) -> int:
    """
    Recursively returns the sum of all elements in the list.

    >>> sum_even([1, 2, 3, 4]) 
    6
    >>> sum_even([10]) 
    10
    """
    if len(lst) == 0: #Base Case
        return 0
    elif lst[0] % 2 == 0: #if number is even
        return lst[0] + sum_even(lst[1:])
    else: #if number is odd
        return 0 + sum_even(lst[1:])


#Problem 7
def contains_non_recursive(target:int, lst:list[int]) -> bool:
    """
    Check if a list contains an integer non recursively
    >>> contains_non_recursive(4, [1, 3, 5, 7]) 
    False
    >>> contains_non_recursive(4, [1, 3, 4, 7]) 
    True
    >>> contains_non_recursive(2, [1]) 
    False
    """
    low = 0 #First index of list
    high = len(lst)-1 #Last index of list

    while low <= high: 
        mid = (low+high)//2 #Determine mid by floor dividing
        if lst[mid] == target: #Target is found
            return True
        elif lst[mid] > target: #Target is less than element at index mid
            high = mid-1
        else: #Target is greater than element at index mid
            low = mid+1
    return False


#Problem 8
def most_frequent_word(lst:list[str]) -> str:
    """
    >>> most_frequent_word(["apple", "banana", "apple", "kiwi", "kiwi", "kiwi", "banana"])
    'kiwi'
    >>> most_frequent_word(["cat","dog","horse","chicken","chicken"]) 
    'chicken'
    >>> most_frequent_word(["tucan"]) 
    'tucan'
    """
    word_count = {}
    for word in lst:
        if word in word_count.keys(): #If word is in the dictionary increment it's count by 1
            word_count[word] += 1 
        else: #Otherwise set it's count to 1
            word_count[word] = 1  
    
    appears_most = None #Word that appears most
    num_appearances = 0 #The number of times it appears
    for word in word_count.keys():
        if appears_most == None: #If appears_most doesn't have a value yet
            appears_most = word 
            num_appearances = word_count[word]
        elif word_count[word] > num_appearances:  #If appears_most appears less than the current word
            appears_most = word
            num_appearances = word_count[word]
    return appears_most


#Problem 9
def most(collection: list[tuple[str, int]]) -> str:
    """Which element of the non-empty collection of (key, count) pairs
    has the greatest total count? (All counts are positive.)
    >>> most([("dogs", 3), ("cats", 5), ("dogs", 3)]) 
    'dogs'
    >>> most([("dogs", 3), ("cats", 7), ("dogs", 3)])
    'cats'
    """
    count_dict = {}
    for tuple in collection:
        if tuple[0] in count_dict.keys():
            count_dict[tuple[0]] += tuple[1] #Increment the count by the second element in the corresponding tuple
        else:
            count_dict[tuple[0]] = tuple[1] #Set the count equal to the second element in the corresponding tuple

    highest_key = None #Key that appears most
    max_count = 0 #Number of times that key appears
    for word in count_dict.keys():
        if highest_key == None: #If highest_key doesn't have a value yet
            highest_key = word 
            max_count = count_dict[word]
        elif count_dict[word] > max_count: #If highest_key appears less than the current word
            highest_key = word
            max_count = count_dict[word]
    return highest_key

   
#Problem 10
def bsearch(k: str, table: list[tuple[str, str]]) -> str:
    """Lookup k in table, which is sorted in key order.
    Returns string "NOPE" if k is not present.
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
        elif table[mid][0] > k: #If key is less than k
            high = mid-1
        else: #If key is more than k
            low = mid+1
    return "Nope"
    


if __name__ == "__main__":
    doctest.testmod()  #Automatically run the tests written in the docstrings