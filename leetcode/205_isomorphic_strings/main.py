# Task link: https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t: dict[str, str] = {}
        t_to_s: dict[str, str] = {}
        for index, symbol in enumerate(s):
            if (
                s_to_t.setdefault(symbol, t[index]) != t[index]
                or t_to_s.setdefault(t[index], symbol) != symbol
            ):
                return False
        return True


def test_example_1():
    s: str = "egg"
    t: str = "add"
    result: bool = Solution().isIsomorphic(s, t)
    expected: bool = True
    assert expected == result


def test_example_2():
    s: str = "paper"
    t: str = "title"
    result: bool = Solution().isIsomorphic(s, t)
    expected: bool = True
    assert expected == result


def test_example_negative():
    s: str = "foo"
    t: str = "bar"
    result: bool = Solution().isIsomorphic(s, t)
    expected: bool = False
    assert expected == result


def test_two_diff_words():
    s: str = "glance"
    t: str = "cinder"
    result: bool = Solution().isIsomorphic(s, t)
    expected: bool = True
    assert expected == result


def test_1():
    s: str = "ggllaa"
    t: str = "cciinn"
    result: bool = Solution().isIsomorphic(s, t)
    expected: bool = True
    assert expected == result


def test_2():
    s: str = "gglaal"
    t: str = "ccinng"
    result: bool = Solution().isIsomorphic(s, t)
    expected: bool = False
    assert expected == result


def test_wrong_anser_1():
    s: str = "badc"
    t: str = "baba"
    result: bool = Solution().isIsomorphic(s, t)
    expected: bool = False
    assert expected == result
