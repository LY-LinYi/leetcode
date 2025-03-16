"""
    给你一个链表数组，每个链表都已经按升序排列。
    请你将所有链表合并到一个升序链表中，返回合并后的链表。

    示例 1：
    输入：lists = [[1,4,5],[1,3,4],[2,6]]
    输出：[1,1,2,3,4,4,5,6]
    解释：链表数组如下：
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    将它们合并到一个有序链表中得到。
    1->1->2->3->4->4->5->6

    示例 2：
    输入：lists = []
    输出：[]

    示例 3：
    输入：lists = [[]]
    输出：[]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        分治法
        时间复杂度O(Nlogk)
        空间复杂度O(logk)
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[0]
        
        left = self.mergeKLists(lists[:k//2])
        right = self.mergeKLists(lists[k//2:])
        
        return self.mergeLists(left, right)
        
        
    def mergeLists(self, head1, head2):
        pre = dummy = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                pre.next = head1
                head1 = head1.next
            else:
                pre.next = head2
                head2 = head2.next
            pre = pre.next
            
        pre.next = head1 if head1 else head2
        return dummy.next