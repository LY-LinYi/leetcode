"""
    给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

    示例 1：
    输入：root = [4,2,7,1,3,6,9]
    输出：[4,7,2,9,6,3,1]

    示例 2：
    输入：root = [2,1,3]
    输出：[2,3,1]

    示例 3：
    输入：root = []
    输出：[]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root