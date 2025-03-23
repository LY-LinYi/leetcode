"""
    在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
    值 0 代表空单元格；
    值 1 代表新鲜橘子；
    值 2 代表腐烂的橘子。
    每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
    返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

    示例 1：

    输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
    输出：4

    示例 2：
    输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
    输出：-1
    解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。

    示例 3：
    输入：grid = [[0,2]]
    输出：0
    解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1
                if x == 2:
                    q.append((i,j))

        ans = 0
        while q and fresh:
            ans += 1
            tmp = q
            q = []
            for x, y in tmp:
                for i, j in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                    if 0<=i<m and 0<=j<n and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        q.append((i, j))
        
        return -1 if fresh else ans

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    solution = Solution()
    print(solution.orangesRotting(grid))