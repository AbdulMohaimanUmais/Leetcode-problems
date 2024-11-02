class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        new_list = None
        current = head

        while current:
            new_node = current.next
            current.next = new_list
            new_list = current
            current = new_node
        
        return new_list