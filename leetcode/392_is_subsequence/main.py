# Task link: https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False
        i = j = 0
        results: list[bool] = [False] * len(s)
        while True:
            if i >= len(s) or j >= len(t):
                break
            if s[i] == t[j]:
                results[i] = True
                i += 1
            j += 1
        return all(results)


def test_1():
    s: str = "egg"
    t: str = "add"
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = False
    assert expected == result


def test_2():
    s: str = "egg"
    t: str = "lkajsdfeeeepww.w.ccnnssgcg"
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = True
    assert expected == result


def test_example_1():
    s: str = "abc"
    t: str = "ahbgdc"
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = True
    assert expected == result


def test_example_2():
    s: str = "axc"
    t: str = "ahbgdc"
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = False
    assert expected == result


def test_wrong_answer_1():
    s: str = "acb"
    t: str = "ahbgdc"
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = False
    assert expected == result


def test_empty_1():
    s: str = ""
    t: str = "ahbgdc"
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = True
    assert expected == result


def test_empty_2():
    s: str = ""
    t: str = ""
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = True
    assert expected == result


def test_empty_3():
    s: str = "lkjasdf"
    t: str = ""
    result: bool = Solution().isSubsequence(s, t)
    expected: bool = False
    assert expected == result
