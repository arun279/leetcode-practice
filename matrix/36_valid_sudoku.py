'''
https://leetcode.com/problems/valid-sudoku/
'''
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
