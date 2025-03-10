"""
    给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
    你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

    示例 1：
    输入：head = [1,2,3,4]
    输出：[2,1,4,3]

    示例 2：
    输入：head = []
    输出：[]

    示例 3：
    输入：head = [1]
    输出：[1]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs1(self, head):
        """
        哨兵迭代
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = dummpy = ListNode(next=head)
        while cur.next and cur.next.next:
            left = cur.next
            right = cur.next.next
            cur.next = right
            left.next = right.next
            right.next = left
            cur = cur.next.next
        return dummpy.next

    def swapPairs2(self, head):
        """
        递归
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        node1 = head
        node2 = head.next
        node3 = node2.next
        
        node1.next = self.swapPairs2(node3)
        node2.next = node1
        return node2
    

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(Solution().swapPairs2(head))