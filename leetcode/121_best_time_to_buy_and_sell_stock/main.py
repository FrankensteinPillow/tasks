# Task link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def brute_force_solution(self, prices: list[int]) -> int:
        """
        Time complexity: O(n^2)
        Memory complexity: O(1)
        """
        result: int = 0
        for i, v1 in enumerate(prices):
            for v2 in prices[i:]:
                if (res := v2 - v1) > result:
                    result = res
        return result

    def half_split_solution(self, prices: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Memory complexity: O(n)
        """
        result: int = 0
        len_prices: int = len(prices)
        if len_prices < 2:
            return result
        mid: int = len_prices // 2
        stack: list[tuple[list[int], list[int]]] = [
            (prices[:mid], prices[mid:])
        ]
        while stack:
            left, right = stack.pop()
            min1: int = min(left)
            max2: int = max(right)
            result = max(max2 - min1, result)
            if len(left) >= 2:
                mid = len(left) // 2
                stack.append((left[:mid], left[mid:]))
            if len(right) >= 2:
                mid = len(right) // 2
                stack.append((right[:mid], right[mid:]))
        return result

    def one_traversal(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Memory complexity: O(1)
        """
        min_elem: float = float("inf")
        max_profit: float = 0
        for price in prices:
            min_elem = min(price, min_elem)
            max_profit = max(price - min_elem, max_profit)
        return int(max_profit)

    def maxProfit(self, prices: list[int]) -> int:
        return self.one_traversal(prices)


def test_simple():
    prices: list[int] = [7, 1, 5, 3, 6, 4]
    max_profit: int = 5
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_simple_2():
    prices: list[int] = [7, 6, 4, 3, 1]
    max_profit: int = 0
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_negatives():
    prices: list[int] = [-5, -4, -3, -2, -1]
    max_profit: int = 4
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_flat():
    prices: list[int] = [1, 1, 1, 1, 1, 1]
    max_profit: int = 0
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_flat_except_one():
    prices: list[int] = [1, 1, 1, 1, 2, 1]
    max_profit: int = 1
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_flat_except_one_in_end():
    prices: list[int] = [1, 1, 1, 1, 1, 2]
    max_profit: int = 1
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_curve():
    prices: list[int] = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]
    max_profit: int = 6
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_wave():
    prices: list[int] = [
        7,
        6,
        5,
        4,
        3,
        2,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        5,
        3,
        1,
        0,
        13,
        55,
        70,
    ]
    max_profit: int = 70
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_one_price():
    prices: list[int] = [13]
    max_profit: int = 0
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_two_days():
    prices: list[int] = [0, 13]
    max_profit: int = 13
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_two_days_reverse():
    prices: list[int] = [13, 0]
    max_profit: int = 0
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_flat_except_first():
    prices: list[int] = [9, 1, 1, 1, 1, 1]
    max_profit: int = 0
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_pit():
    prices: list[int] = [3, 2, 3, -99, 4, 5, 100]
    max_profit: int = 199
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


def test_double_pit():
    prices: list[int] = [-100, 3, 2, 3, -99, 4, 5, 100]
    max_profit: int = 200
    result: int = Solution().maxProfit(prices)
    assert result == max_profit


# test_wave()
