from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if only negative numbers in array
        if all([n < 0 for n in nums]):
            return max(nums, default=0)
        accumulator: int = 0
        maximum: int = 0
        for number in nums:
            accumulator = max(0, accumulator + number)
            maximum = max(maximum, accumulator)
        return maximum


def test_simple():
    nums: List[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert Solution().maxSubArray(nums) == 6


def test_full_array():
    nums: List[int] = [5, 4, -1, 7, 8]
    assert Solution().maxSubArray(nums) == 23


def test_one_element():
    nums: List[int] = [1]
    assert Solution().maxSubArray(nums) == 1


def test_zero_elements():
    nums: List[int] = []
    assert Solution().maxSubArray(nums) == 0


def test_all_negative():
    nums: List[int] = [-1, -2, -3, -1, -3, -4, -5]
    assert Solution().maxSubArray(nums) == -1


def test_all_positive():
    nums: List[int] = [1, 2, 3, 1, 3, 4, 5]
    assert Solution().maxSubArray(nums) == 19


def test_all_zeros():
    nums: List[int] = [0, 0, 0, 0, 0]
    assert Solution().maxSubArray(nums) == 0


def test_stair():
    nums: List[int] = [-2, 2, -2, 2, -2, 2, -2, 2, -2]
    assert Solution().maxSubArray(nums) == 2


def test_stair_v():
    nums: List[int] = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert Solution().maxSubArray(nums) == 15
