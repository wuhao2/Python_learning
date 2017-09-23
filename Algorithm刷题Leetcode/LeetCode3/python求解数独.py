# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 9:17'


class Suduko(object):
    def __init__(self, s):
        self.s = s

    def check_all(self, i, j, value):
        # 检测s[i][j]=value时，是否满足数独约束
        return self.check_row(i, j, value) \
               and self.check_column(i, j, value) \
               and self.check_small_sudoku(i, j, value)

    def check_row(self, i, j, value):
        # 检测s[i][j]=value是否满足 行中不允许重复数字
        return value not in self.s[i]

    def check_column(self, i, j, value):
        # 检测s[i][j]=value是否满足 列中不允许重复数字
        column = [self.s[v][j] for v in range(9)]
        return value not in column

    def check_small_sudoku(self, i, j, value):
        # 检测s[i][j]=value是否满足 小九宫格不允许重复数字
        small_sudoku = [self.s[m][n] for m in range(i // 3 * 3, (i // 3 + 1) * 3)
                        for n in range(j // 3 * 3, (j // 3 + 1) * 3)]
        return value not in small_sudoku

    def recursion_search(self):
        # 回溯求解，如果i,j都大于等于8，表示求解OK
        i, j = self.start_point()
        if i >= 8 and j >= 8 and self.s[8][8]:
            return True

        for value in range(1, 10):
            if self.check_all(i, j, value):
                self.s[i][j] = value  # 如果s[i][j]满足约束，则令s[i][j]=value
                if not self.recursion_search():
                    self.s[i][j] = 0  # 如果后面的递归搜索不满足要求，令s[i][j] = 0
                else:
                    return True
        return False  # 如果该点遍历1-9都不符合要求，则表示上游选值不当，回溯

    def start_point(self):
        for i in range(9):
            for j in range(9):
                if not self.s[i][j]:
                    return i, j
        return i, j


if '__main__' == __name__:
    import time
    s = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 9, 0, 2, 0, 0],
         [0, 5, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 0, 4, 5, 7, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 3, 0],
         [0, 0, 1, 0, 0, 0, 0, 6, 8],
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    S = Suduko(s)
    start = time.time()
    S.recursion_search()
    end = time.time()
    print("used time:", end-start)
    for i in range(9):
        print(S.s[i])

