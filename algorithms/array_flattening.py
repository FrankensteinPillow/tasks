from typing import Any, List, Union


def flatten_recursive(data: List[Any]) -> List[int]:
    result: List[int] = []
    for element in data:
        if isinstance(element, list):
            result += flatten_recursive(element)
            continue
        result.append(element)
    return result


def flatten_iterative(data: List[Any]) -> List[int]:
    if not data:
        return []
    result: List[int] = []
    stack: List[Any] = []
    main_index: int = 0
    stack.append(data[main_index])
    while stack:
        element: Union[List[Any], int] = stack.pop()
        if isinstance(element, list):
            for i in range(len(element) - 1, -1, -1):
                stack.append(element[i])
            continue
        result.append(element)
        if not stack and main_index < len(data) - 1:
            main_index += 1
            stack.append(data[main_index])
    return result


list_numbers: List[List[Any]] = [
    [[], 1, 2, 3, [4], [5, 6, 7], [[8], [9], [10]], 11, [[[12, 13, 14], []]]],
    [],
    [[[1]]],
    [[1, 2, 3], 4],
    [1, 2, 3, 4, 5, [], [], [6, 7, [8, 9, [10, 11, [12]]]]],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [[[[[[1, 2, 3], 4, 5], 6, 7], 8, 9], 10, 11], 12, [13, 14, 15]],
    [-3, -2, -1, [[[1, 2, 3]], 4, [5, [6, [7, 8, 9, [10, [11]]]]], 12, 13]],
]
for numbers in list_numbers:
    print("-" * 40)
    print(numbers)
    print(flatten_recursive(numbers))
    print(flatten_iterative(numbers))
