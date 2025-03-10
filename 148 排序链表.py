"""
    给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 

    示例 1：
    输入：head = [4,2,1,3]
    输出：[1,2,3,4]

    示例 2：
    输入：head = [-1,5,3,4,0]
    输出：[-1,0,3,4,5]

    示例 3：
    输入：head = []
    输出：[]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        自顶向下分治法，快慢指针拆分链表为两部分，再合并两个有序链表
        时间复杂度: O(nlogn)
        空间复杂度: O(logn)
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        head2 = self.middleNode(head)
        head = self.sortList(head)
        head2 = self.sortList(head2)
        ans = self.mergeLinked(head, head2)
        return ans
        
        
    def mergeLinked(self, head1, head2):
        cur = dummy = ListNode()
        
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        
        cur.next = head1 if head1 else head2
        return dummy.next
        
        
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow