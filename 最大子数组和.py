"""
    给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    子数组是数组中的一个连续部分。

    示例 1：
    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

    示例 2：
    输入：nums = [1]
    输出：1

    示例 3：
    输入：nums = [5,4,-1,7,8]
    输出：23
"""
class Solution(object):
    def maxSubArray1(self, nums):
        """
        前缀和：通过前缀和，我们可以把子数组的元素和转换成两个前缀和的差
        :type nums: List[int]
        :rtype: int
        """
        ans = -float('inf')
        presum, min_presum = 0, 0
        for x in nums:
            presum += x
            ans = max(ans, presum - min_presum)
            min_presum = min(presum, min_presum)

        return ans
    
    def maxSubArray2(self, nums):
        """
        动态规划：定义f[i]表示以nums[i]结尾的最大子数组和
        如果nums[i]左边的子数组元素和是负的，就不用和左边的子数组拼在一起了。
        :type nums: List[int]
        :rtype: int
        """
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i -1], 0) + nums[i]
        return max(f)
        

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))