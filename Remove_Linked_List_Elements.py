# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        newList = ListNode(next = head)
        current = newList
        val
        while current.next:
            if current.next == val:
                current.next = current.next.next
            else:
                current = current.next
        return newList.next
