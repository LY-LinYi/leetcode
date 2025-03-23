"""
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

    示例 1：
    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    示例 2：
    输入：nums = [0,1]
    输出：[[0,1],[1,0]]

    示例 3：
    输入：nums = [1]
    输出：[[1]]
"""
class Solution(object):
    def permute(self, nums):
        """
        时间复杂度：O(n⋅n!)，其中 n 为 nums 的长度
        空间复杂度：O(n)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n
        
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i + 1)
                    on_path[j] = False
            
        dfs(0)
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))