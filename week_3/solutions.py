import doctest

"1. [10 points] What does this program print?"

def f(x: int) -> int:
    x = x + 1
    return x
x = 5
y = 7
z = f(y)

print(f"x={x}, y={y}, z={z}") 
# prints x=5, y=7, z=8



"2. [15 points] What does this program print?"

CATS = ["tiger", "lion", "cougar", "leopard"]
ANIMALS = ["horse", "cougar", "dog", "tiger"]
def is_feline(animal: str) -> bool:
    """Does it purr? Does it have sharp teeth?"""
    for cat in CATS:
        if animal == cat:
            return True
    return False

def pet_chooser(choices: list[str]) -> list[str]:
    """Which animals would make good pets?"""
    selection = []
    for choice in choices:
        if is_feline(choice):
            selection.append(choice)
    return selection

print(pet_chooser(ANIMALS))
#prints ['cougar', 'tiger']

"3. [25 points] Complete function count_one_value."

def count_one_value(k: str, li: list[str]) -> int:
    """How many occurrences of k are in li?
    >>> count_one_value("duck", ["duck", "goose", "duck", "duck"])
    3
    >>> count_one_value("t-rex", ["duck", "goose", "duck", "duck"])
    0
    """
    counter = 0
    for el in li:
        if el == k:
            counter += 1
    return counter


"4. [25 points] Complete function count_all_values."

def count_all_values(li: list[str]) -> dict[str, int]:
    """Returns dict with counts of strings in li.
    >>> count_all_values(["carrot", "chocolate", "carrot", "strawberry"])
    {'carrot': 2, 'chocolate': 1, 'strawberry': 1}
    >>> count_all_values([])
    {}
    """
    val_dict = {}
    for el in li:
        if el in val_dict:
            val_dict[el] += 1
        else:
            val_dict[el] = 1
    return val_dict


"5. [25 points] Complete function select_by_value."

def select_by_value(min_val: int, li: list[str], values: dict[str, int]) -> list[str]:
    """Returns list of elements of li associated with a value at least min_val in values.
    (Assume all elements in li are keys in values)
    >>> select_by_value(5, ["dog", "cat", "rabbit"], {"cat": 7, "rabbit": 3, "dog": 9})
    ['dog', 'cat']
    >>> select_by_value(17, ["dog", "cat", "rabbit"], {"cat": 12, "rabbit": 4, "dog": 9})
    []
    """
    new_li = []
    for el in li:
        if values[el] > min_val:
            new_li.append(el)
    return new_li


"Bonus problem 1:"
"""
Finish function count_ge. The input (formal arguments)
of count_ge are:
- nums: a list of zero or more integers
- at_least: an integer value
The result of count_ge should be the number of elements of nums
whose value is at least (i.e., greater than or equal to) at_least.
count_ge should not have an effect, only a result.
I have provided a few doctests. I will use additional tests in grading.
"""
def count_ge(nums: list[int], at_least: int) -> int:
    """Returns a count of elements in nums whose value is
    at least (>=) at_least.
    >>> count_ge([1, 2, 3, 4, 5], 3)
    3
    >>> count_ge([-10, 17, -3, 5], 0)
    2
    >>> count_ge([], 0)
    0
    >>> count_ge([7, 12, 17], 99)
    0
    """
    count = 0
    for num in nums:
        if num >= at_least:
            count += 1
    return count



"Bonus problem 2:"
"""
Return the longest string from a list of strings.
Input (formal) arguments: words, a non-empty list of strings
Return value: The element of words that is longest.
In case of a tie, return the first word with the greatest length.
Recall that len(s) returns the length of string s.
"""
def longest_word(words: list[str]) -> str:
    """Return the longest element of words.
    >>> longest_word(['we', 'know', 'how', 'to', 'select', 'extremes'])
    'extremes'
    >>> longest_word(['we', 'already', 'know', 'how'])
    'already'
    >>> longest_word(['really?'])
    'really?'
    """
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


if __name__ == "__main__":
    doctest.testmod()




