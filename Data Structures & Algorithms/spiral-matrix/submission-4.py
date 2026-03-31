class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle empty matrix case
        if not matrix or not matrix[0]:
            return []
            
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0
        x, y = 0, 0
        direction = "Y"
        increment = 1
        result = []

        while left <= right and top <= bottom:
            if direction == 'Y' and increment == 1:
                while y <= right:
                    result.append(matrix[x][y])
                    y += 1
                y -= 1  # step back after overshooting
                top += 1  # move top boundary down
                direction = 'X'
                x += 1  # go down to next row

            elif direction == 'X' and increment == 1:
                while x <= bottom:
                    result.append(matrix[x][y])
                    x += 1
                x -= 1
                right -= 1  # move right boundary left
                direction = 'Y'
                increment = -1  # now go in reverse Y direction
                y -= 1

            elif direction == 'Y' and increment == -1:
                while y >= left:
                    result.append(matrix[x][y])
                    y -= 1
                y += 1
                bottom -= 1  # move bottom boundary up
                direction = 'X'
                increment = -1  # explicitly set increment to -1
                x -= 1

            elif direction == 'X' and increment == -1:
                while x >= top:
                    result.append(matrix[x][y])
                    x -= 1
                x += 1
                left += 1  # move left boundary right
                direction = 'Y'
                increment = 1  # back to normal Y direction
                y += 1  # Missing: move to next column after going up

        return result