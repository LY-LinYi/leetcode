"""
    你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
    在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
    其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

    例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
    请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

    示例 1：
    输入：numCourses = 2, prerequisites = [[1,0]]
    输出：true
    解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

    示例 2：
    输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
    输出：false
    解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        题意：给定一个有向图，判断图中是否有环
        三色标记法：0未访问，1正在访问，2已访问
        时间复杂度：O(n+m)，n是numCourses，m是prerequisites的长度
        空间复杂度：O(n+m)
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        p = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            p[b].append(a)
        colors = [0] * numCourses
        
        def dfs(x):
            colors[x] = 1
            for y in p[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            return False
            
        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False
        return True
    
    
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(Solution().canFinish(numCourses, prerequisites))