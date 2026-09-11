class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        isRowZero = False
        ROWS,COLS = len(matrix),len(matrix[0])

  
        for c in range(COLS):
            if matrix[0][c] == 0:
                isRowZero = True
                break
        for r in range(ROWS):
            if matrix[r][0] == 0:
                matrix[0][0] = 0
                break

        for r in range(1,ROWS):    
            for c in range(1,COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        

        

        for c in range(1,COLS):
            if matrix[0][c] == 0:
                for r in range(1,ROWS): 
                    matrix[r][c] = 0


        for r in range(1,ROWS): 
            if matrix[r][0] == 0:
                for c in range(1,COLS):
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        if isRowZero == True:
            for c in range(COLS):
                matrix[0][c] = 0

        
        