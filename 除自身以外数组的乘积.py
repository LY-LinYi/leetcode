"""
    给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
    题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
    请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

    示例 1:
    输入: nums = [1,2,3,4]
    输出: [24,12,8,6]

    示例 2:
    输入: nums = [-1,1,0,-3,3]
    输出: [0,0,9,0,0]
"""
class Solution(object):
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        l, r, ans = [0] * n, [0] * n, [0] * n
        l[0] = 1
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
            
        r[-1] = 1
        for i in range(n-2,-1,-1):
            r[i] = r[i+1] * nums[i+1]

        for i in range(n):
            ans[i] = l[i] * r[i]
        return ans
    
    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
            
        r = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * r
            r *= nums[i]

        return ans
        

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))