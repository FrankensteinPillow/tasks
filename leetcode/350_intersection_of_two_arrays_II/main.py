# Task link: https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect_brute_force(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result: list[int] = []
        mem1: dict[int, int] = {}
        mem2: dict[int, int] = {}
        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                if n1 == n2 and i not in mem1 and j not in mem2:
                    result.append(n1)
                    mem1[i] = n1
                    mem2[j] = n2
        return result

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter_nums1: dict[int, int] = {}
        counter_nums2: dict[int, int] = {}
        result: list[int] = []
        for number in nums1:
            if number not in counter_nums1:
                counter_nums1[number] = 1
                continue
            counter_nums1[number] += 1
        for number in nums2:
            if number not in counter_nums2:
                counter_nums2[number] = 1
                continue
            counter_nums2[number] += 1
        for k, v in counter_nums1.items():
            value: int | None = counter_nums2.get(k)
            if value is not None:
                if value <= v:
                    result.extend([k] * value)
                else:
                    result.extend([k] * v)
        return result


def test_simple_brute_force():
    nums1: list[int] = [1, 2, 2, 1]
    nums2: list[int] = [2, 2]
    expected: list[int] = [2, 2]
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_simple_2_brute_force():
    nums1: list[int] = [1, 2, 2, 1, 9, 9]
    nums2: list[int] = [4, 4, 5, 6, 8, 8, 9, 1, 4, 4, 9, 1]
    expected: list[int] = [1, 1, 9, 9]
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_empty_result_brute_force():
    nums1: list[int] = [1]
    nums2: list[int] = [2]
    expected: list[int] = []
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_empty_result_2_brute_force():
    nums1: list[int] = [1, 2, 3, 4]
    nums2: list[int] = [9, 9, 9, 6, 6, 6]
    expected: list[int] = []
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_one_element_in_nums2_brute_force():
    nums1: list[int] = [1, 2, 2, 1]
    nums2: list[int] = [2]
    expected: list[int] = [2]
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_two_element_in_nums2_brute_force():
    nums1: list[int] = [1, 2, 2, 2, 1]
    nums2: list[int] = [2, 2]
    expected: list[int] = [2, 2]
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_one_element_in_nums1_brute_force():
    nums1: list[int] = [1]
    nums2: list[int] = [2, 2, 1, 1, 1]
    expected: list[int] = [1]
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_two_element_in_nums1_brute_force():
    nums1: list[int] = [1, 1]
    nums2: list[int] = [2, 2, 1, 1, 1]
    expected: list[int] = [1, 1]
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_one_elements_in_each_brute_force():
    nums1: list[int] = [3]
    nums2: list[int] = [3]
    expected: list[int] = [3]
    assert Solution().intersect_brute_force(nums1, nums2) == expected


def test_simple():
    nums1: list[int] = [1, 2, 2, 1]
    nums2: list[int] = [2, 2]
    expected: list[int] = [2, 2]
    assert Solution().intersect(nums1, nums2) == expected


def test_simple_2():
    nums1: list[int] = [1, 2, 2, 1, 9, 9]
    nums2: list[int] = [4, 4, 5, 6, 8, 8, 9, 1, 4, 4, 9, 1]
    expected: list[int] = [1, 1, 9, 9]
    assert Solution().intersect(nums1, nums2) == expected


def test_empty_result():
    nums1: list[int] = [1]
    nums2: list[int] = [2]
    expected: list[int] = []
    assert Solution().intersect(nums1, nums2) == expected


def test_empty_result_2():
    nums1: list[int] = [1, 2, 3, 4]
    nums2: list[int] = [9, 9, 9, 6, 6, 6]
    expected: list[int] = []
    assert Solution().intersect(nums1, nums2) == expected


def test_one_element_in_nums2():
    nums1: list[int] = [1, 2, 2, 1]
    nums2: list[int] = [2]
    expected: list[int] = [2]
    assert Solution().intersect(nums1, nums2) == expected


def test_two_element_in_nums2():
    nums1: list[int] = [1, 2, 2, 2, 1]
    nums2: list[int] = [2, 2]
    expected: list[int] = [2, 2]
    assert Solution().intersect(nums1, nums2) == expected


def test_one_element_in_nums1():
    nums1: list[int] = [1]
    nums2: list[int] = [2, 2, 1, 1, 1]
    expected: list[int] = [1]
    assert Solution().intersect(nums1, nums2) == expected


def test_two_element_in_nums1():
    nums1: list[int] = [1, 1]
    nums2: list[int] = [2, 2, 1, 1, 1]
    expected: list[int] = [1, 1]
    assert Solution().intersect(nums1, nums2) == expected


def test_one_elements_in_each():
    nums1: list[int] = [3]
    nums2: list[int] = [3]
    expected: list[int] = [3]
    assert Solution().intersect(nums1, nums2) == expected
