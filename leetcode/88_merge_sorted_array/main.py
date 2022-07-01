from typing import List


class Solution:
    def merge(
        self, nums1: List[int], n: int, nums2: List[int], m: int
    ) -> None:
        result: List[int] = []
        i: int = 0
        j: int = 0
        while i != n and j != m:
            if nums2[j] < nums1[i]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                i += 1
        if j < m:
            result.extend(nums2[j:])
        if i < n:
            # here from i to n because first array represented as arr[n + m]
            result.extend(nums1[i:n])
        nums1[:] = result[:]


def test_simple_second_lower():
    arr1: List[int] = [4,5,6,0,0,0]
    arr2: List[int] = [1,2,3]
    result: List[int] = [1,2,3,4,5,6]
    Solution().merge(arr1, 3, arr2, 3)
    assert arr1 == result


def test_empty_array():
    arr1: List[int] = [0, 0, 0]
    arr2: List[int] = [2,5,6]
    result: List[int] = [2,5,6]
    Solution().merge(arr1, 0, arr2, 3)
    assert arr1 == result


def test_simple():
    arr1: List[int] = [1,2,3,0,0,0]
    arr2: List[int] = [2,5,6]
    result: List[int] = [1,2,2,3,5,6]
    Solution().merge(arr1, 3, arr2, 3)
    assert arr1 == result


def test_equal_arrays():
    arr1: List[int] = [1, 1, 1,0,0,0]
    arr2: List[int] = [1,1,1]
    result: List[int] = [1,1,1,1,1,1]
    Solution().merge(arr1, 3, arr2, 3)
    assert arr1 == result


def test_empty_second_array():
    arr1: List[int] = [1, 1, 1]
    arr2: List[int] = []
    result: List[int] = [1, 1, 1]
    Solution().merge(arr1, 3, arr2, 0)
    assert arr1 == result


def test_empty_second_array_first_len_one():
    arr1: List[int] = [1]
    arr2: List[int] = []
    result: List[int] = [1]
    Solution().merge(arr1, 3, arr2, 0)
    assert arr1 == result


def test_negative_second():
    arr1: List[int] = [0,0,0]
    arr2: List[int] = [-3, -2, -1]
    result: List[int] = [-3, -2, -1]
    Solution().merge(arr1, 0, arr2, 3)
    assert arr1 == result


def test_negative_second():
    arr1: List[int] = [-6,6,9, 0, 0, 0]
    arr2: List[int] = [-3, -2, -1]
    result: List[int] = [-6, -3, -2, -1, 6, 9]
    Solution().merge(arr1, 3, arr2, 3)
    assert arr1 == result