
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head


        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, left, right):

        newList = ListNode()
        present = newList

        while left and right:
            if left < right:
                present.next = left
                left = left.next

            else:
                present.next = right
                right = right.next

            present = present.next

        present.next = left if left else right

        return newList.next