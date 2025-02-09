"""
    给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
    请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

    输入: nums = [100,4,200,1,3,2]
    输出: 4
    解释: 最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        num_list = sorted(list(set(nums)))
        max_len = 0
        tmp_len = 1
        x = num_list[0]
        for y in num_list[1:]:
            if y == x + 1:
                tmp_len += 1
            else:
                max_len = max(tmp_len, max_len)
                tmp_len = 1
            x = y
        max_len = max(tmp_len, max_len)
        return max_len
    
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                tmp_len = 1
                while num + 1 in num_set:
                    tmp_len += 1
                    num += 1
                max_len = max(tmp_len, max_len)
        return max_len


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    nums = [1,2,0,1]
    nums = [0, -1]
    print(Solution().longestConsecutive(nums))
