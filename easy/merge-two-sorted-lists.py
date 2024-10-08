# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is None:
            return None

        elif l1 is None:
            return l2

        elif l2 is None:
            return l1

        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        curr = head

        while l1 and l2:
            if l1 >= l2:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return head.next
