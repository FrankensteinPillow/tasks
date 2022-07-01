from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map: defaultdict = defaultdict(int)
        for number in nums:
            hash_map[number] += 1
        for _, v in hash_map.items():
            if v > 1:
                return True
        return False

    def containsDuplicate_short(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


def test_havent_dublicates():
    nums: List[int] = [1, 2, 3, 4]
    s: Solution = Solution()
    assert s.containsDuplicate(nums) == False


def test_have_dublicates():
    nums: List[int] = [1, 2, 3, 4, 1]
    s: Solution = Solution()
    assert s.containsDuplicate(nums) == True


def test_one_elements():
    nums: List[int] = [1]
    s: Solution = Solution()
    assert s.containsDuplicate(nums) == False


def test_two_elements():
    nums: List[int] = [1, 2]
    s: Solution = Solution()
    assert s.containsDuplicate(nums) == False


def test_two_elements_duplicate():
    nums: List[int] = [1, 1]
    s: Solution = Solution()
    assert s.containsDuplicate(nums) == True


def test_have_dublicates_many():
    nums: List[int] = [1, 2, 3, 4, 1, 4, 4, 4, 4, 4, 4, 4]
    s: Solution = Solution()
    assert s.containsDuplicate(nums) == True


def test_havent_dublicates_short():
    nums: List[int] = [1, 2, 3, 4]
    s: Solution = Solution()
    assert s.containsDuplicate_short(nums) == False


def test_have_dublicates_short():
    nums: List[int] = [1, 2, 3, 4, 1]
    s: Solution = Solution()
    assert s.containsDuplicate_short(nums) == True


def test_one_elements_short():
    nums: List[int] = [1]
    s: Solution = Solution()
    assert s.containsDuplicate_short(nums) == False


def test_two_elements_short():
    nums: List[int] = [1, 2]
    s: Solution = Solution()
    assert s.containsDuplicate_short(nums) == False


def test_two_elements_duplicate_short():
    nums: List[int] = [1, 1]
    s: Solution = Solution()
    assert s.containsDuplicate_short(nums) == True


def test_have_dublicates_many_short():
    nums: List[int] = [1, 2, 3, 4, 1, 4, 4, 4, 4, 4, 4, 4]
    s: Solution = Solution()
    assert s.containsDuplicate_short(nums) == True
