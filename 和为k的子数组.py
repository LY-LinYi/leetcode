"""
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
    子数组是数组中元素的连续非空序列。

    示例 1: 
    输入: nums = [1,1,1], k = 2
    输出: 2

    示例 2: 
    输入: nums = [1,2,3], k = 3
    输出: 2
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for left in range(n):
            sums = 0
            for right in range(left, -1, -1):
                sums += nums[right]
                if sums == k:
                    ans += 1
        return ans


if __name__ == "__main__":
    nums = [0,0]
    k = 0
    print(Solution().subarraySum(nums, k))