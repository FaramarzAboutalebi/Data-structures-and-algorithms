from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] += 1
    
    def count(self, point: List[int]) -> int:
        x,y = point
        res = 0

        for (px,py),count_P in self.points.items():
            if abs(px-x) != abs(py-y) or x == px or y == py:
                continue
            res += (count_P * 
                    self.points.get((x,py),0) *
                    self.points.get((px,y),0))
        return res
            
        
