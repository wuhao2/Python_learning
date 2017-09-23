# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 9:02'


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):  # 行和列是否符合数独
            tmp = []
            tmp1 = []
            for j in range(9):
                tmp.append(board[i][j])
                tmp1.append(board[j][i])
            if self.isnodifferent(tmp) == False or self.isnodifferent(tmp1) == False:
                return False  # 如果行和列出现重复数字，则返回错

        """判断九宫格是否有相同的数字"""
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp = []
                tmp.append(board[i][j])
                tmp.append(board[i][j + 1])
                tmp.append(board[i][j + 2])
                tmp.append(board[i + 1][j])
                tmp.append(board[i + 1][j + 1])
                tmp.append(board[i + 1][j + 2])
                tmp.append(board[i + 2][j])
                tmp.append(board[i + 2][j + 1])
                tmp.append(board[i + 2][j + 2])
                if not self.isnodifferent(tmp):
                    return False
        return True

    def isnodifferent(self, s):  # 判断列表中是否有相同的数字
        while '.' in s:
            s.remove('.')
        if s == []:
            return True
        flag = 0
        tmp = []
        tmp.append(s[0])  # 先加入第一个元素
        for i in range(1, len(s)):
            # 判断一个列表中书否有重复，
            # 将列表中的元素网tmp中append，同时判断下一个加入的元素是否在tmp中
            if s[i] in tmp:
                flag = 1
                break
            tmp.append(s[i])
        if flag:
            return False
        else:
            return True
# test
board = [[8, 1, 2, 7, 5, 3, 6, 4, 9],
         [9, 4, 3, 6, 8, 2, 1, 7, 5],
         [6, 7, 5, 4, 9, 1, 2, 8, 3],
         [1, 5, 4, 2, 3, 7, 8, 9, 6],
         [3, 6, 9, 8, 4, 5, 7, 2, 1],
         [2, 8, 7, 1, 6, 9, 5, 3, 4],
         [5, 2, 1, 9, 7, 4, 3, 6, 8],
         [4, 3, 8, 5, 2, 6, 9, 1, 7],
         [7, 9, 6, 3, 1, 8, 4, 5, 2]]

s = Solution()
print(s.isValidSudoku(board))