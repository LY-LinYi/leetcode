"""
    给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
    示例 1：
    输入：root = [1,null,2,3]
    输出：[1,3,2]

    示例 2：
    输入：root = []
    输出：[]

    示例 3：
    输入：root = [1]
    输出：[1]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.in_order_tree_values(root, [])

    def in_order_tree_values(self, root, result):
        if result is None:
            return []
        if root:
            self.in_order_tree_values(root.left, result)
            result.append(root.val)
            self.in_order_tree_values(root.right, result)
        return result
        

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))