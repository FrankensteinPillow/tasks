from typing import List


def get_lost_permutation(numbers: List[int]) -> int:
    if not numbers:
        return 0
    num_sum: int = 0
    min_num: int = numbers[0]
    max_num: int = numbers[0]
    for n in numbers:
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n
        num_sum += n
    expected_sum: int = int((max_num - min_num + 1) * (max_num + min_num) / 2)
    return expected_sum - num_sum


numbers: List[List[int]] = [
    [-1, 0, 1, 2, 3, 4, 6, 7, -2, 8, 9],
    [0, 2],
    [],
    [1, 2],
    [9, 3, 4, 1, 5, 7, 6, 8],
    [-1, -2, -3, -5, -6, -7],
    [-1, -2, 1, 2, 3],
]
for nums in numbers:
    print("-" * 40)
    print(nums)
    print(get_lost_permutation(nums))
