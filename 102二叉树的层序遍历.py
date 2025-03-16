"""
    给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 
    （即逐层地，从左到右访问所有节点）。

    示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：[[3],[9,20],[15,7]]

    示例 2：
    输入：root = [1]
    输出：[[1]]

    示例 3：
    输入：root = []
    输出：[]
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        队列
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            result = []
            length = len(q)
            for _ in range(length):
                p = q.popleft()
                result.append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            ans.append(result)
        return ans
    