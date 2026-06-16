class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        top, bottom = 0, len(matrix) - 1

        while top < bottom:

            left, right = top, bottom

            for i in range(right-left):

                temp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]

                matrix[bottom-i][left] = matrix[bottom][right-i]

                matrix[bottom][right-i] = matrix[top+i][right]

                matrix[top+i][right] = temp





            top += 1
            bottom -= 1

# time complexity: O(n^2)
# space complexity: O(1)



        