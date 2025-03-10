"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        哨兵节点，迭代
        时间复杂度O(n)
        空间复杂度O(1)
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            dummy.next = ListNode(carry % 10)
            carry = carry // 10
            dummy = dummy.next
        return pre.next
    
    def addTwoNumbers2(self, l1, l2):
        """
        递归
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.addTwoNumberFunc(l1, l2, 0)
        
    def addTwoNumberFunc(self, l1, l2, carry):
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        s = carry + l1.val + (l2.val if l2 else 0)
        l1.val = s % 10
        l1.next = self.addTwoNumberFunc(l1.next, l2.next if l2 else None, s // 10)
        return l1


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

        