"""
    给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
    图示两个链表在节点 c1 开始相交：

    题目数据 保证 整个链式结构中不存在环。
    注意，函数返回结果后，链表必须 保持其原始结构。
    自定义评测：

    评测系统 的输入如下（你设计的程序 不适用 此输入）：

    intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
    listA - 第一个链表
    listB - 第二个链表
    skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
    skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
    评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_linked(head):
    result = [] 
    while head:
        result.append(str(head.val))
        head = head.next
    print('->'.join(result))
    
def build_linked(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def build_intersecting_linked(intersectVal, listA, listB, skipA, skipB):
    if intersectVal == 0:
        listA = build_linked(listA)
        listB = build_linked(listB)
        return listA, listB, None
    
    intersecting_part = None
    if intersectVal != 0:
        intersecting_part = build_linked(listA[skipA:])
        
    listA_head = build_linked(listA[:skipA])
    currentA = listA_head
    if currentA:
        while currentA.next:
            currentA = currentA.next
        currentA.next = intersecting_part
        
    listB_head = build_linked(listB[:skipB])
    currentB = listB_head
    if currentB:
        while currentB.next:
            currentB = currentB.next
        currentB.next = intersecting_part
    
    return listA_head, listB_head, intersecting_part

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
    

if __name__ == "__main__":
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    skipA = 2
    skipB = 3
    listA_head, listB_head, intersecting_part = build_intersecting_linked(intersectVal, listA, listB, skipA, skipB)
    print(Solution().getIntersectionNode(listA_head, listB_head).val)