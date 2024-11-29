class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        else:
            return head