"""
    给你二叉树的根结点 root ，请你将它展开为一个单链表：
    展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
    展开后的单链表应该与二叉树 先序遍历 顺序相同。
    
    示例 1：
    输入：root = [1,2,5,3,4,null,6]
    输出：[1,null,2,null,3,null,4,null,5,null,6]

    示例 2：
    输入：root = []
    输出：[]

    示例 3：
    输入：root = [0]
    输出：[0]
"""
class Solution(object):
    def flatten(self, root):
        """
        分治
        时间复杂度：O(N)
        空间复杂度：O(N)
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        return right_tail or left_tail or root
    
class Solution(object):
    head = None
    def flatten(self, root):
        """
        头插法：
            1.如果当前节点为空，返回。
            2.递归右子树。
            3.递归左子树。
            4.把 root.left 置为空。
            5.头插法，把 root 插在 head 的前面，也就是 root.right=head。
            6.现在 root 是链表的头节点，把 head 更新为 root。
        时间复杂度：O(N)
        空间复杂度：O(N)
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.head
        self.head = root