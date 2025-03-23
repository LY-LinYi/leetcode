"""
    给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
    解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

    示例 1：
    输入：nums = [1,2,3]
    输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    示例 2：
    输入：nums = [0]
    输出：[[],[0]]
"""
class Solution:
    def subsets(self, nums):
        """
        输入的视角(选或不选)
        对于输入的 nums，考虑每个 nums[i] 是选还是不选，由此组合出 2^n 个不同的子集。
        dfs 中的 i 表示当前考虑到 nums[i] 选或不选。

        时间复杂度：O(n * 2^n)
        空间复杂度：O(n)
        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans =[]
        path = []
        
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            
        dfs(0)
        return ans
    

class Solution(object):
    def subsets(self, nums):
        """
        答案的视角(枚举选哪个)
        枚举子集（答案）的第一个数选谁，第二个数选谁，第三个数选谁，依此类推。
        dfs 中的 i 表示现在要枚举选 nums[i] 到 nums[n−1] 中的一个数，添加到 path 末尾。
        如果选 nums[j] 添加到 path 末尾，那么下一个要添加到 path 末尾的数，
        就要在 nums[j+1] 到 nums[n−1] 中枚举了。
        时间复杂度：O(2^n)，其中 n 为 nums 的长度。
        空间复杂度：O(1)。

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans =[]
        path = []
        
        def dfs(i):
            ans.append(path.copy())
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
            
        dfs(0)
        return ans