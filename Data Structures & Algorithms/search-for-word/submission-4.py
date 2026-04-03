class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True

            # ✅ Bounds check FIRST
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit:
                return False

            if board[r][c] != word[i]:
                return False

            visit.add((r, c))

            for dr, dc in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                if dfs(i + 1, r + dr, c + dc):
                    return True

            visit.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True 
        return False
