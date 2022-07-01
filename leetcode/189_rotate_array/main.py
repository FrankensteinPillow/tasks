from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) <= 1:
            return
        k = len(nums) - k % len(nums)

        def reverse(arr: List[int], start: int, stop: int) -> None:
            mid: int = start + (stop - start) // 2
            for j, i in enumerate(range(start, mid + 1)):
                arr[i], arr[stop - j] = arr[stop - j], arr[i]

        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)


def test_rotate_by_three():
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7]
    s: Solution = Solution()
    s.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_by_five():
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7]
    s: Solution = Solution()
    s.rotate(nums, 5)
    assert nums == [3, 4, 5, 6, 7, 1, 2]


def test_rotate_by_four():
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7]
    s: Solution = Solution()
    s.rotate(nums, 4)
    assert nums == [4, 5, 6, 7, 1, 2, 3]


def test_rotate_by_two():
    nums: List[int] = [-1, -100, 3, 99]
    s: Solution = Solution()
    s.rotate(nums, 2)
    print(nums)
    assert nums == [3, 99, -1, -100]
