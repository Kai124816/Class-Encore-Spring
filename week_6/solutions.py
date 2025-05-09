import doctest

#Binary Search Solutions

#Problem 1
def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target's index.

    >>> binary_search([1, 3, 5, 7, 9], 5) 
    2
    >>> binary_search([1, 3, 5, 7, 9], 6) 
    -1
    >>> binary_search([], 1)
    -1
    """
    left = 0
    right = len(arr) - 1
    result = -1  # Default if target not found

    while left <= right:
        mid = (left + right) // 2  # Calculate midpoint
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return result  # Return -1 if not found

    
#Problem 2
def find_first(arr, target):
    """
    Find the first position of a target in a sorted array. Return -1 if
    you can't find the target

    >>> find_first([1, 2, 2, 2, 3, 4], 2) 
    1
    >>> find_first([1, 2, 3, 4], 5) 
    -1
    >>> find_first([], 1) 
    -1
    """
    left = 0
    right = len(arr) - 1
    result = -1  # Store result if found

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid       # Update result and continue left
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1     # Move to right half
        else:
            right = mid - 1    # Move to left half

    return result


#Problem 3
def search_insert_position(arr, target):
    """
    Find the index where target should be inserted in sorted array.

    >>> search_insert_position([1, 3, 5, 6], 5)
    2
    >>> search_insert_position([1, 3, 5, 6], 2) 
    1
    >>> search_insert_position([1, 3, 5, 6], 7) 
    4
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Move right
        else:
            right = mid - 1  # Move left

    return left  # Left is insertion point



#Problem 4
def sqrt_int(x):
    """
    Compute the integer square root of a non-negative integer.
    Return -1 if no square root exists

    >>> sqrt_int(8) 
    -1
    >>> sqrt_int(16) 
    4
    >>> sqrt_int(1) 
    1
    >>> sqrt_int(0)
    0
    """
    if x == 0 or x == 1:
        return x  # Edge case

    high = x // 2
    low = 1

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == x:
            return mid  # Exact square root found
        elif mid * mid < x:
            low = mid + 1  # Search higher
        else:
            high = mid - 1  # Search lower

    return -1  # No integer square root



#Problem 5
def find_first_with_prefix(words, target):
    """
    Returns the index of the first word which matches the target word in a sorted list.
    Hint if a word comes before another word in alphabetical order it's value is less than 
    that other word's. For example "apple" < "banana".

    >>> find_first_with_prefix(["apple", "banana", "cherry", "date", "fig", "grape"], "cherry")
    2
    >>> find_first_with_prefix(["apple", "banana", "banana", "banana", "cherry"], "banana")
    1
    >>> find_first_with_prefix(["apple", "banana", "cherry"], "kiwi")
    -1
    >>> find_first_with_prefix([], "any")
    -1
    """
    high = len(words) - 1
    low = 0
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if words[mid] == target:
            result = mid        # Found match
            high = mid - 1      # Check for earlier match
        elif words[mid] < target:
            low = mid + 1       # Move right
        else:
            high = mid - 1      # Move left

    return result

    

#Recursion Problems

#Problem 1
def factorial(n: int) -> int:
    """
    Compute the factorial of a number.

    >>> factorial(4) 
    24
    >>> factorial(5) 
    120
    >>> factorial(6) 
    720
    """
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive call



#Problem 2
def sum_of_digits(n: int) -> int:
    """
    Compute the sum of all the digits in a number.

    >>> sum_of_digits(423) 
    9
    >>> sum_of_digits(52) 
    7
    >>> sum_of_digits(1493) 
    17
    """
    if n < 10:
        return n  # Base case
    return (n % 10) + sum_of_digits(n // 10)  # Last digit + recurse on rest



#Problem 3
def is_palindrome(s: str) -> bool:
    """
    Determine if a string is a palindrome.

    >>> is_palindrome("llol") 
    False
    >>> is_palindrome("tacocat") 
    True
    >>> is_palindrome("racecar") 
    True
    """
    if len(s) <= 1:
        return True  # Base case: empty or one-char string
    if s[0] != s[-1]:
        return False  # Mismatch
    return is_palindrome(s[1:-1])  # Recurse on substring


#Problem 4
def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number (0-based indexing).

    >>> fibonacci(5) 
    5
    >>> fibonacci(6) 
    8
    >>> fibonacci(8) 
    21
    """
    if n == 1 or n == 2:
        return 1  # Base cases
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive relation



#Problem 5
def sum_to_x(l: list[int], x: int) -> bool:
    """
    Determine if the numbers in a list sum to x.

    >>> sum_to_x([5, 7, 1], 13) 
    True
    >>> sum_to_x([8, 3, 1, 1, 4], 12)
    False
    >>> sum_to_x([10, 3, 7], 20) 
    True
    """
    if len(l) == 1:
        return l[0] == x  # Base case: single element
    return sum_to_x(l[1:], x - l[0])  # Try including current element



if __name__ == "__main__":
    doctest.testmod()