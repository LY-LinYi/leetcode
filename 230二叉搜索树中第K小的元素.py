"""
    给定一个二叉搜索树的根节点 root ，和一个整数 k ，
    请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

    示例 1：
    输入：root = [3,1,4,null,2], k = 1
    输出：1

    示例 2：
    输入：root = [5,3,6,2,4,null,null,1], k = 3
    输出：3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution1(object):
    def kthSmallest(self, root, k):
        """
        时间复杂度: O(n)
        空间复杂度: O(n)
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ans = 0
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            nonlocal k, ans
            k -= 1
            if k == 0:
                ans = root.val
            dfs(root.right)
        dfs(root)
        return ans
    

class Solution2(object):
        def kthSmallest(self, root, k):
            """
            :type root: Optional[TreeNode]
            :type k: int
            :rtype: int
            """
            in_order_list = self.in_order_traversal_to_list(root)
            return in_order_list[k-1]
            
        def in_order_traversal_to_list(self, root, result=None):
            if result is None:
                result = []
            if root:
                self.in_order_traversal_to_list(root.left, result)
                result.append(root.val)
                self.in_order_traversal_to_list(root.right, result)
            return result