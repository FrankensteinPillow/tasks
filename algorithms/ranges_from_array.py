from random import randint
from typing import List, Set, Tuple, Dict


def get_ranges_with_sort(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Time complexity: O(nlogn)
    Memory complexity: O(1)
    """
    if not numbers:
        return []
    if len(numbers) == 1:
        return [(numbers[0], numbers[0])]
    numbers = sorted(numbers)  # <- O(nlogn) cause of that
    result: List[Tuple[int, int]] = []
    cur: int = numbers[0]
    prev: int = numbers[0]
    for number in numbers[1:]:
        if number - cur > 1:
            result.append((prev, cur))
            prev = number
        cur = number
    result.append((prev, cur))
    return result


def get_ranges(numbers: List[int]) -> List[Tuple[int, int]]:
    if not numbers:
        return []
    if len(numbers) < 2:
        return [(numbers[0], numbers[0])]
    result: List[Tuple[int, int]] = []
    tmp_result: Dict[int, int] = {}
    for number in numbers:
        if number - 1 in tmp_result:
            tmp_result[number - 1] = number
        elif number + 1 in tmp_result:
            tmp_result[number] = tmp_result[number + 1]
            del tmp_result[number + 1]
        else:
            tmp_result[number] = number
    print(tmp_result)
    return result


for _ in range(1):
    print("-" * 40)
    # numbers: Set[int] = {randint(-30, 30) for _ in range(randint(0, 30))}
    numbers: List[int] = [7, 5, 3, 1, 2, 4, 6,    16, 14, 12, 10, 11, 13, 15]
    print(f"{numbers=}")
    print(f"sorted numbers={sorted(numbers)}")
    print(get_ranges_with_sort(list(numbers)))
    print(get_ranges(list(numbers)))

