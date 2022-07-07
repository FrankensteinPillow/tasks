# Task link: https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result: list[int] = []
        mem: dict[int, int] = {}
        for i, n1 in enumerate(nums1):
            for _, n2 in enumerate(nums2):
                if n1 == n2 and i not in mem:
                    result.append(n1)
                    mem[i] = n1
        return result


def test_simple():
    nums1: list[int] = [1,2,2,1]
    nums2: list[int] = [2,2]
    expected: list[int] = [2,2]
    assert Solution().intersect(nums1, nums2) == expected


def test_simple_2():
    nums1: list[int] = [1,2,2,1,9,9]
    nums2: list[int] = [4,4,5,6,8,8,9,1,4,4,9,1]
    expected: list[int] = [1,1,9,9]
    assert Solution().intersect(nums1, nums2) == expected