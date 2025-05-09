import doctest
#Note when you test the functions remove "# doctest: +SKIP" for each of the doctests

#Problem 1
def factorial(n: int) -> int:
    """
    Compute the factorial of a number.

    >>> factorial(4) # doctest: +SKIP
    24
    >>> factorial(5) # doctest: +SKIP
    120
    >>> factorial(6) # doctest: +SKIP
    720
    """
    pass 


#Problem 2
def sum_of_digits(n: int) -> int:
    """
    Compute the sum of all the digits in a number.

    >>> sum_of_digits(423) # doctest: +SKIP
    9
    >>> sum_of_digits(52) # doctest: +SKIP
    7
    >>> sum_of_digits(1493) # doctest: +SKIP
    17
    """
    pass


#Problem 3
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
    pass


#Problem 4
def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number (0-based indexing).

    >>> fibonacci(5) # doctest: +SKIP
    5
    >>> fibonacci(6) # doctest: +SKIP
    8
    >>> fibonacci(8) # doctest: +SKIP
    21
    """
    pass


#Problem 5
def sum_to_x(l: list[int], x: int) -> bool:
    """
    Determine if the numbers in a list sum to x.

    >>> sum_to_x([5, 7, 1], 13) # doctest: +SKIP
    True
    >>> sum_to_x([8, 3, 1, 1, 4], 12) # doctest: +SKIP
    False
    >>> sum_to_x([10, 3, 7], 20) # doctest: +SKIP
    True
    """
    pass


if __name__ == "__main__":
    doctest.testmod()