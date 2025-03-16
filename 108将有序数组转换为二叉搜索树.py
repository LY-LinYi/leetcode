"""
    给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

    示例 1：
    输入：nums = [-10,-3,0,5,9]
    输出：[0,-3,9,-10,null,5]
    解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

    示例 2：
    输入：nums = [1,3]
    输出：[3,1]
    解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        递归
        时间复杂度：O(n)
        空间复杂度：O(logn)
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # if len(nums) == 0:
        #     return None
        # if len(nums) == 1:
        #     return TreeNode(nums[0])
        if not nums:
            return None
        length = len(nums)
        m = length // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])
        return root