import doctest

#Problem 1
def count_keys(d):
    """
    Recursively counts all keys in a nested dictionary.

    >>> count_keys({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}, 'f': 4})
    6
    >>> count_keys({})
    0
    >>> count_keys({'x': {'y': {'z': {}}}})
    3
    """
    count = 0
    for key, value in d.items():
        count += 1
        if isinstance(value, dict):
            count += count_keys(value)
    return count


#Problem 2
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
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total


#Problem 3
def sum_values(d:dict)->int:
    """
    Sum all of the values in a nested dictionary

    >>> sum_values({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}, 'f': 4})
    10
    >>> sum_values({})
    0
    >>> sum_values({'x': {'y': {'z': 2}}})
    2
    """
    count = 0
    for key, value in d.items():
        if isinstance(value, dict):
            count += sum_values(value)
        else:
            count += value
    return count


#Problem 4
def flatten(lst:list)->list:
    """
    Recursively flattens a nested list into a single list.

    >>> flatten([1, [2, [3, 4], 5], 6])
    [1, 2, 3, 4, 5, 6]
    >>> flatten([[1], [2, [3]], 4])
    [1, 2, 3, 4]
    >>> flatten([])
    []
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result = result + flatten(item)
        else:
            result.append(item)
    return result


#Problem 5
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
    for item in lst:
        if isinstance(item, list):
            if nested_contains(item,target) == True:
                return True
        else:
            if item == target:
                return True
    return False


#Problem 6
def max_depth(structure:list)->int:
    """
    Recursively finds the maximum depth of a nested list.

    >>> max_depth([1, [2, [3, [4]]]])
    4
    >>> max_depth([1, [2, [3, 4], 5], 6])
    3
    >>> max_depth([5])
    1
    """
    depth_max = 1
    for item in structure:
        if isinstance(item, list):
            depth = 1 + max_depth(item)
            if depth > depth_max:
                depth_max = depth
    return depth_max


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
    >>> highest_caloriest(foods)
    'Pizza'

    >>> highest_caloriest({"Apple": {"Apple": 95}})
    'Apple'

    >>> highest_caloriest({})
    ''
    """
    high_count = 0
    most_cals = ''

    for food in calorie_dict.keys():
        nested_dict = calorie_dict[food]
        calorie_count = 0
        for ingredient in nested_dict.keys():
            calorie_count += nested_dict[ingredient]
        if calorie_count > high_count:
            high_count = calorie_count
            most_cals = food
    return most_cals


if __name__ == "__main__":
    doctest.testmod()  
