import doctest

#Problem 1
def count_keys(d):
    """
    Recursively counts all keys in a nested dictionary.

    >>> count_keys({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}, 'f': 4}) # doctest: +SKIP
    6
    >>> count_keys({}) # doctest: +SKIP
    0
    >>> count_keys({'x': {'y': {'z': {}}}}) # doctest: +SKIP
    3
    """
    return


#Problem 2
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


#Problem 3
def sum_values(d:dict)->int:
    """
    Sum all of the values in a nested dictionary

    >>> sum_values({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}, 'f': 4}) # doctest: +SKIP
    10
    >>> sum_values({}) # doctest: +SKIP
    0
    >>> sum_values({'x': {'y': {'z': 2}}}) # doctest: +SKIP
    2
    """
    return


#Problem 4
def flatten(lst:list)->list:
    """
    Recursively flattens a nested list into a single list.

    >>> flatten([1, [2, [3, 4], 5], 6]) # doctest: +SKIP
    [1, 2, 3, 4, 5, 6]
    >>> flatten([[1], [2, [3]], 4]) # doctest: +SKIP
    [1, 2, 3, 4]
    >>> flatten([]) # doctest: +SKIP
    []
    """
    return


#Problem 5
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


#Problem 6
def max_depth(structure:list)->int:
    """
    Recursively finds the maximum depth of a nested list.

    >>> max_depth([1, [2, [3, [4]]]]) # doctest: +SKIP
    4
    >>> max_depth([1, [2, [3, 4], 5], 6]) # doctest: +SKIP
    3
    >>> max_depth([5]) # doctest: +SKIP
    1
    """
    return


#Problem 7
def highest_caloriest(calorie_dict: dict[str, dict[str, int]]) -> str:
    """
    Given a dictionary where each key is a food item and the value is a 
    nested dictionary mapping its ingredients to their respective calorie counts,
    return the name of the food item with the highest total calorie count.

    Doctests:
    >>> foods = {
    ...     "Burger": {"Bun": 120, "Patty": 300, "Cheese": 100},
    ...     "Salad": {"Lettuce": 10, "Tomato": 15, "Dressing": 80},
    ...     "Pizza": {"Dough": 200, "Cheese": 150, "Pepperoni": 250}
    ... }
    >>> highest_caloriest(foods) # doctest: +SKIP
    'Pizza'

    >>> highest_caloriest({"Apple": {"Apple": 95}}) # doctest: +SKIP
    'Apple'

    >>> highest_caloriest({}) # doctest: +SKIP
    ''
    """
    return


if __name__ == "__main__":
    doctest.testmod()  
