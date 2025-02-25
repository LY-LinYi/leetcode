"""
    给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

    示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]

    示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
    def spiralOrder1(self, matrix):
        """
        标记法
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        total = m * n
        ans = [0] * total
        visited = [[False for _ in range(n)] for _ in range(m)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, col = 0, 0
        directionIndex = 0

        for i in range(total):
            ans[i] = matrix[row][col]
            visited[row][col] = True
            nextRow, nextCol = row + directions[directionIndex][0], col + directions[directionIndex][1]
            if not (0 <= nextRow < m and 0 <= nextCol < n and not visited[nextRow][nextCol]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            col += directions[directionIndex][1]

        return ans
    
    def spiralOrder2(self, matrix):
        """
        不标记法
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        total = m * n
        ans = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, col = 0, -1
        di = 0

        while len(ans) < total:
            print(m, n)
            dx, dy = directions[di]
            for _ in range(n):
                row += dx
                col += dy
                ans.append(matrix[row][col])
            di = (di + 1) % 4
            n, m = m - 1, n

        return ans

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    solution = Solution()
    print(solution.spiralOrder(matrix))