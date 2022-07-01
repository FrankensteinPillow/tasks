from typing import List, Dict, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [-1, -1]
        sums: Dict[int, int] = {}
        for i, number in enumerate(nums):
            dif: int = target - number
            if dif not in sums:
                sums[dif] = i
            element: Optional[int] = sums.get(number)
            if element is not None and element != i:
                return [sums[number], i]
        return [-1, -1]


def test_simple():
    target: int = 12
    nums: List[int] = [1,2,3,4,5,6,7,8]
    assert Solution().twoSum(nums, target) == [4, 6]


def test_simple_with_negative():
    target: int = -11
    nums: List[int] = [-1,2,3,-4,5,6,-7,8]
    assert Solution().twoSum(nums, target) == [3, 6]


def test_simple_no_answer():
    target: int = 99
    nums: List[int] = [1,2,3,4,5,6,7,8]
    assert Solution().twoSum(nums, target) == [-1, -1]


def test_two_elements():
    target: int = 3
    nums: List[int] = [1,2]
    assert Solution().twoSum(nums, target) == [0, 1]
