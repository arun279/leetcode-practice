'''
https://leetcode.com/problems/valid-sudoku/
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from run_tests import run_tests

class Solution:
    def isValidSudoku(self, board):
        # Check rows
        for row in board:
            if not self.isValidUnit(row):
                return False
        
        # Check columns
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        
        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValidUnit(sub_box):
                    return False
        
        return True
    
    def isValidUnit(self, unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))

s = Solution()
test_cases = [
    ([[["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]]], True),
    ([[["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]]], False)
]
run_tests.run_tests(s.isValidSudoku, test_cases)
