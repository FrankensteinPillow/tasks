# Task link: https://leetcode.com/problems/reshape-the-matrix/


class Solution:
    def matrixReshape(
        self, mat: list[list[int]], r: int, c: int
    ) -> list[list[int]]:
        len_rows: int = len(mat)
        len_cols: int = len(mat[0])
        if len_rows * len_cols != r * c:
            return mat
        result: list[list[int]] = [[0 for _ in range(c)] for _ in range(r)]
        i = j = 0
        for row in mat:
            for value in row:
                result[i][j] = value
                j += 1
                if j == c:
                    j = 0
                    i += 1
        return result


def test_simple_negative():
    mat: list[list[int]] = [[1, 2], [3, 4]]
    expected: list[list[int]] = [[1, 2], [3, 4]]
    assert Solution().matrixReshape(mat, 2, 4) == expected


def test_negative():
    mat: list[list[int]] = [[1, 2], [3, 4]]
    expected: list[list[int]] = [[1, 2], [3, 4]]
    assert Solution().matrixReshape(mat, 3, 5) == expected


def test_simple():
    mat: list[list[int]] = [[1, 2], [3, 4]]
    expected: list[list[int]] = [[1, 2, 3, 4]]
    assert Solution().matrixReshape(mat, 1, 4) == expected


def test_simple_reverse():
    mat: list[list[int]] = [[1, 2], [3, 4]]
    expected: list[list[int]] = [[1], [2], [3], [4]]
    assert Solution().matrixReshape(mat, 4, 1) == expected


def test_2x3_to_3x2():
    mat: list[list[int]] = [[1, 2, 3], [3, 4, 5]]
    expected: list[list[int]] = [[1, 2], [3, 3], [4, 5]]
    assert Solution().matrixReshape(mat, 3, 2) == expected


def test_3x2_to_2x3():
    mat: list[list[int]] = [[1, 2], [3, 3], [4, 5]]
    expected: list[list[int]] = [[1, 2, 3], [3, 4, 5]]
    assert Solution().matrixReshape(mat, 2, 3) == expected


def test_1x9_to_3x3():
    mat: list[list[int]] = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    expected: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().matrixReshape(mat, 3, 3) == expected


def test_3x3_to_1x9():
    mat: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected: list[list[int]] = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert Solution().matrixReshape(mat, 1, 9) == expected
