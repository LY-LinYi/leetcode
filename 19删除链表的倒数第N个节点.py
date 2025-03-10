"""
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

    示例 1：
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

    示例 2：
    输入：head = [1], n = 1
    输出：[]

    示例 3：
    输入：head = [1,2], n = 1
    输出：[1]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd1(self, head, n):
        """
        计算链表长度后找到删除节点前一个节点
        时间复杂度：O(L)
        空间复杂度：O(1)
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        length = get_length(head)
        cur = dummpy = ListNode(next=head)
        for i in range(length-n):
            cur = cur.next
        cur.next = cur.next.next
        return dummpy.next
    
    def removeNthFromEnd2(self, head, n):
        """
        双指针
        时间复杂度：O(L)
        空间复杂度：O(1)
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        left = dummpy = ListNode(next=head)
        right = head
        for _ in range(n):
            right = right.next
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return dummpy.next
    
    def removeNthFromEnd3(self, head, n):
        """
        栈
        时间复杂度：O(n)
        空间复杂度：O(n)
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        cur = dummpy = ListNode(next=head)
        stack = list()
        while cur:
            stack.append(cur)
            cur = cur.next
            
        for _ in range(n):
            stack.pop()
            
        prev = stack[-1]
        prev.next = prev.next.next
        return dummpy.next
        

if __name__ == '__main__':
    s = Solution()
    print(s.removeNthFromEnd([1,2,3,4,5], 2))